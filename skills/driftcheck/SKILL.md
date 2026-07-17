---
name: driftcheck
description: "Compares an authoritative objective baseline with the current project state and classifies material divergence."
disable-model-invocation: true
---

# Driftcheck

Identify, classify, and rank differences between the active objective baseline
and current implementation, documentation, data, methods, evaluation,
operations, UX, or deliverables. Never assume every divergence should be
reversed; the current state may be right while the baseline is stale.

## Invocation contract

Run only after the user explicitly selects `/driftcheck`. Never invoke another
VibeLib skill on the user's behalf.

Recognize these optional keyed parameters:

- `baseline`: expected state or authoritative source
- `current`: current state or evidence source
- `scope`, `dimensions`, `timepoint`, `rank-by`
- `role`: `background`, `foreground`, or `standalone`
- `include`, `exclude`, `output`

Treat non-parameter text as the primary request. If there is a separate primary
request, default `role` to `background`; otherwise default it to `standalone`.
An explicit role wins.

When other skills are explicitly selected in the same prompt, share evidence
and produce one integrated deliverable. Never activate `/reconcile` merely
because a drift disposition requires a decision.

## Classifications

Assign the narrowest supported classification:

- `True drift`: current state conflicts with an authoritative objective,
  requirement, or constraint without accepted authorization
- `Approved evolution`: the difference is intentional and authorized; the
  active baseline should represent it
- `Potentially beneficial divergence`: the difference may improve the project
  but has not been formally evaluated or accepted
- `Stale objective or baseline`: evidence indicates the expected state should
  be reconsidered or updated
- `Incomplete work`: expected implementation is planned but unfinished
- `Documentation drift`: documentation differs from authoritative behavior
- `Data or method drift`: sources, populations, schemas, transformations,
  protocols, assumptions, models, or evaluations changed
- `Scope drift`: the project expanded, narrowed, or redirected beyond accepted
  scope
- `Operational drift`: actual execution differs from the validated or
  documented procedure
- `Defect`: an internal flaw that does not necessarily represent objective
  drift
- `Unknown`: evidence cannot establish the baseline or current state

Do not report drift when no authoritative expected state exists.

## Evidence required per finding

Establish:

- expected state
- baseline evidence
- baseline authority
- observed current state
- current-state evidence
- classification
- confidence

## Workflow

1. Reconstruct the active objective baseline.
2. Identify accepted decisions that supersede older artifacts.
3. Extract users, outcomes, success criteria, constraints, non-goals, scope,
   and methods.
4. Model the active current state.
5. Build traceability between objectives and implementation or evidence.
6. Detect meaningful differences.
7. Classify each difference.
8. Determine materiality and decision impact.
9. Recommend a disposition without assuming realignment.
10. Contribute only differences relevant to the primary request unless
    standalone.

Recommend one of these dispositions when supported:

- realign the current implementation
- update the objective or baseline
- formally accept the exception
- retain and validate a beneficial divergence
- complete planned work
- update documentation
- update traceability
- run an experiment
- explicitly invoke `/reconcile` in a later request
- investigate further

## Severity

Report severity separately from confidence:

- `Critical`: defeats the core objective, violates a hard boundary, or makes
  the primary outcome invalid or unsafe
- `Major`: materially reduces objective achievement or creates a high
  likelihood of failed delivery or wrong decisions
- `Significant`: meaningful divergence with bounded impact or a practical
  workaround
- `Minor`: localized inconsistency with limited impact

## Avoid false positives

Do not classify true drift when:

- an accepted decision superseded the earlier requirement
- implementation adds detail without changing the objective
- work is incomplete and represented accurately
- a historical artifact is retained for provenance
- the expected state lacks authority
- the issue is an internal defect rather than objective divergence

## Role behavior

### Background

- Surface only drift that affects the primary request.
- Expose baseline uncertainty when it changes the answer.
- Do not produce a full traceability matrix unless requested.

### Foreground

- Make material divergence, authority, and disposition choices visible.
- Integrate them into the requested output.

### Standalone

Use this structure:

1. Overall alignment assessment
2. Active baseline and authority
3. Top decision-relevant differences
4. Traceability matrix
5. Detailed drift register
6. Potentially beneficial divergences
7. Stale or disputed objectives
8. Recommended dispositions
9. Unknowns and evidence gaps

For each traceability entry include:

- baseline item and authority
- current evidence
- classification and difference
- decision needed

## Evidence rules

- Cite concrete baseline and current-state evidence.
- Label consequential claims as **Observed**, **Inferred**, or **Unknown**.
- Report conflicting authority and uncertainty explicitly.
- Distinguish the oldest baseline from the active baseline.
- Distinguish current behavior from recommended disposition.

## Boundaries

Do not enforce the oldest objective, assume alignment is always correct, repair
findings without authorization, treat every stale file as drift, or perform
broad flaw discovery unrelated to objectives.
