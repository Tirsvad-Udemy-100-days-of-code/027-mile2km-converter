# RC-008 code-mil-002 review

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-008 |
| CrossReference | [code-mil-002], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [190a1fa] |

---

## Artifact Under Review

- Instance reviewed: [code-mil-002]
- Checklist used: [QC-PY-001]
- Scope: full review of src/mile2km/*.py and tests/*.py
- Language and domain: n/a
- Language reviewer: none
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | `ConverterWindow`, snake_case functions and modules, UPPER_SNAKE constants. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names state purpose: `miles_to_km`, `parse_miles`, `format_km`, `button_clicked`. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | ruff 0.17.0 check and format are clean with default rules; no suppressions in `src/`. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | Every function, method, test and fixture is annotated, including `-> None`; mypy --strict is clean. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | `parse_miles` raises `ValueError` from the cause; the `except ValueError` in `button_clicked` shows a message; no bare except. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | Only `master: tk.Tk | None = None`; no builtin is shadowed. |
| 7 | Files, locks and connections are managed with context managers | N-A | No files, locks or connections are used. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Every module, class and function has a Doxygen docstring with brief, param and return. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | No `print` and no logging is needed; no secrets exist. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | Pass | No DCD exists in this project (no use case or design artifact was planned, see [PP-001] Open Issues). Each class and function traces to its MIL-002 task by its module and docstring; this deviation is recorded here and is open to challenge. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | Tests are named for behaviour, order-independent, with no network. The GUI tests share one Tk root to avoid flaky display creation, and skip without a display. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | `mypy --strict src tests` is clean (mypy installed ad hoc, not a project dependency); `Any` is used once in the workflow test with a justification. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | `dependencies = []`; development dependencies are pinned exactly. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | Each number and text is defined once in `constants.py`; `format_km` is the only formatter. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | `converter.py` imports only `math` and `constants`; `gui.py` imports the converter and constants; no cycles. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | The conversion rule is separate from the window; the window delegates to `convert_text`; no type switches. |

## Overall Verdict

Go — all Mandatory criteria pass after the review edits (flaky GUI fixture fixed). Review done by the python-developer agent and the author.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| No open action | S01 | 2026-10-13 |

---

[code-mil-002]: ../../../src/mile2km/gui.py
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[190a1fa]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/027-mile2km-converter/commit/190a1fa44b010a11c4d8f0e71b8ce52bc7b639d7
