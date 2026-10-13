# MIL-004 GUI tests in CI

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-004 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [9bcf252] |

---

## Purpose

Decide whether the continuous-integration run exercises the Tkinter window tests instead of skipping them, so a change to the window is verified on every pull request.

## Deliverable

An updated `.gitea/workflows/ci.yml` that installs `python3-tk` and a virtual display on the runner and runs pytest under it, with the README and review record updated to match.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | The CI run on the pull request is green | Met | Not met |
| 2 | The pytest log of that run shows the `tests/test_gui.py` tests as passed, with 0 skipped | Met | Not met |
| 3 | The workflow keeps explicit permissions, a timeout and exact action versions, and its review record is a `Go` | Met | Not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-001 | The CI workflow exists |
| MIL-002 | The GUI tests exist |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 2, success criterion 1 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-14 — a one-file change, within the one-day effort of [BC-001].

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Run GUI tests in CI | Add a step to `.gitea/workflows/ci.yml` that installs `python3-tk` and `xvfb` with apt and runs pytest under `xvfb-run`, so the Tk tests are no longer skipped on the runner. Install only what is needed, keep the permissions and pinned actions, and confirm on the pull request that the GUI tests pass. | No | [BC-001] Objective 2 |
| 2 | Update README and workflow review | Change the README section Continuous integration, which says the GUI tests are skipped on the runner, and add a review record for the changed workflow against the workflow and YAML checklists. | No | [BC-001] Success criterion 1 |

---

[BC-001]: ../business-case.md
[9bcf252]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/027-mile2km-converter/commit/9bcf2525f61cd2b9ade0d7ba4e6857e7e83890ab
