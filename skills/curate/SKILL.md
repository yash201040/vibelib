---
name: curate
description: "Assesses and safely updates project artifacts for coherence, currency, usefulness, and reproducibility."
disable-model-invocation: true
---

# Curate

Bring project artifacts into a coherent, current, useful, and reproducible
state. Identify stale artifacts and propose consolidation, archival,
quarantine, or deletion without erasing history or provenance.

## Invocation contract

Run only after the user explicitly selects `/curate`. Never invoke another
VibeLib skill on the user's behalf.

Recognize these optional keyed parameters:

- `mode`: `report`, `update`, or `update-and-prune`; default `report`
- `scope`, `source-of-truth`, `include`, `exclude`, `preserve`
- `staleness-basis`, `generated-policy`, `disposition`, `verification`
- `role`: `background`, `foreground`, or `standalone`
- `output`

An unambiguous request to update named, non-destructive artifacts may select
`update`; otherwise use `report`. Never infer `update-and-prune`.

Treat non-parameter text as the primary request. If there is a separate primary
request, default `role` to `background`; otherwise default it to `standalone`.
An explicit role wins.

When other skills are explicitly selected in the same prompt, share the
source-of-truth and evidence context and produce one integrated deliverable.

## Modes

### Report

Inspect, classify, and propose changes. Do not modify anything.

### Update

Update explicitly requested non-destructive artifacts. Do not archive or
delete.

### Update and prune

Update approved artifacts first. Then present an exact archive or deletion
proposal and stop for explicit confirmation. Selecting this mode does not
itself confirm any destructive action.

## Safety contract

1. Default to report when modification intent is ambiguous.
2. Never delete from a general request such as "clean everything."
3. Never permanently overwrite irreplaceable or authoritative material without
   explicit authorization.
4. Prefer archive or quarantine when uncertainty is material.
5. Do not classify an item as unused from static text search alone.
6. Check configuration, dynamic loading, scheduled workflows, notebooks,
   external consumers, and human processes when relevant.
7. Preserve raw data, provenance, accepted decisions, audit evidence,
   published deliverables, and regulated records unless explicitly authorized.
8. Never reveal secrets while reporting curation findings.

## Artifact classifications

Use one or more of:

- Authoritative
- Active source
- Current derived
- Generated but unverified
- Stale derived
- Contradictory
- Broken
- Duplicate
- Orphaned
- Superseded
- Historical or provenance
- Out of scope
- Unknown

## Workflow

1. Identify authoritative sources.
2. Establish dependency order.
3. Identify generated and manually maintained artifacts.
4. Inventory only the requested scope and necessary dependencies.
5. Detect staleness, contradiction, duplication, broken references, and
   orphaning.
6. Determine which artifacts can be reproduced.
7. Build an ordered update plan.
8. Apply approved non-destructive updates only when the mode permits.
9. Validate regenerated or updated artifacts.
10. Prepare an exact disposition ledger.
11. Request confirmation before every archive or deletion action.
12. Report completed actions and unresolved items.

Prefer this dependency order:

1. objectives, accepted decisions, and contracts
2. source data definitions and configuration
3. implementation, methods, and notebooks
4. tests and validation
5. generated outputs, tables, models, and figures
6. documentation, screenshots, reports, and handoff material

When a reproducible generator exists, update the source or generator and
regenerate; do not manually patch generated output.

## Destructive confirmation gate

Before archive or deletion, list every candidate with:

- exact item path or identifier
- proposed action
- reason
- evidence
- dependency risk
- recovery method

Then state exactly:

> No archive or deletion action has been performed. Confirm this exact list,
> modify it, or cancel.

Confirmation applies only to the exact listed items and actions. A changed
action or newly discovered candidate requires separate confirmation. After
presenting the ledger, stop and wait; do not treat a prior broad request,
selected mode, or silence as confirmation.

## Role behavior

### Background

- Curate only artifacts needed for the primary deliverable.
- Avoid a project-wide cleanup report.
- Surface blocked updates, contradictions, and destructive actions that need
  approval.

### Foreground

- Make relevant stale artifacts and proposed updates visible.
- Integrate curation status into the requested deliverable.

### Standalone

Use this structure:

1. Curation status
2. Source-of-truth map
3. Artifact inventory
4. Stale or inconsistent artifacts
5. Update plan or completed updates
6. Validation results
7. Disposition ledger
8. Items awaiting confirmation
9. Unknowns and blocked items
10. Reproducibility and handoff notes

## Evidence rules

- Cite concrete project evidence for classifications and dependencies.
- Label consequential claims as **Observed**, **Inferred**, or **Unknown**.
- Preserve conflicting evidence and uncertainty.
- Distinguish current source artifacts from generated outputs.
- Record what changed and how it was validated.

## Boundaries

Do not redesign under the label of cleanup, delete based only on age or naming,
remove decision-useful failed experiments without confirmation, rewrite project
history to appear cleaner, automatically resolve objective drift, or treat
unfamiliar files as unnecessary.
