# MIL-002 Converter application

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Purpose

Decide whether the miles-to-kilometers converter works as the assignment describes and is covered by tests, so that the documentation can describe a finished product.

## Deliverable

A Tkinter application in `src/mile2km/` with `constants.py`, a display-free conversion function and a GUI window, plus pytest tests, all with Doxygen comments.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `miles_to_km(10)` returns 16.09, and zero, negative and fractional inputs are tested | Met | Not met |
| 2 | Window titled "Miles to Kilometer Converter" has an entry, labels `Miles`, `is equal to` and `Km`, a result label and a Calculate button | Met | Not met |
| 3 | Pressing Calculate with a valid number shows the kilometers; invalid text shows a message and does not crash | Met | Not met |
| 4 | All constants (conversion factor, titles, labels, padding) live in `constants.py` | Met | Not met |
| 5 | `pytest` passes with 0 failures and the code review against the Python QC checklist is `Go` | Met | Not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-001 | pyproject, layout and CI must exist before code |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 1, 2 | Application and tests |
| Success criteria 1, 3 | Correctness, zero runtime dependencies |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-16 — two days after MIL-001.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Add constants.py | Create `src/mile2km/constants.py` with the miles-to-kilometers factor (1.609), window title, label texts, entry width and padding. Other modules import from it; no magic numbers elsewhere. | No | [BC-001] Constraints |
| 2 | Implement conversion function | Add `miles_to_km(miles: float) -> float` in a display-free module (the assignment's function name) using the factor from `constants.py`, plus a rounded text formatter for display. Keeping it free of Tkinter makes it testable without a display. | No | [BC-001] Objective 2 |
| 3 | Build Tkinter window | Build the window as in the lecture: entry, `Miles`, `is equal to` and `Km` labels, a result label and a Calculate button in a grid layout. `button_clicked` reads the entry, converts through `miles_to_km` and updates the result label; invalid input shows a message. | No | [BC-001] Objective 1 |
| 4 | Add entry point | Add `src/mile2km/__main__.py` so `python -m mile2km` starts the app, with a `main()` function. The command is documented in the README. | No | [BC-001] Objective 1 |
| 5 | Add pytest tests | Test the conversion (typical, zero, negative, fractional), the formatter and the invalid-input path through a GUI-free function; a GUI smoke test is skipped when no display is available. | No | [BC-001] Objective 2 |
| 6 | Review code against QC checklist | Review `src/` and `tests/` against the Python checklist in `framework/qc/code/`, record the `RC-*` and fix findings before the pull request. | No | [BC-001] Success criterion 1 |

---

[BC-001]: ../business-case.md
