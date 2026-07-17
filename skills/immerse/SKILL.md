---
name: immerse
description: "Builds a verified mental model of a project or selected segment at a requested abstraction level."
disable-model-invocation: true
---

# Immerse

Build the project context needed to understand or complete the user's request.
This is a context-acquisition workflow, not a flaw audit, cleanup operation,
objective-drift assessment, or decision comparison.

## Invocation contract

Run only after the user explicitly selects `/immerse`. Never invoke another
VibeLib skill on the user's behalf.

Recognize these optional keyed parameters in the user's prompt:

- `segment`: area to understand; default `entire project`
- `level`: `top`, `high`, `mid`, `low`, or `bottom`; default `top`
- `role`: `background`, `foreground`, or `standalone`
- `focus`, `include`, `exclude`, `constraints`, `questions`, `output`

Treat non-parameter text as the primary request. If there is a separate primary
request, default `role` to `background`; otherwise default it to `standalone`.
An explicit role wins. Unknown keyed fields are additional context, not new
workflows.

When other skills are explicitly selected in the same prompt, share evidence
and produce one integrated deliverable in the user's requested format. Do not
emit one report per skill unless requested.

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
9. Build an evidence map.
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

- Make the requested project model visible and central.
- Emphasize the selected segment and level.
- Integrate the model into the primary deliverable rather than adding an
  automatic separate report.

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
9. Contradictions and unknowns
10. Useful areas for deeper immersion

## Evidence rules

- Label consequential claims as **Observed**, **Inferred**, or **Unknown**.
- Prefer active authoritative artifacts and cite concrete project evidence.
- Documentation is not proof of implementation.
- Existing code is not proof that a workflow runs.
- Do not fabricate project history, intent, or rationale.
- Report conflicting evidence and unsupported depth explicitly.
- Distinguish what the project does from what it should do.

## Boundaries

Do not perform an adversarial flaw-first audit, reconcile alternatives, curate
artifacts, classify objective drift, or make changes unless the user explicitly
selects or requests that separate work.
