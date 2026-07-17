# Basic invocations

Type `/` in Cursor Agent chat, choose the skill from autocomplete, and then add
the request.

## Free-form request

```text
/xray
Review the authentication flow for authorization gaps, unsafe defaults, and
missing failure handling. Report only material findings.
```

Because `/xray` was explicitly selected, Cursor includes the Xray skill.

## Standalone orientation

```text
/immerse
segment: entire project
level: top
role: standalone
focus: objective, major components, current state, and critical junctions
```

With no separate deliverable, `standalone` returns the workflow's standard
orientation structure.

## Background contribution

```text
/immerse
segment: billing pipeline
level: mid
role: background

Write an onboarding guide for the engineer taking ownership of billing.
```

The requested output is the onboarding guide. Immerse contributes only the
project context that materially improves it.

## Non-invocation

```text
Write an immersive introduction to this repository.
```

This does not select `/immerse`. VibeLib skills have automatic model invocation
disabled, so ordinary prose is not a trigger.
