# VibeLib

Explicit, reusable analysis workflows for Cursor Agent.

VibeLib provides five slash-invoked Agent Skills:

- `/immerse` — understand a project or selected area
- `/xray` — find material flaws, failure modes, and risks
- `/reconcile` — compare alternatives and support a defensible decision
- `/driftcheck` — compare an authoritative baseline with the current state
- `/curate` — assess project artifacts and propose updates behind a
  confirmation gate

Every skill is advisory by default: it highlights what it found, discusses the
options and paths worth considering, and leaves the decision to you. No skill
changes your project on its own initiative. The one exception is `/curate`,
which can apply reversible edits automatically when you pass `mode: auto`;
without it, `/curate` gathers every proposed edit behind a single confirmation
gate and applies nothing until you confirm.

It works in Cursor IDE and the desktop Agents Window. There is no MCP server,
package dependency, virtual environment, or runtime to maintain.

## Quick start

### 1. Install

Until the Marketplace listing is available, clone or download this repository.
On macOS or Linux:

```sh
git clone --depth 1 https://github.com/yash201040/vibelib.git
cd vibelib
./scripts/install-user.sh
```

The installer copies all five skills into `~/.cursor/skills/` and refuses to
overwrite existing skills. Your work folders do not need Git or any language
environment.

If you downloaded the ZIP, run `./scripts/install-user.sh` from the extracted
folder. On Windows, copy each folder inside `skills/` into
`%USERPROFILE%\.cursor\skills\`.

### 2. Reload Cursor

Run `Developer: Reload Window` from the Command Palette if the skills do not
appear immediately.

### 3. Invoke a skill

Type `/` in Cursor Agent chat, select a VibeLib skill, and describe the task:

```text
/xray
Review the checkout flow for authorization gaps and unsafe retry behavior.
```

Or provide optional parameters for tighter control:

```text
/immerse
segment: evaluation pipeline
level: mid
role: foreground
focus: transformations and validation gates

Give me a concise orientation for a new maintainer.
```

## Explicit activation

VibeLib skills have automatic model invocation disabled. A skill is loaded only
when you explicitly select `/skill-name`; ordinary words such as "immerse" or
"curate" do not trigger it.

This makes skill selection deterministic. The Agent's analysis and wording
remain model-generated and can vary between runs.

## Common options

Each skill documents its own parameters. Common options include:

- `segment` or `scope` — what to inspect
- `level` — `top`, `high`, `mid`, `low`, or `bottom`
- `focus` — questions or risks to prioritize
- `role`:
  - `background` — improve another requested deliverable
  - `foreground` — highlight findings, discuss the options, and let you decide
    within the requested deliverable
  - `standalone` — return the workflow's complete report

You can explicitly select several skills in one prompt. See the
[`examples/`](examples/) directory for basic, parameterized, hierarchical, and
composed requests.

## Marketplace

VibeLib is packaged as a Cursor plugin. After its Marketplace listing is
approved, users will be able to install it once at **User** scope from Cursor's
**Customize** page and use it in any folder.

Do not install both the Marketplace plugin and copied personal skills; duplicate
skill-name precedence is not documented.

## Compatibility

- Cursor IDE and desktop Agents Window use the same user-scoped skills.
- Cursor CLI supports Agent Skills, but plugin discovery may require explicit
  CLI configuration.
- Cloud Agents do not automatically inherit locally installed user skills.

## Development

Validate the plugin with Python's standard library:

```sh
python3 scripts/validate.py
```

Behavioral invariants and prompt-level evaluation cases are documented in
[`tests/conformance-cases.md`](tests/conformance-cases.md).

For local plugin testing, copy `.cursor-plugin/`, `skills/`, `README.md`, and
`LICENSE` into `~/.cursor/plugins/local/vibelib/`. Some Cursor versions reject
development symlinks whose targets are outside the local plugin directory.

See Cursor's [Agent Skills documentation](https://cursor.com/docs/skills) and
[Plugins documentation](https://cursor.com/docs/plugins).

## License

[MIT](LICENSE)
