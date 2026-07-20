#!/usr/bin/env python3
"""Validate the dependency-free VibeLib Cursor plugin structure."""

from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path
from typing import Any


EXPECTED_SKILLS = (
    "immerse",
    "xray",
    "reconcile",
    "driftcheck",
    "curate",
)
EXPECTED_CONFORMANCE_CASES = tuple(f"VC-{number:02d}" for number in range(1, 20))
SHARED_SKILL_MARKERS = (
    "## Operating stance",
    "not change the project on your own initiative.",
    "## Invocation contract",
    "Mentioning, quoting,\nattaching, or reading this skill is not invocation.",
    "In a composed prompt",
    "Treat every unscoped parameter as ambiguous.",
    "Apply precedence in this order",
    "Converse: address the user directly",
    "let the user choose.",
)
SKILL_SPECIFIC_MARKERS = {
    "immerse": (
        "## Parameter semantics",
        "evidence and coverage map",
        "Inspected, inferred, and uninspected",
    ),
    "xray": (
        "## Parameter semantics",
        "## Validation safety",
        "Authorization alone never makes an unsafe test acceptable.",
    ),
    "reconcile": (
        "## Parameter semantics",
        "## Decision sufficiency gate",
        "Never treat model-chosen preferences as user-approved",
    ),
    "driftcheck": (
        "## Parameter semantics",
        "## Orthogonal finding model",
        "## Ranking fields",
        "`Relationship: Not assessable`",
    ),
    "curate": (
        "## Parameter semantics",
        "## Autonomy and modes",
        "## Gated actions",
        "## Live and physical state safety",
        "## Apply and validation",
        "## The confirmation gate",
        "single confirmation gate",
    ),
}
SKILL_NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SEMVER_PATTERN = re.compile(
    r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)"
    r"(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$"
)


class Validation:
    """Collect validation errors so one run reports every structural issue."""

    def __init__(self) -> None:
        self.errors: list[str] = []

    def require(self, condition: bool, message: str) -> None:
        if not condition:
            self.errors.append(message)


def parse_scalar(value: str) -> Any:
    value = value.strip()
    if value == "true":
        return True
    if value == "false":
        return False
    if value == "null":
        return None
    if len(value) >= 2 and value[0] == value[-1] == '"':
        try:
            return json.loads(value)
        except json.JSONDecodeError:
            return value[1:-1]
    if len(value) >= 2 and value[0] == value[-1] == "'":
        return value[1:-1].replace("''", "'")
    return value


def parse_frontmatter(path: Path, validation: Validation) -> tuple[dict[str, Any], str]:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as error:
        validation.errors.append(f"{path}: cannot read file: {error}")
        return {}, ""

    lines = text.splitlines()
    if not lines or lines[0] != "---":
        validation.errors.append(f"{path}: must start with YAML frontmatter")
        return {}, text

    try:
        closing_index = lines.index("---", 1)
    except ValueError:
        validation.errors.append(f"{path}: frontmatter has no closing delimiter")
        return {}, ""

    metadata: dict[str, Any] = {}
    for line_number, line in enumerate(lines[1:closing_index], start=2):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line[:1].isspace() or ":" not in line:
            validation.errors.append(
                f"{path}:{line_number}: expected a top-level 'key: value' field"
            )
            continue
        key, raw_value = line.split(":", 1)
        key = key.strip()
        if not key or key in metadata:
            validation.errors.append(
                f"{path}:{line_number}: invalid or duplicate frontmatter key"
            )
            continue
        metadata[key] = parse_scalar(raw_value)

    body = "\n".join(lines[closing_index + 1 :]).strip()
    return metadata, body


def load_manifest(path: Path, validation: Validation) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        validation.errors.append(f"{path}: plugin manifest is missing")
        return {}
    except (OSError, json.JSONDecodeError) as error:
        validation.errors.append(f"{path}: invalid plugin manifest: {error}")
        return {}

    if not isinstance(data, dict):
        validation.errors.append(f"{path}: manifest root must be a JSON object")
        return {}
    return data


def validate_manifest(root: Path, validation: Validation) -> dict[str, Any]:
    manifest_path = root / ".cursor-plugin" / "plugin.json"
    manifest = load_manifest(manifest_path, validation)

    validation.require(
        manifest.get("name") == "vibelib",
        f"{manifest_path}: name must be 'vibelib'",
    )
    validation.require(
        isinstance(manifest.get("description"), str)
        and bool(manifest["description"].strip()),
        f"{manifest_path}: description must be a non-empty string",
    )
    version = manifest.get("version")
    validation.require(
        isinstance(version, str) and bool(SEMVER_PATTERN.fullmatch(version)),
        f"{manifest_path}: version must use semantic versioning",
    )
    validation.require(
        manifest.get("license") == "MIT",
        f"{manifest_path}: license must be 'MIT'",
    )
    return manifest


def validate_skills(root: Path, validation: Validation) -> None:
    skills_root = root / "skills"
    if not skills_root.is_dir():
        validation.errors.append(f"{skills_root}: skills directory is missing")
        return

    discovered = {
        child.name
        for child in skills_root.iterdir()
        if child.is_dir() and (child / "SKILL.md").is_file()
    }
    expected = set(EXPECTED_SKILLS)
    validation.require(
        discovered == expected,
        (
            f"{skills_root}: expected skills {sorted(expected)}, "
            f"found {sorted(discovered)}"
        ),
    )

    for skill_name in EXPECTED_SKILLS:
        path = skills_root / skill_name / "SKILL.md"
        metadata, body = parse_frontmatter(path, validation)
        if not metadata:
            continue

        validation.require(
            metadata.get("name") == skill_name,
            f"{path}: name must match parent folder '{skill_name}'",
        )
        validation.require(
            bool(SKILL_NAME_PATTERN.fullmatch(str(metadata.get("name", "")))),
            f"{path}: name must be lowercase kebab-case",
        )
        description = metadata.get("description")
        validation.require(
            isinstance(description, str) and bool(description.strip()),
            f"{path}: description must be a non-empty string",
        )
        if isinstance(description, str):
            validation.require(
                len(description) <= 1024,
                f"{path}: description exceeds 1024 characters",
            )
            validation.require(
                "Invoke explicitly" in description,
                f"{path}: description must state when to invoke the skill",
            )
        validation.require(
            metadata.get("disable-model-invocation") is True,
            f"{path}: disable-model-invocation must be true",
        )
        validation.require(
            "paths" not in metadata,
            f"{path}: paths must be omitted so the skill is globally available",
        )
        validation.require(
            metadata.get("user-invocable", True) is not False,
            f"{path}: user-invocable must not be false",
        )
        validation.require(bool(body), f"{path}: skill body must not be empty")
        for marker in (*SHARED_SKILL_MARKERS, *SKILL_SPECIFIC_MARKERS[skill_name]):
            validation.require(
                marker in body,
                f"{path}: required contract marker is missing: {marker!r}",
            )

        try:
            line_count = len(path.read_text(encoding="utf-8").splitlines())
        except OSError:
            continue
        validation.require(
            line_count < 500,
            f"{path}: SKILL.md must stay under 500 lines (found {line_count})",
        )


def validate_conformance_cases(root: Path, validation: Validation) -> None:
    path = root / "tests" / "conformance-cases.md"
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as error:
        validation.errors.append(f"{path}: cannot read conformance cases: {error}")
        return

    case_ids = re.findall(r"^## (VC-\d{2}):", text, flags=re.MULTILINE)
    expected = set(EXPECTED_CONFORMANCE_CASES)
    discovered = set(case_ids)
    validation.require(
        discovered == expected,
        (
            f"{path}: expected conformance cases {sorted(expected)}, "
            f"found {sorted(discovered)}"
        ),
    )
    validation.require(
        len(case_ids) == len(discovered),
        f"{path}: conformance case identifiers must be unique",
    )


def validate_supporting_files(root: Path, validation: Validation) -> None:
    required_files = (
        root / "README.md",
        root / "LICENSE",
        root / "scripts" / "install-user.sh",
        root / "examples" / "basic.md",
        root / "examples" / "parameters-and-roles.md",
        root / "examples" / "composed.md",
        root / "tests" / "conformance-cases.md",
    )
    for path in required_files:
        validation.require(path.is_file(), f"{path}: required file is missing")

    installer = root / "scripts" / "install-user.sh"
    if installer.exists() and os.name != "nt":
        validation.require(
            os.access(installer, os.X_OK),
            f"{installer}: installer must be executable",
        )


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    validation = Validation()

    manifest = validate_manifest(root, validation)
    validate_skills(root, validation)
    validate_conformance_cases(root, validation)
    validate_supporting_files(root, validation)

    if validation.errors:
        print("VibeLib validation failed:", file=sys.stderr)
        for error in validation.errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    version = manifest.get("version", "unknown")
    print(
        f"VibeLib {version} is valid: "
        f"{len(EXPECTED_SKILLS)} explicit-only skills and "
        f"{len(EXPECTED_CONFORMANCE_CASES)} conformance cases discovered."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
