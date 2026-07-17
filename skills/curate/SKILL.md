---
name: curate
description: "Assesses and safely updates project artifacts for coherence and reproducibility. Invoke explicitly when artifact curation or cleanup is requested."
disable-model-invocation: true
---

# Curate

Bring project artifacts into a coherent, current, useful, and reproducible
state. Identify stale artifacts and propose consolidation, archival,
quarantine, or deletion without erasing history or provenance.

## Invocation contract

Run only after the user explicitly selects `/curate`. Mentioning, quoting,
attaching, or reading this skill is not invocation. Never invoke another
VibeLib skill on the user's behalf.

Recognize these optional keyed parameters:

- `mode`: `report`, `update`, or `update-and-prune`; default `report`
- `scope`, `source-of-truth`, `include`, `exclude`, `preserve`
- `staleness-basis`, `generated-policy`, `disposition`, `verification`
- `role`: `background`, `foreground`, or `standalone`
- `output`

An unambiguous request to update named, non-destructive artifacts may select
`update`; otherwise use `report`. Never infer `update-and-prune`.

In a single-skill prompt, unscoped recognized parameters belong to Curate and
unknown keyed fields are additional context. A native Curate request asks for
artifact assessment or approved updates and defaults to `standalone`. Default
to `background` only when the user requests a distinct primary deliverable,
such as a release package or handoff, that curation should support. If
`role: background` is explicit but no separate deliverable exists, ask what the
curation should support.

In a composed prompt, bind parameters under a `Curate:` heading to this skill.
Treat every unscoped parameter as ambiguous. A parameter may apply to multiple
skills only when the user places it under an explicit `Shared:` heading and
every named skill recognizes the same meaning; otherwise ask for namespaced
parameters. Treat `Request:` or the final non-parameter instruction as the
global deliverable.

Apply precedence in this order: the safety and confirmation contract,
explicit Curate parameters, explicit global request and format, then defaults.
A global output format controls the final response; Curate's `output` controls
only its contribution. Share source-of-truth and evidence context with other
explicitly selected skills. If there is a global deliverable, produce one
integrated response. If several skills are `standalone` without a global
deliverable, use one response with a clearly labeled section per skill in
invocation order.

## Parameter semantics

- `scope`: boundary of the inventory and allowed updates
- `source-of-truth`: authoritative artifacts or the rule for identifying them
- `include`: artifacts or categories that must be considered
- `exclude`: artifacts or categories not to inspect or change; disclose blocked
  dependency analysis
- `preserve`: items or classes that must not be changed, moved, disabled, or
  removed
- `staleness-basis`: evidence used to judge currency, such as an accepted
  decision, source revision, dependency version, timestamp, checksum,
  calibration state, or reproducibility result; if omitted, derive and state
  the basis before classifying staleness
- `disposition`: requested candidate actions such as keep, update, regenerate,
  move, archive, quarantine, consolidate, replace, or delete; it does not
  authorize a gated action
- `verification`: checks required after updates, including expected outputs,
  dependency checks, calibration, review, or recovery validation
- `output`: structure or detail for Curate's contribution, subordinate to an
  explicit global deliverable

`generated-policy` accepts:

- `regenerate-from-source` (default when reproducible and in scope)
- `preserve-current`
- `report-only`

If a supplied value falls outside these forms or conflicts with `preserve`,
ask for clarification.

## Modes

### Report

Inspect, classify, and propose changes. Do not modify anything.

### Update

Update explicitly requested content in named artifacts when the change is
reversible and does not alter artifact identity or availability. Do not perform
any gated action.

### Update and prune

Update approved artifacts first. Then present an exact proposal for every gated
action and stop for explicit confirmation. Selecting this mode does not itself
confirm any gated action.

## Safety contract

1. Default to report when modification intent is ambiguous.
2. Never perform a gated action from a general request such as "clean
   everything."
3. Never permanently overwrite irreplaceable or authoritative material without
   exact-item confirmation and a recovery method.
4. Prefer proposing archive or quarantine over deletion when uncertainty is
   material; all remain gated actions.
5. Do not classify an item as unused from static text search alone.
6. Check configuration, dynamic loading, scheduled workflows, notebooks,
   external consumers, physical dependencies, and human processes when
   relevant.
7. Preserve raw data, provenance, accepted decisions, audit evidence,
   published deliverables, and regulated records unless exact-item confirmation
   is given and applicable policy permits the action.
8. Never reveal secrets while reporting curation findings.

## Gated actions

The following require the exact-item confirmation gate even when
`mode: update-and-prune` is selected:

- moving or renaming
- archiving or quarantining
- disabling or making unavailable
- consolidating, merging, or replacing
- deleting
- permanently overwriting irreplaceable or authoritative material

Treat a consolidation as two phases: create and validate the proposed combined
artifact without removing sources, then gate every source disposition. A
selected mode, requested `disposition`, prior broad approval, or silence is
never confirmation.

## Live and physical state safety

Reversibility alone does not make a live-state change safe. Before changing
production or operational state, equipment or instrument settings, a physical
environment, or directly enacting a procedure change in live operations,
require all of:

1. The exact target, expected side effects, affected people or systems, and
   hazard boundaries are stated.
2. The change is isolated, bounded, or scheduled in an approved safe window.
3. The responsible owner explicitly authorizes the exact change.
4. Monitoring and stopping conditions are active.
5. A tested recovery method and an approved fail-safe or operational stopping
   state are available.
6. Required permissions, safety controls, and applicable policy are satisfied.

If any condition is missing, remain in report mode and propose the controlled
change. Never perform an illegal, uncontrolled, irrecoverable, or foreseeably
harmful live or physical action.

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
2. Build the relevant dependency graph.
3. Identify generated and manually maintained artifacts.
4. Inventory only the requested scope and necessary dependencies.
5. Detect staleness, contradiction, duplication, broken references, and
   orphaning.
6. Determine which artifacts can be reproduced.
7. Build an ordered update plan with success criteria and recovery for each
   change.
8. Apply approved non-destructive updates only when the mode permits.
9. Validate regenerated or updated artifacts.
10. Prepare an exact disposition ledger.
11. Request confirmation before every gated action.
12. Report completed actions and unresolved items.

## Update validation and failure handling

Before an update, capture or identify the prior state, required verification,
dependent changes, and a safe recovery method. If success criteria are absent
and cannot be derived from authoritative evidence, ask before modifying.

If validation fails:

1. Stop dependent updates and all gated actions.
2. Use only a pre-approved, verified-safe rollback or recovery.
3. For artifact-only changes when safe recovery is unavailable, preserve the
   evidence and current artifact state, identify every partial change, and
   request direction.
4. For a live or physical change, enter the pre-approved fail-safe or
   operational stop, preserve evidence, and escalate; never leave an
   unvalidated state active.
5. Never report the curation as complete or continue from a failed intermediate
   state without explicit acceptance and a revised plan.

Build the dependency graph from the project rather than imposing a fixed
software-oriented order. Consider any relevant:

- objectives, accepted decisions, contracts, policies, and requirements
- source data, materials, configurations, instrument settings, and
  environmental conditions
- implementation, procedures, methods, models, notebooks, and active
  operational state
- tests, reviews, calibration, validation, and compliance evidence
- generated outputs, tables, models, figures, physical products, and reports
- documentation, screenshots, handoff material, and external or human
  consumers

For each candidate, determine inbound and outbound dependencies, authority,
reproducibility, current use, recovery method, and the consequence of changing
identity or availability.

When a reproducible generator exists, inspect the source or generator first.
Modify it only when it is explicitly included in the approved update scope. If
it is out of scope, report the generated artifact as blocked and request scope
expansion; do not silently edit upstream code, data, configuration, procedures,
or equipment settings. Do not manually patch generated output unless the user
explicitly accepts a documented, non-reproducible exception.

## Exact-item confirmation gate

Before any gated action, assign a stable ledger identifier such as
`CURATE-LEDGER-1` and list every candidate with:

- exact item path or identifier
- proposed action
- reason
- evidence
- dependency risk
- recovery method

Then state:

> No gated action has been performed. To continue, explicitly invoke `/curate`,
> reference this ledger identifier, and confirm the exact listed items and
> actions; otherwise modify the list or cancel.

Confirmation applies only to the exact listed items and actions. A changed
action or newly discovered candidate requires a new ledger. After presenting
the ledger, stop and wait.

On a later turn, act only when the user explicitly re-invokes `/curate`,
references the ledger identifier, and confirms its exact items and actions.
Before acting, revalidate current state and dependencies. If relevant state,
evidence, or dependencies changed, invalidate the ledger and present a revised
one. A bare "confirm", prior broad request, selected mode, or silence is never
confirmation.

## Role behavior

### Background

- Curate only artifacts needed for the primary deliverable.
- Avoid a project-wide cleanup report.
- Surface blocked updates, contradictions, and gated actions that need
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

Do not redesign under the label of cleanup, change artifact identity or
availability based only on age or naming, remove decision-useful failed
experiments without exact-item confirmation, rewrite project history to appear
cleaner, automatically resolve objective drift, or treat unfamiliar files as
unnecessary.
