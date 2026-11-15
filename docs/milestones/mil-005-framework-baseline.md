# MIL-005 Framework baseline

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-005 |
| CrossReference | [BC-001], [PP-001], [MIL-003], [MIL-004] |
| Language | en |
| Domain | education |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-15 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version; accepted with the Go verdict of the review record (autonomous, not independent) | pending |

---

## Purpose

This gate decides whether Miles to Kilometer Converter has the baseline of the framework: the adopted framework release, a wiki in English, Danish and Malay, the README in the framework template, complete licence metadata and reviewed documents, merged to the default branch with a green build. The work is delivered on the branch `mil-005-framework-baseline` and one pull request.

## Deliverable

A merged pull request that holds: the updated Business Case, Stakeholder Analysis, Project Plan and milestones MIL-001 to MIL-004 with their review records; the traceability matrix; the wiki in English, Danish and Malay; the README with its layout and document appendix brought up to date; `pyproject.toml` with complete licence metadata; and the framework release adopted by the project. The converter and its tests do not change.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | BC-001, SA-001, PP-001, MIL-001 to MIL-004 and MIL-005 each have an `Accepted` Version History row and a review record with the verdict `Go` | All of them | Any missing or `Go-with-conditions` |
| 2 | `python -m pytest` runs | Exit code 0 | Any failure |
| 3 | `docs/wiki/` has `_Sidebar.md` and the pages Home, Getting-Started and Project-Documents in en, da and ms | 9 pages and the sidebar | A page or language missing |
| 4 | `framework/scripts/check-readme.sh` and `framework/scripts/check-languages.sh` run | Exit code 0 | Any finding |
| 5 | `pyproject.toml` sets `license`, `license-files` and the project URLs for the documentation and the issue tracker | All set | Any missing |
| 6 | All CI (continuous integration) checks of the pull request | Green | Red or pending |
| 7 | The pull request carries one `Closes #N` line per task of this milestone | Every issue is closed after the merge | An issue stays open |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-003] accepted | Documents and baselines the finished converter |
| [MIL-004] accepted | The CI workflow it describes has the form of that milestone |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 1 to 4 | Criterion 2 (the behaviour is unchanged and its tests pass) |
| Objective 7 | Criteria 1, 3, 4, 5 and 7 (documents, wiki, README, licence and issues) |
| Success criteria 4 and 6 | Criteria 3 and 6 (the wiki pages and the green pull request) |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 (AI as stand-in, autonomous mode, not independent) |

## Target Date

2026-11-22: one week after the start, as the Business Case assumption requires.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Adopt the framework release | Track the `framework/` submodule and `.gitmodules`, install the skills, hooks and `.editorconfig`, and track `.env.example`, so the project follows the same rules as the other projects of the portfolio. | No | Objective 7 |
| 2 | Update and review the planning documents | Add this milestone to the Business Case and Project Plan, add the missing MIL-004 to the plan, add concern IDs to the Stakeholder Analysis, set the domain of the earlier milestones, create the traceability matrix and review each changed document against its QC checklist, so the plan-first gate is met. | No | Objective 7 |
| 3 | Move the wiki into the repository in English, Danish and Malay | Write the pages Home, Getting-Started and Project-Documents in `docs/wiki/`, with the Danish and Malay pages named as the framework requires and a sidebar, carrying over the install and usage text of the existing pages, so a visitor can learn what the exercise is and how to run it in their own language. | No | Objective 7 |
| 4 | Update the README | Keep the README in the framework template and bring its project layout and document appendix up to date, with the links to the traceability matrix and the wiki, so the README is complete and checkable. | No | Objective 7 |
| 5 | Add licence metadata to pyproject.toml | Set the licence expression, `license-files`, authors and the project URLs for the repository, documentation and issue tracker, so package tools can read them. | No | Objective 7 |

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
[MIL-003]: ./mil-003-documentation-and-publication.md
[MIL-004]: ./mil-004-ci-gui-tests.md
