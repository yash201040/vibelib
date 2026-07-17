# VibeLib

VibeLib is a dependency-free Cursor plugin containing five explicit analysis
workflows:

- `/immerse` builds a verified project mental model.
- `/xray` performs an adversarial, evidence-based review.
- `/reconcile` compares alternatives and supports a defensible decision.
- `/driftcheck` compares an authoritative baseline with the current state.
- `/curate` assesses and safely updates project artifacts.

The workflows are Cursor Agent Skills, not an MCP server. They need no project
Git repository, package manager, virtual environment, or external service.

## Deterministic activation

Every skill declares:

```yaml
disable-model-invocation: true
```

Cursor therefore includes a VibeLib skill only when you explicitly select its
`/skill-name` in Agent chat. Installed skills appear when you type `/` and
search the autocomplete menu.

This makes **skill selection deterministic**. It does not make the model's
analysis or wording deterministic: after selection, Cursor Agent still
interprets the request, inspects available evidence, and performs the workflow.

VibeLib has no always-on router. Words such as "immerse", "curate", or "xray"
in ordinary prose do not activate a workflow.

## Install

### Cursor Marketplace

Once VibeLib is published, install it from Cursor's **Customize** page and
choose **User** scope. A user-scoped installation makes the five skills
available in every folder you open, including folders without Git.

The initial repository is Marketplace-compatible but is not automatically
published by this source tree.

### Test the plugin locally

Download or clone this repository anywhere. From the repository root, copy the
plugin into Cursor's local plugin directory:

```sh
mkdir -p "$HOME/.cursor/plugins/local"
test ! -e "$HOME/.cursor/plugins/local/vibelib"
mkdir "$HOME/.cursor/plugins/local/vibelib"
cp -R .cursor-plugin skills README.md LICENSE \
  "$HOME/.cursor/plugins/local/vibelib/"
```

The `test` guard prevents overwriting an existing local installation. Inspect
and remove or rename an existing destination explicitly before replacing it.
Cursor reloads local plugins when this directory changes; if the skills are not
visible, restart Cursor or run `Developer: Reload Window`.

Cursor documentation also suggests symlinking a development repository, but
Cursor 3.12.10 rejects local-plugin symlinks whose targets are outside
`~/.cursor/plugins/local`. A real copy is the verified portable setup.

This method loads the plugin manifest and all five skills. It does not matter
whether the folder where you later use a skill is a Git repository.

### Personal-skill fallback

From an unpacked copy of this repository, run:

```sh
./scripts/install-user.sh
```

The script copies the five skill directories into `~/.cursor/skills/`. It
checks every destination first and aborts without overwriting an existing skill
with the same name.

Do not install VibeLib both as a plugin and as copied personal skills. Cursor
does not document precedence for duplicate skill names.

To remove a copied personal installation, inspect and then remove only these
directories:

```text
~/.cursor/skills/immerse
~/.cursor/skills/xray
~/.cursor/skills/reconcile
~/.cursor/skills/driftcheck
~/.cursor/skills/curate
```

## Use

Type `/` in Cursor Agent chat and select a VibeLib skill. Add the request and
optional keyed parameters as ordinary prompt text:

```text
/immerse
segment: evaluation pipeline
level: mid
role: foreground
focus: transformations and validation gates

Give me a concise orientation for a new maintainer.
```

Recognized parameters are documented in each skill. Free-form prompts also
work:

```text
/xray
Review the checkout flow for authorization gaps and unsafe retry behavior.
```

### Roles

Most skills support:

- `background`: use the workflow to improve another requested deliverable and
  surface only material results
- `foreground`: make the workflow analysis visible while integrating it into
  the requested deliverable
- `standalone`: return the workflow's standard report

If a prompt contains a separate deliverable, the default is `background`.
Otherwise the default is `standalone`. Use an explicit role when composing
skills or when the distinction matters.

### Compose workflows

Select every workflow you want in the same prompt:

```text
/immerse
/xray
/reconcile

Immerse:
  segment: model evaluation
  level: high
  role: background

Xray:
  segment: model evaluation
  level: mid
  role: foreground
  focus: leakage, metric misuse, and reproducibility

Reconcile:
  option A: retain the current evaluation
  option B: rebuild with temporal external validation
  criteria: validity, release risk, reproducibility, and effort
  role: foreground

Write one release decision memo, not separate workflow reports.
```

Each selected skill shares the current prompt and evidence context. VibeLib
instructs the agent to integrate overlapping work and avoid duplicate reports.
It never auto-selects an unrequested VibeLib skill.

More examples are in [`examples/`](examples/).

## Repository structure

```text
.
├── .cursor-plugin/
│   └── plugin.json
├── skills/
│   ├── immerse/SKILL.md
│   ├── xray/SKILL.md
│   ├── reconcile/SKILL.md
│   ├── driftcheck/SKILL.md
│   └── curate/SKILL.md
├── examples/
├── scripts/
└── README.md
```

Cursor discovers each direct child of `skills/` that contains a `SKILL.md`.
The plugin itself has no executable runtime.

## Validate

Contributors can run the structural validator with the Python standard library:

```sh
python3 scripts/validate.py
```

The validator checks the plugin manifest, expected skill inventory, folder/name
agreement, required frontmatter, and explicit-only invocation. Python is only
needed for repository validation, not to install or use the plugin.

Before publishing, also load the plugin locally and verify:

1. All five names appear in `/` autocomplete.
2. Selecting a name loads only that skill.
3. Ordinary prose does not activate a VibeLib skill.
4. Several explicitly selected skills can contribute to one response.

## Publish

Cursor Marketplace plugins are distributed from public Git repositories and
reviewed before listing. After setting the final repository metadata:

1. Test this repository through `~/.cursor/plugins/local/vibelib`.
2. Push it to a public GitHub repository.
3. Submit the repository URL at
   [cursor.com/marketplace/publish](https://cursor.com/marketplace/publish).

See Cursor's [Agent Skills documentation](https://cursor.com/docs/skills) and
[Plugins documentation](https://cursor.com/docs/plugins) for the current
platform behavior.

## License

VibeLib is released under the [MIT License](LICENSE).
