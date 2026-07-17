---
name: reconcile
description: "Compares incompatible proposals or alternatives, exposes the real disagreement, and supports a defensible choice."
disable-model-invocation: true
---

# Reconcile

Compare opposing, alternate, or incompatible human, AI, stakeholder,
methodological, or implementation proposals. Expose the real disagreement
rather than flattening it into a vague compromise.

## Invocation contract

Run only after the user explicitly selects `/reconcile`. Never invoke another
VibeLib skill on the user's behalf.

Recognize these optional keyed parameters:

- `scope`
- `role`: `background`, `foreground`, or `standalone`
- `option A`, `option B`, and further named `option` entries
- `criteria`, with optional priorities
- `constraints`, `priority`, `horizon`, `evidence-standard`, `output`

Options and criteria may also be written as ordinary headings or lists. Treat
the remaining text as the primary request. If there is a separate primary
request, default `role` to `background`; otherwise default it to `standalone`.
An explicit role wins.

When other skills are explicitly selected in the same prompt, share evidence
and produce one integrated deliverable rather than separate workflow reports.

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
10. Recommend a decision or a decision process.
11. State what evidence would change the recommendation.

Use only relevant criteria, such as objective fitness, correctness, scientific
validity, stakeholder value, safety, security, privacy, ethics, compliance,
reliability, reproducibility, effort, time, operating cost, scalability,
reversibility, compatibility, migration burden, team capability, and cognitive
load.

Do not manufacture precise scores. If criteria priorities are missing, state
which value judgments drive the recommendation rather than silently inventing
weights.

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
