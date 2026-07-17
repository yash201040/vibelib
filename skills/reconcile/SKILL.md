---
name: reconcile
description: "Compares alternatives, exposes the real disagreement, and supports a defensible choice. Invoke explicitly when a decision comparison is requested."
disable-model-invocation: true
---

# Reconcile

Compare opposing, alternate, or incompatible human, AI, stakeholder,
methodological, or implementation proposals. Expose the real disagreement
rather than flattening it into a vague compromise.

## Invocation contract

Run only after the user explicitly selects `/reconcile`. Mentioning, quoting,
attaching, or reading this skill is not invocation. Never invoke another
VibeLib skill on the user's behalf.

Recognize these optional keyed parameters:

- `scope`
- `role`: `background`, `foreground`, or `standalone`
- `option A`, `option B`, and further named `option` entries
- `criteria`, with optional priorities
- `constraints`, `priority`, `horizon`, `evidence-standard`, `output`

Options and criteria may also be written as ordinary headings or lists. In a
single-skill prompt, unscoped recognized parameters belong to Reconcile and
unknown keyed fields are additional context. A native Reconcile request asks
for a comparison or decision and defaults to `standalone`. Default to
`background` only when the user requests a distinct primary deliverable, such
as a broader plan or memo, that the comparison should support. If
`role: background` is explicit but no separate deliverable exists, ask what the
comparison should support.

In a composed prompt, bind parameters under a `Reconcile:` heading to this
skill. Treat every unscoped parameter as ambiguous. A parameter may apply to
multiple skills only when the user places it under an explicit `Shared:`
heading and every named skill recognizes the same meaning; otherwise ask for
namespaced parameters. Treat `Request:` or the final non-parameter instruction
as the global deliverable.

Apply precedence in this order: safety and hard constraints, explicit
Reconcile parameters, explicit global request and format, then defaults. A
global output format controls the final response; Reconcile's `output` controls
only its contribution. Share evidence with other explicitly selected skills.
If there is a global deliverable, produce one integrated response. If several
skills are `standalone` without a global deliverable, use one response with a
clearly labeled section per skill in invocation order.

## Parameter semantics

- `scope`: decision boundary and affected system, population, process, or
  artifact
- `options`: two or more named alternatives; include the status quo when viable
- `criteria`: decision factors, optionally ordered
- `constraints`: hard boundaries that make an option infeasible, not merely
  undesirable
- `priority`: an explicit ordering, tie-breaker, or stakeholder value; never
  convert it into invented numerical weights
- `horizon`: time period over which consequences must be evaluated; if omitted,
  cover both immediate effects and the relevant lifecycle and state the assumed
  horizon
- `output`: structure or detail for Reconcile's contribution, subordinate to an
  explicit global deliverable

`evidence-standard` accepts:

- `exploratory`: compare scenarios and identify information needed; do not make
  a categorical recommendation from unresolved assumptions
- `supported` (default): ground the recommendation in concrete evidence and
  explicit assumptions
- `strict`: require authoritative evidence for decisive facts and explicit
  stakeholder priorities; otherwise return a conditional recommendation or
  decision process

## Core rules

1. Steelman every viable option.
2. Separate facts, assumptions, forecasts, constraints, and preferences.
3. Do not hide subjective judgment inside arbitrary numerical scoring.
4. Determine whether the alternatives are truly exclusive.
5. Consider the status quo, hybrid, phased, conditional, and reversible
   approaches when they are genuinely viable.
6. Prefer bounded experiments when uncertainty is testable.
7. Do not implement while the decision remains unresolved.

Classify the actual disagreement as one or more of:

- evidence conflict
- assumption conflict
- objective conflict
- constraint conflict
- risk-tolerance conflict
- time-horizon conflict
- terminology conflict

Resolve terminology and factual disagreements before comparing preferences.

## Decision sufficiency gate

Before selecting an option, establish:

1. At least two distinct alternatives, or one proposal and a meaningful status
   quo.
2. The objective and hard constraints.
3. Stakeholder priorities or a tie-breaker sufficient to resolve material
   tradeoffs.
4. Evidence that meets the requested standard for decisive claims.

If missing information or priorities could reverse the result, ask a focused
clarifying question. If clarification is unavailable, provide a conditional
recommendation, bounded experiment, or decision process instead of selecting
an option categorically. Never treat model-chosen preferences as user-approved
priorities. A categorical recommendation is still permitted when one option
dominates across all plausible unresolved priorities; explain why.

## Workflow

1. Define the exact decision.
2. Establish scope, objective, decision owner when known, and hard constraints.
3. Normalize all alternatives into comparable descriptions.
4. Identify prerequisites and hidden dependencies.
5. Describe best, likely, and credible failure outcomes.
6. Identify who benefits and who bears cost or risk.
7. Classify the real disagreement.
8. Evaluate explicit, decision-relevant criteria.
9. Search for dominance, hybrid solutions, sequencing, and reversible tests.
10. Apply the decision sufficiency gate, then recommend a decision, conditional
    decision, experiment, or decision process.
11. State what evidence would change the recommendation.

Use only relevant criteria, such as objective fitness, correctness, scientific
validity, stakeholder value, safety, security, privacy, ethics, compliance,
reliability, reproducibility, effort, time, operating cost, scalability,
reversibility, compatibility, migration burden, team capability, and cognitive
load.

Do not manufacture precise scores. State which explicit priorities or
conditional value judgments drive the result.

## Role behavior

### Background

- Resolve only alternatives that affect the primary request.
- Supply the selected rationale without a full decision report.
- Surface unresolved value judgments when they materially change the result.

### Foreground

- Make the tradeoff analysis and decisive criteria visible.
- Show accepted costs and unresolved uncertainty.
- Integrate the analysis into the requested output.

### Standalone

Use this structure:

1. Decision statement
2. Decision context
3. Objectives and constraints
4. Alternatives
5. Real disagreement
6. Evidence and tradeoff comparison
7. Recommendation
8. Accepted tradeoffs
9. Confidence
10. What would change the decision
11. Next action

When the user requests a decision record, use:

```markdown
# Decision: <title>

- Status: Proposed | Accepted | Deferred | Superseded
- Scope:
- Decision owner:

## Context
## Objectives and constraints
## Alternatives considered
## Evidence and tradeoffs
## Decision
## Consequences and accepted risks
## Validation trigger
## Conditions that reopen the decision
```

Never mark a decision `Accepted` without explicit human acceptance or
authoritative evidence that it was accepted.

## Evidence rules

- Cite concrete project evidence when available.
- Label consequential claims as **Observed**, **Inferred**, or **Unknown**.
- Preserve conflicting evidence and uncertainty.
- State assumptions and forecasts separately from facts.
- Explain who bears each material downside.

## Boundaries

Do not average incompatible approaches into a weak compromise, treat
popularity as evidence, execute the selected option without authorization, or
produce unrelated project context.
