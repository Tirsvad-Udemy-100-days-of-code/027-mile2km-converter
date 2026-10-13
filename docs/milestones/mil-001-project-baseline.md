# MIL-001 Project baseline

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Purpose

Decide whether the project skeleton and tooling are ready for application code: configuration, ignore rules, source documentation configuration and continuous integration exist and work.

## Deliverable

`pyproject.toml`, Python `.gitignore`, `Doxyfile`, the `src/` and `tests/` folders and a CI workflow that runs pytest, merged to `main` by pull request.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `pyproject.toml` declares `requires-python` above 3.13 and an empty runtime `dependencies` list | Met | Not met |
| 2 | `.gitignore` ignores `.venv/`, `__pycache__/` and `.env`, and `git status` never shows `.env` | Met | Not met |
| 3 | `Doxyfile` is present and `doxygen Doxyfile` reads it without configuration errors (or the missing tool is recorded) | Met | Not met |
| 4 | CI workflow file exists and runs pytest after creating a venv | Met | Not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| none | First milestone |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 3, 4 | Scope: `pyproject.toml`, `.gitignore`, `Doxyfile` |
| Constraints: Python above 3.13, venv, pytest | `pyproject.toml` |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-14 — one day after the plan is accepted; within the one-day Business Case cost estimate.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Add Python .gitignore | Add the standard Python `.gitignore` and also ignore `.env`, `.venv/` and Doxygen output, so the personal token file is never committed and the repository stays clean for S03. | No | [BC-001] Constraints |
| 2 | Add pyproject.toml | Project configuration: name, version, `requires-python = ">=3.13"`, no runtime dependencies, a `dev` optional dependency group with pytest, and pytest settings (`pythonpath = src`, `testpaths = tests`). Needed by every later task and by CI. | No | [BC-001] Constraints |
| 3 | Add Doxyfile | Doxygen configuration that reads `src/`, writes HTML to `docs/doxygen/` and extracts Doxygen comments. Supports Business Case objective 4. | No | [BC-001] Objective 4 |
| 4 | Create src and tests layout | Create the `src/mile2km/` package and `tests/` with a `conftest.py` so pytest runs from the repository root. Provides the required folder structure. | No | [BC-001] Constraints |
| 5 | Add CI workflow | Gitea Actions workflow (`.gitea/workflows/ci.yml`) that sets up Python 3.13, creates a venv, installs `.[dev]` and runs pytest on pull requests and pushes to `main`. Documented in the README section Continuous integration. | No | [BC-001] Success criterion 1 |

---

[BC-001]: ../business-case.md
