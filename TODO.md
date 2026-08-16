> NOTE THAT THIS DOCUMENT IS DEPRECATED!

# Documentation TODOs

This is the temporary backlog for supporting documentation. Complete an item when the team needs the process it governs; do not create empty documents in anticipation of future work. Prefer short sections in an existing document over new files.

## Before routine requirements and risk work

- [ ] **Define the repository layout and local commands** in `CONTRIBUTING.md`: where requirements, risks, evidence, configuration records, and generated output belong; how to install the pinned tools; and how to validate and preview changes.
- [ ] **Define the contribution workflow** in `CONTRIBUTING.md`: branch, commit, and pull-request conventions; required reviewers; PR contents; baseline changes; and the expedited path, if any, for time-critical corrections.
- [ ] **Create a concise authoring reference** in `docs/authoring.md`: established requirement and risk fields, allowed values, field applicability, ID allocation, relation usage, and one good example of each record type. Include the requirement, rationale, risk, cause, and consequence sentence templates.
- [ ] **Define status transitions and decision authority** in `docs/authoring.md`: who may approve, waive, retire, or supersede a requirement; who may accept, close, or retire a risk; and who must approve unresolved or accepted high risks.
- [ ] **Specify automated semantic checks** alongside the validation script: required-field rules, TBD/TBR/TBS resolution data, UID rules, relation integrity, risk-level calculations, and warning-only sentence checks. Treat executable tests as the authoritative specification where practical.

## Before the corresponding review

- [ ] **Define MCR, SRR, PDR, CDR, TRR, and FRR** in `docs/reviews.md`. For each review, state its purpose, participants, required inputs, required repository state, decisions to make, exit criteria, disposition process, approver, and resulting baseline tag.
- [ ] **Define the baselining and change process** in `docs/reviews.md`: when a baseline is created, annotated-tag contents, how post-review dispositions are handled, how changes between baselines are approved, and the prohibition on moving or reusing baseline tags.
- [ ] **Define applicability and configuration conventions** in `docs/authoring.md`: how requirements, risks, evidence, and waivers identify the vehicle configuration and mission phase to which they apply.

## Before tests and flight operations

- [ ] **Create a minimal interface-control template** with only the mechanical, electrical, power, data/software, ownership, and verification information needed for integration.
- [ ] **Create minimal analysis and test-report templates** covering objective, configuration, method, result, linked requirements/risks, evidence location, anomalies, and conclusion.
- [ ] **Create a configuration-record template** that identifies the exact hardware, software revision, parameters, calibration state, and setup used for each test or flight.
- [ ] **Define verification-evidence handling**: procedure and evidence naming, storage/linking, reviewer expectations, failure and re-test handling, waivers, and the rule that flight-critical safety requirements receive initial verification before flight.
- [ ] **Create operations and flight-readiness checklist templates** with owner, vehicle/configuration identity, sign-offs, hold points, abort criteria, and links to applicable requirements and risks.
- [ ] **Define the minimum concept-of-operations content** needed to describe mission phases, actors, system states, nominal flow, off-nominal behavior, and success criteria without duplicating requirements.

## After the core workflow is proven

- [ ] Publish generated StrictDoc HTML for read-only member access; decide separately whether browser editing is worth supporting.
- [ ] Confirm that the generated verification matrix and traceability views are sufficient; add custom reporting only for a demonstrated review need.
- [ ] Extract the proven grammar, CI, templates, and generic guidance into a reusable starter for future rocket-program repositories.
- [ ] Decide whether shared guidance should eventually live in a club-wide systems-engineering repository; keep program-specific baselines, configurations, evidence, and decisions here.
