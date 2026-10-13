# MIL-003 Documentation and publication

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [04cc0e3] |

---

## Purpose

Decide whether S02 and S03 can find, understand and run the project: README, screenshots, a wiki in three languages, source documentation and repository metadata are complete.

## Deliverable

`README.md` from the project template, screenshots under `docs/images/`, a wiki in English, Danish and Bahasa Malaysia, a Doxygen build, and the repository description and topics set on the git host.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `README.md` has every section of the template and passes `framework/scripts/check-readme.sh` | Met | Not met |
| 2 | README and each wiki language show a screenshot of the running app | Met | Not met |
| 3 | Wiki has Home, Install and Usage pages in en, da and ms, plus a sidebar | Met | Not met |
| 4 | `doxygen Doxyfile` completes without warnings about undocumented public items in `src/` | Met | Not met |
| 5 | Repository description and at least 3 topics are set on the git host | Met | Not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-002 | The documentation describes the finished application |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 3, 4, 5, 6 | README, Doxygen, wiki, metadata |
| Success criteria 2, 4, 5 | Runs from clean clone, 3 wiki languages, metadata |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-20 — three days after MIL-002, with a buffer for wiki and token issues.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Write README | Write `README.md` with the template sections (Requirements, Set up for Windows PowerShell, Linux Debian and MacOS, Run, Run the tests, Continuous integration, Build the source documentation, Project layout, License), including how to create and use a `.venv` and `python -m pip install --upgrade pip`. | No | [BC-001] Objective 3 |
| 2 | Capture screenshots | Run the app and capture screenshots of the window before and after a conversion, save them under `docs/images/` and embed them in the README and the wiki. | No | [BC-001] Objective 5 |
| 3 | Verify Doxygen build | Run `doxygen Doxyfile`, fix undocumented items and keep generated output out of git. | No | [BC-001] Objective 4 |
| 4 | Write wiki in three languages | Write Home, Install and Usage in English, Danish and Bahasa Malaysia with the screenshot, following the naming of the example wiki (`Page.md`, `Page-da.md`, `Page-ms.md`) and a `_Sidebar.md`; publish to the repository wiki. | No | [BC-001] Objective 5 |
| 5 | Set repository description and topics | Use the git host API with the token from `.env` (never printed, imported or committed) to set the repository description and topics: python, tkinter, gui, converter, udemy, 100-days-of-code. | No | [BC-001] Objective 6 |
| 6 | Run framework document checks | Run `check-readme.sh` and `check-languages.sh`, fix findings, and confirm the README steps work from a fresh clone and venv. | No | [BC-001] Success criterion 2 |

---

[BC-001]: ../business-case.md
[04cc0e3]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/027-mile2km-converter/commit/04cc0e3e8494b836cd6445d64b0ff967354b2545
