---
name: xray
description: "Performs an adversarial, evidence-based review of a project or selected segment and ranks material flaws and risks."
disable-model-invocation: true
---

# Xray

Investigate flaws, discrepancies, invalid assumptions, failure modes, and
material risks. This is an adversarial review workflow, not general context
building.

## Invocation contract

Run only after the user explicitly selects `/xray`. Never invoke another
VibeLib skill on the user's behalf.

Recognize these optional keyed parameters:

- `segment`: review scope; default `entire project`
- `level`: `top`, `high`, `mid`, `low`, or `bottom`; default `top`
- `role`: `background`, `foreground`, or `standalone`
- `focus`, `include`, `exclude`, `constraints`, `threat-model`
- `evidence-standard`, `readiness-target`, `output`

Treat non-parameter text as the primary request. If there is a separate primary
request, default `role` to `background`; otherwise default it to `standalone`.
An explicit role wins.

When other skills are explicitly selected in the same prompt, share evidence,
avoid duplicate findings, and produce one integrated deliverable in the
requested format.

## Level model

- `top`: problem fitness, objective and outcome validity, target users or
  population, product or research logic, success criteria, proxy metrics,
  primary functionality, end-to-end failure paths, governance, readiness, and
  claims versus evidence
- `high`: architecture, major workstreams, component and trust boundaries,
  methodology, interfaces, dependencies, systemic single points of failure,
  and cross-project reproducibility, privacy, security, and maintainability
- `mid`: modules, notebooks, pipelines, schemas, protocols, algorithms,
  transformations, state transitions, validation gates, leakage, aggregation,
  evaluation logic, retries, idempotency, failure handling, and unenforced
  invariants
- `low`: functions, classes, queries, cells, configurations, methods,
  procedures, local correctness, types, side effects, resource usage, error
  propagation, unsafe defaults, edge cases, and test adequacy
- `bottom`: literal expressions, statements, formulas, fields, commands,
  operator precedence, types, scopes, casting, evaluation order, null or
  missing behavior, indexing, units, precision, boundaries, mutation, and
  exact downstream effects

For non-code projects, use the equivalent evidentiary or operational unit.

## Review dimensions

Consider only dimensions relevant to the requested scope:

- objective and requirement correctness
- logical correctness
- data quality and provenance
- population, selection, temporal, or evaluation leakage
- scientific, statistical, and measurement validity
- reproducibility
- reliability and recovery
- security and privacy
- safety, ethics, and compliance
- performance and scalability
- maintainability and change risk
- UX and operator error
- documentation and claim accuracy
- physical, hardware, calibration, and tolerance risk

## Finding model

Use one status:

- `Confirmed`: directly supported by concrete evidence and a plausible failure
  path
- `Reproduced`: safely triggered or validated
- `Strongly indicated`: multiple concrete signals support it, but reproduction
  is incomplete
- `Hypothesis`: plausible and decision-relevant, but unverified

Assign severity independently from confidence:

- `Critical`: credible path to invalidating the core outcome, severe harm,
  hard-boundary violation, unrecoverable corruption, major security, privacy,
  or safety failure, or catastrophic operational failure
- `Major`: material likelihood of wrong decisions, failed delivery, broad
  unreliability, significant harm, or invalid core functionality without a
  reliable workaround
- `Significant`: meaningful but bounded risk, degradation, discrepancy, or
  workaround-dependent issue
- `Minor`: localized issue with limited consequence

Do not inflate style preferences into material findings. Consolidate multiple
symptoms under their common root cause.

## Workflow

1. Establish intended use and unacceptable outcomes.
2. Map critical inputs, transformations, decisions, outputs, and consumers.
3. Identify trust boundaries and irreversible operations.
4. Generate plausible, scope-relevant risk hypotheses.
5. Investigate each hypothesis using available evidence.
6. Attempt safe reproduction or validation when appropriate.
7. Consolidate symptoms under root causes.
8. Rank findings by consequence, likelihood, detectability, blast radius,
   reversibility, and confidence.
9. Offer fix choices for consequential findings.
10. Contribute only findings relevant to the primary request unless standalone.

Do not run destructive, unsafe, production-impacting, or privacy-invasive tests
without explicit authorization. State what was not inspected.

## Fix choices

When useful, distinguish:

- `Containment`: fastest action that reduces immediate exposure
- `Robust fix`: preferred correction within the current design
- `Redesign`: structural alternative for a systemic problem

For each viable choice, state the change, expected risk reduction, tradeoffs,
relative effort, migration impact, verification, and rollback. Do not implement
a fix unless the user separately requests implementation.

## Role behavior

### Background

- Investigate silently.
- Surface only risks that alter the primary answer or deliverable.
- Do not dump a complete audit or unrelated style findings.

### Foreground

- Make key findings, failure paths, and evidence visible.
- Prioritize the user's decision and integrate findings into the requested
  deliverable.

### Standalone

Use this structure:

1. Readiness verdict
2. Audit scope and level
3. Inspected and uninspected areas
4. Critical and Major findings
5. Risk summary
6. Detailed findings
7. Systemic root causes
8. Fix sequence
9. Residual risks
10. Limitations

For each detailed finding use:

```markdown
## XR-<number>: <title>

- Severity:
- Confidence:
- Status:
- Affected scope:

### Evidence
### Trigger and failure path
### Impact
### Root cause
### Validation needed
### Fix choices
### Recommended action
### Verification and rollback
```

## Evidence rules

- Cite concrete project evidence for consequential claims.
- Label unverified catastrophic scenarios as hypotheses.
- Report conflicting evidence and preserve uncertainty.
- Absence of findings is not proof of correctness.
- Distinguish current behavior from recommended behavior.

## Boundaries

Do not substitute general project orientation, objective-drift classification,
decision reconciliation, artifact cleanup, or unrequested implementation for
the requested review.
