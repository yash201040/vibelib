---
name: driftcheck
description: "Compares an authoritative baseline with the current state and classifies material divergence. Invoke explicitly when alignment or objective drift is in question."
disable-model-invocation: true
---

# Driftcheck

Identify, classify, and rank differences between the active objective baseline
and current implementation, documentation, data, methods, evaluation,
operations, UX, or deliverables. Never assume every divergence should be
reversed; the current state may be right while the baseline is stale.

## Operating stance

Highlight what matters and lay out the options worth considering; in the
foreground, converse with the user about them rather than deciding alone. Do
not change the project on your own initiative.

## Invocation contract

Run only after the user explicitly selects `/driftcheck`. Mentioning, quoting,
attaching, or reading this skill is not invocation. Never invoke another
VibeLib skill on the user's behalf.

Recognize these optional keyed parameters:

- `baseline`: expected state or authoritative source
- `current`: current state or evidence source
- `scope`, `dimensions`, `timepoint`, `rank-by`
- `role`: `background`, `foreground`, or `standalone`
- `include`, `exclude`, `output`

In a single-skill prompt, unscoped recognized parameters belong to Driftcheck
and unknown keyed fields are additional context. A native Driftcheck request
asks for alignment analysis and defaults to `standalone`. Default to
`background` only when the user requests a distinct primary deliverable, such
as a release assessment or remediation plan, that drift analysis should
support. If `role: background` is explicit but no separate deliverable exists,
ask what the analysis should support.

In a composed prompt, bind parameters under a `Driftcheck:` heading to this
skill. Treat every unscoped parameter as ambiguous. A parameter may apply to
multiple skills only when the user places it under an explicit `Shared:`
heading and every named skill recognizes the same meaning; otherwise ask for
namespaced parameters. Treat `Request:` or the final non-parameter instruction
as the global deliverable.

Apply precedence in this order: safety constraints, baseline authority,
explicit Driftcheck parameters, explicit global request and format, then
defaults. A global output format controls the final response; Driftcheck's
`output` controls only its contribution. Share evidence with other explicitly
selected skills. If there is a global deliverable, produce one integrated
response. If several skills are `standalone` without a global deliverable, use
one response with a clearly labeled section per skill in invocation order.
Never activate `/reconcile` merely because a disposition requires a decision.

## Parameter semantics

- `baseline`: expected state and its authority source
- `current`: current state and its evidence source
- `scope`: boundary of the comparison
- `dimensions`: one or more of `implementation-or-behavior`, `documentation`,
  `data-or-method`, `scope`, `operation`, or `deliverable`; omit to consider
  every relevant dimension
- `timepoint`: baseline and current dates, revisions, versions, or events; if
  omitted, use the latest supported active states and state that assumption
- `rank-by`: ordered ranking criteria chosen from `severity`,
  `decision-impact`, `urgency`, `reversibility`, or `confidence`; default
  `severity`, then `decision-impact`, then `confidence`
- `include` and `exclude`: required and prohibited evidence areas; disclose
  when exclusions prevent assessment
- `output`: structure or detail for Driftcheck's contribution, subordinate to
  an explicit global deliverable

## Orthogonal finding model

Do not force a difference into one competing classification. Record these
fields independently:

1. `Baseline status`: `Authoritative`, `Superseded`, `Disputed`, or `Unknown`.
2. `Relationship`: `Aligned`, `Divergent`, or `Not assessable`.
3. `Dimensions`: one or more requested dimensions.
4. `Authorization`: `Approved`, `Unapproved`, `Unknown`, or `Not applicable`.
5. `Work state`: `Complete`, `Incomplete`, `Planned`, `Not applicable`, or
   `Unknown`.
6. `Value assessment`: `Harmful`, `Potentially beneficial`, `Neutral`, or
   `Unknown`.
7. `Defect relationship`: `None`, `Independent defect`,
   `Divergence-caused defect`, or `Unknown`.
8. `Disposition`: the recommended next treatment.

Derive summary labels only after recording those fields:

- `True drift`: an authoritative active baseline, a divergent relationship,
  and unapproved authorization
- `Approved evolution`: a divergent relationship with authoritative approval
- `Potentially beneficial divergence`: divergence that may improve outcomes
  but lacks completed evaluation or acceptance
- `Stale baseline`: evidence indicates the expected state itself should be
  reconsidered or has been superseded

`Incomplete work` is a work state, not a divergence type.
`implementation-or-behavior`, `documentation`, `data-or-method`, `scope`,
`operation`, and `deliverable` are the canonical dimension names. A defect may
be independent of drift.

When no authoritative expected state can be established, set
`Relationship: Not assessable`, explain the missing authority, and do not
report true drift.

## Ranking fields

Every finding records `Severity`, `Decision impact`, and `Confidence`. Also
record `Urgency` or `Reversibility` when selected by `rank-by`.

- `Decision impact`: `High` changes a consequential decision or outcome;
  `Medium` changes a bounded decision or requires a workaround; `Low` has
  limited decision effect; also allow `None` and `Unknown`
- `Urgency`: `Immediate`, `Time-bound` with the relevant deadline, `Monitor`,
  `None`, or `Unknown`
- `Reversibility`: `Hard`, `Moderate`, `Easy`, `Not applicable`, or `Unknown`
- `Confidence`: `High` for direct or independently corroborated evidence,
  `Medium` for concrete evidence with a material gap, or `Low` for indirect or
  assumption-dependent evidence

Rank lexicographically in the exact `rank-by` order. Do not collapse unlike
criteria into an invented numerical score.

## Evidence required per finding

Establish:

- expected state
- baseline evidence
- baseline authority
- baseline status
- observed current state
- current-state evidence
- relationship and dimensions
- authorization, work state, value assessment, and defect relationship
- recommended disposition
- severity, decision impact, confidence, and any other selected ranking fields

## Workflow

1. Reconstruct the active objective baseline.
2. Identify accepted decisions that supersede older artifacts.
3. Extract users, outcomes, success criteria, constraints, non-goals, scope,
   and methods.
4. Model the active current state.
5. Build traceability between objectives and implementation or evidence.
6. Detect meaningful differences.
7. Record every orthogonal finding field.
8. Record the required ranking fields and apply `rank-by`.
9. Derive supported summary labels and materiality.
10. Recommend a disposition without assuming realignment.
11. Contribute only differences relevant to the primary request unless
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
- `None`: no material difference
- `Unknown`: impact cannot be established from available evidence

## Avoid false positives

Do not derive `True drift` when:

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

- Highlight the findings that matter most to the user's decision instead of
  burying them in a monolithic report.
- Converse: address the user directly, surface what you found, and invite their
  direction rather than resolving open choices for them.
- Lay out the meaningful options, choices, or paths to consider with their
  tradeoffs, and let the user choose.
- Make material divergence, authority, and the candidate dispositions visible as
  options, and let the user decide the treatment.
- Integrate them into the requested deliverable without changing the project.

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

- baseline item, authority, and baseline status
- current evidence and relationship
- dimensions and difference
- authorization, work state, value assessment, and defect relationship
- severity, decision impact, confidence, and selected ranking fields
- disposition or decision needed

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
