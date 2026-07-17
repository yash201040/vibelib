# Parameters and roles

Skill selection is deterministic; parameters remain ordinary prompt text that
Cursor Agent interprets. Use concise `key: value` lines when a workflow needs a
clear scope or output mode.

## Reconcile alternatives

```text
/reconcile
scope: persistence layer
role: standalone
option A: retain SQLite and add migration discipline
option B: move to PostgreSQL now
criteria: correctness, deployment complexity, operating cost, reversibility
priority: correctness first, then reversibility
constraints: one maintainer; beta launch in four weeks
horizon: beta launch through the first year of operation
evidence-standard: supported

Recommend an option and state what evidence would change the recommendation.
```

## Check drift against an explicit baseline

```text
/driftcheck
baseline: accepted requirements in docs/product-requirements.md
current: current implementation and user documentation
scope: account deletion
dimensions: implementation-or-behavior, documentation, operation
rank-by: severity, decision-impact, confidence
role: foreground

Write a release-readiness assessment.
```

## Curate without destructive authority

```text
/curate
mode: update-and-prune
scope: generated reports and their documentation
source-of-truth: scripts/generate_reports.py and config/reporting.yaml
preserve: published reports and accepted decision records
role: standalone
```

`update-and-prune` may update approved, reversible content. It still must stop
after presenting the exact ledger for moves, quarantine, consolidation,
replacement, archival, disabling, or deletion. The mode is not confirmation
for any gated action.

## Bottom-level investigation

```text
/xray
segment: src/time/normalize.ts
level: bottom
focus: timestamp units, inclusive boundaries, null handling, and downstream
  record-count impact
role: standalone
```

Use explicit roles in consequential requests. If omitted, a native workflow
request defaults to `standalone`; `background` applies only when the prompt asks
for a distinct deliverable that the workflow should support.
