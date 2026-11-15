# Traceability Matrix: Miles to Kilometer Converter

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001], [SA-001], [PP-001], [MIL-001], [MIL-002], [MIL-003], [MIL-004], [MIL-005] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-15 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version; created with the review records of the baseline (autonomous, not independent) | [9fd6cde] |

---

## Purpose

Tracks backward and forward links between the artifact instances of Miles to Kilometer Converter so that the traceability of the documents is measurable. A row is added or updated whenever an instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [BC-001] | Business Case | en | education | - | [SA-001], [PP-001], [MIL-001], [MIL-002], [MIL-003], [MIL-004], [MIL-005] | [RC-012] (Go, re-review of the whole document), [RC-001] (Go, the first review) |
| [SA-001] | Stakeholder Analysis | en | education | [BC-001] | [PP-001] | [RC-013] (Go, re-review of the whole document), [RC-002] (Go, the first review) |
| [PP-001] | Project Plan | en | education | [BC-001], [SA-001] | [MIL-001], [MIL-002], [MIL-003], [MIL-004], [MIL-005] | [RC-014] (Go, review of the whole document; the plan had no review record before) |
| [MIL-001] | Milestone / Gateway | en | education | [BC-001], [PP-001] | [MIL-002] | [RC-015] (Go, re-review after the metadata change), [RC-003] (Go, the first review) |
| [MIL-002] | Milestone / Gateway | en | education | [BC-001], [MIL-001] | [MIL-003], [MIL-004] | [RC-016] (Go, re-review after the metadata change), [RC-004] (Go, the first review) |
| [MIL-003] | Milestone / Gateway | en | education | [BC-001], [MIL-002] | [MIL-005] | [RC-017] (Go, re-review after the metadata change), [RC-005] (Go, the first review) |
| [MIL-004] | Milestone / Gateway | en | education | [BC-001], [MIL-001], [MIL-002] | [MIL-005] | [RC-018] (Go, re-review after the metadata change), [RC-009] (Go, the first review) |
| [MIL-005] | Milestone / Gateway | en | education | [BC-001], [PP-001], [MIL-003], [MIL-004] | - | [RC-019] (Go) |
| Wiki | Wiki | en, da, ms | education | [BC-001] | - | [RC-020] (Go-with-conditions) |
| CI workflow (`.gitea/workflows/ci.yml`) | Workflow | - | - | [MIL-001], [MIL-004] | - | [RC-006] and [RC-007] (the first version), [RC-010] and [RC-011] (re-review after the change of MIL-004) |
| Python code of MIL-002 (`src/mile2km/`, `tests/`) | Python Source Code (PY) | - | - | [MIL-002] | - | [RC-008] |

## Concern Coverage

| Concern (CN-ID) | Views that answer it | Decisions (ADR) | Quality check (TP) | Status |
| --- | --- | --- | --- | --- |
| CN-001 | [MIL-002] (criteria 1 to 4) | - | - | Covered |
| CN-002 | [MIL-001] (criterion 4), [MIL-002] (criterion 5), [MIL-004] (criteria 1 and 2) | - | - | Covered |
| CN-003 | [MIL-002] (criteria 1 and 2) | - | - | Covered |
| CN-004 | [MIL-003] (criteria 1 and 2) | - | - | Covered |
| CN-005 | [MIL-003] (criteria 1 and 5) | - | - | Covered |
| CN-006 | [MIL-001] (criterion 1) | - | - | Covered |
| CN-007 | [MIL-005] (criteria 1, 3, 4 and 5) | - | - | Covered |

## Open Inconsistencies

| # | Views | Inconsistency | Found in (RC-ID) | Status | Resolved in |
| --- | --- | --- | --- | --- | --- |
| - | - | none found | - | Closed | - |

## Coverage Notes

- No view, design or test-plan artifact exists (the scope excludes them), so the concerns are covered by the Go/No-Go criteria of the milestones. In Upstream, `-` means foundational; in Downstream, `-` means nothing is built on it yet.
- The source code is reviewed in [RC-008] and not again in [MIL-005], which changes no source file. These records and this matrix have no QC checklist for themselves and are not reviewed.
- The domain of every artifact is `education` since [MIL-005]; the earlier review records state the former domain `it` as it was at the time. Criterion 3 of [MIL-003] still names the wiki pages Install and Usage as they were when that milestone was accepted; the wiki of [MIL-005] has the pages Home, Getting-Started and Project-Documents, and criterion 4 of the Business Case names them.

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
[MIL-001]: ../milestones/mil-001-project-baseline.md
[MIL-002]: ../milestones/mil-002-converter-application.md
[MIL-003]: ../milestones/mil-003-documentation-and-publication.md
[MIL-004]: ../milestones/mil-004-ci-gui-tests.md
[MIL-005]: ../milestones/mil-005-framework-baseline.md
[RC-001]: ./reviews/rc-001-business-case.md
[RC-002]: ./reviews/rc-002-stakeholder-analysis.md
[RC-003]: ./reviews/rc-003-mil-001.md
[RC-004]: ./reviews/rc-004-mil-002.md
[RC-005]: ./reviews/rc-005-mil-003.md
[RC-006]: ./reviews/rc-006-ci-workflow.md
[RC-007]: ./reviews/rc-007-ci-workflow-yaml.md
[RC-008]: ./reviews/rc-008-code-mil-002.md
[RC-009]: ./reviews/rc-009-mil-004.md
[RC-010]: ./reviews/rc-010-ci-workflow-gui.md
[RC-011]: ./reviews/rc-011-ci-workflow-gui-yaml.md
[RC-012]: ./reviews/rc-012-business-case-baseline.md
[RC-013]: ./reviews/rc-013-stakeholder-analysis-baseline.md
[RC-014]: ./reviews/rc-014-project-plan-baseline.md
[RC-015]: ./reviews/rc-015-milestone-001-baseline.md
[RC-016]: ./reviews/rc-016-milestone-002-baseline.md
[RC-017]: ./reviews/rc-017-milestone-003-baseline.md
[RC-018]: ./reviews/rc-018-milestone-004-baseline.md
[RC-019]: ./reviews/rc-019-milestone-005.md
[RC-020]: ./reviews/rc-020-wiki.md
[9fd6cde]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/027-mile2km-converter/commit/9fd6cde0a158f4d49e21e4156abda8d3cac2036e
