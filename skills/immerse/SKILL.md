---
name: immerse
description: "Builds a verified mental model of a project or selected segment. Invoke explicitly when project context or orientation is the requested workflow."
disable-model-invocation: true
---

# Immerse

Build the project context needed to understand or complete the user's request.
This is a context-acquisition workflow, not a flaw audit, cleanup operation,
objective-drift assessment, or decision comparison.

## Operating stance

Highlight what matters and lay out the options worth considering; in the
foreground, converse with the user about them rather than deciding alone. Do
not change the project on your own initiative.

## Invocation contract

Run only after the user explicitly selects `/immerse`. Mentioning, quoting,
attaching, or reading this skill is not invocation. Never invoke another
VibeLib skill on the user's behalf.

Recognize these optional keyed parameters in the user's prompt:

- `segment`: area to understand; default `entire project`
- `level`: `top`, `high`, `mid`, `low`, or `bottom`; default `top`
- `role`: `background`, `foreground`, or `standalone`
- `focus`, `include`, `exclude`, `constraints`, `questions`, `output`

In a single-skill prompt, unscoped recognized parameters belong to Immerse and
unknown keyed fields are additional context. A native Immerse request asks for
project understanding and defaults to `standalone`. Default to `background`
only when the user requests a distinct primary deliverable, such as a guide,
plan, patch, or decision memo, that immersion should support. If
`role: background` is explicit but no separate deliverable exists, ask what the
immersion should support before proceeding.

In a composed prompt, bind parameters under an `Immerse:` heading to this
skill. Treat every unscoped parameter as ambiguous. A parameter may apply to
multiple skills only when the user places it under an explicit `Shared:`
heading and every named skill recognizes the same meaning; otherwise ask for
namespaced parameters. Treat `Request:` or the final non-parameter instruction
as the global deliverable.

Apply precedence in this order: safety constraints, explicit Immerse
parameters, explicit global request and format, then defaults. A global output
format controls the final response; Immerse's `output` controls only its
contribution. Share evidence with other explicitly selected skills. If there
is a global deliverable, produce one integrated response. If several skills
are `standalone` without a global deliverable, use one response with a clearly
labeled section per skill in invocation order and deduplicate shared evidence.

## Parameter semantics

- `focus`: questions, mechanisms, or junctions to prioritize
- `include`: artifacts or areas that must be considered
- `exclude`: areas not to inspect; disclose when an excluded dependency limits
  confidence
- `constraints`: limits on tools, time, depth, access, or acceptable side
  effects
- `questions`: questions the mental model must answer or mark unresolved
- `output`: structure or detail for Immerse's contribution, subordinate to an
  explicit global deliverable

Do not claim complete coverage merely because `segment: entire project` was
requested. Scale depth to available evidence and disclose material omissions.

## Level model

- `top`: objective, intended users or population, domain logic, primary
  deliverables, non-goals, constraints, end-to-end flow, critical junctions,
  current state, and consequential unknowns
- `high`: major components or workstreams, architecture or methodology,
  ownership boundaries, interfaces, dependencies, lifecycle, and information
  movement
- `mid`: modules, pipelines, notebooks, schemas, algorithms, protocols,
  transformations, state transitions, validation gates, control flow, inputs,
  outputs, assumptions, and invariants
- `low`: functions, classes, queries, cells, configurations, methods,
  procedures, exact inputs and outputs, execution order, side effects, edge
  cases, local dependencies, and adjacent change impact
- `bottom`: literal statements, expressions, operators, formulas, fields,
  commands, syntax, types, scope, lifecycles, evaluation order, null or missing
  behavior, units, indexing, casting, boundaries, and exact downstream impact

For non-code projects, use the equivalent meaningful unit at the selected
level, such as a protocol step, formula, policy clause, instrument setting, or
operational action.

## Critical junctions

A critical junction is where an important decision occurs, data or control
branches, an assumption enters, responsibility changes, information is
materially transformed, validation accepts or rejects work, failures can
propagate, a user-facing result is created, or a dependency constrains later
choices.

For each relevant junction, establish:

- input
- decision or transformation
- output
- governing assumption or mechanism
- why it matters

## Workflow

1. Establish the project or segment boundary.
2. Find authoritative objective and decision sources.
3. Distinguish active, historical, generated, and unknown artifacts.
4. Reconstruct intent, terminology, constraints, and non-goals.
5. Trace the requested scope at the selected level.
6. Identify relevant critical junctions.
7. Classify major areas as implemented, partial, planned, superseded, blocked,
   ambiguous, or unknown.
8. Detect contradictions among documentation, implementation, data, outputs,
   and decisions.
9. Build an evidence and coverage map.
10. Contribute only context relevant to the primary request unless standalone.

Inspect adjacent areas only when needed for dependencies, evidence, downstream
impact, or safety. Do not modify the project merely to complete the mental
model; changes require a separate explicit request.

## Role behavior

### Background

- Build the necessary model internally.
- Surface only facts, assumptions, terminology, dependencies, junctions, and
  unknowns that materially change the primary deliverable.
- Do not output a general project overview.

### Foreground

- Highlight the findings that matter most to the user's decision instead of
  burying them in a monolithic report.
- Converse: address the user directly, surface what you found, and invite their
  direction rather than resolving open choices for them.
- Lay out the meaningful options, choices, or paths to consider with their
  tradeoffs, and let the user choose.
- Emphasize the selected segment and level, and offer paths for going deeper:
  areas to explore next, open questions to resolve, and assumptions worth
  confirming.
- Integrate the model into the requested deliverable without changing the
  project.

### Standalone

Use this structure, omitting empty sections:

1. Mental model
2. Objective and boundaries
3. Project or segment map
4. End-to-end flow
5. Critical junctions
6. Current implementation state
7. Key decisions and assumptions
8. Evidence map
9. Inspected, inferred, and uninspected coverage
10. Contradictions and unknowns
11. Useful areas for deeper immersion

## Evidence rules

- Label consequential claims as **Observed**, **Inferred**, or **Unknown**.
- Prefer active authoritative artifacts and cite concrete project evidence.
- Documentation is not proof of implementation.
- Existing code is not proof that a workflow runs.
- Do not fabricate project history, intent, or rationale.
- Report conflicting evidence and unsupported depth explicitly.
- Distinguish what the project does from what it should do.
- Treat the mental model as verified only to the extent that material
  **Observed** claims trace to inspected evidence.
- For each material evidence-map entry, record the claim, status, source or
  artifact, covered scope, and limitation.
- List consequential areas that were not inspected and why.

## Boundaries

Do not perform an adversarial flaw-first audit, reconcile alternatives, curate
artifacts, classify objective drift, or make changes unless the user explicitly
selects or requests that separate work.
