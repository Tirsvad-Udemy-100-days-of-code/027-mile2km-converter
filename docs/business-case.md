# Business Case

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001], [PP-001], [MIL-001], [MIL-002], [MIL-003], [MIL-004], [MIL-005] |
| Language | en |
| Domain | education |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [04cc0e3] |
| 2026-11-15 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Added objective 7, success criterion 6, a scope item, an out-of-scope item, a risk, an assumption and a constraint exception for the baseline milestone MIL-005; changed the measure of success criterion 4 to the page names of the new wiki; set the domain to education; reviewed in autonomous mode, not independent | pending |

---

## Executive Summary

A course participant of Udemy's "100 Days of Code: The Complete Python Pro Bootcamp" must deliver the Day 27 assignment: a Tkinter miles-to-kilometers converter. The project builds that small graphical user interface (GUI) as a clean, tested, documented, dependency-free Python repository that other course participants and repository visitors can read, run and compare against. A later milestone, [MIL-005], brought the finished project to the baseline of the framework.

## Methodological and Standards Foundation

The project follows the software quality assurance (SQA) and quality control (QC) framework mounted at `framework/`: Business Case, Stakeholder Analysis, Project Plan, milestones, tasks as issues, then code, each step reviewed against its QC checklist. Quality characteristics are tagged with ISO/IEC 25010:2023. Code follows the `coding-conventions` skill for Python and the layering of the `clean-architecture` skill (the conversion rule is kept apart from the GUI).

## Problem Statement

The course assignment is normally solved in a single throw-away script. That gives the participant a working window but no tests, no documented way to run it, no source documentation and nothing another participant or a repository visitor can reuse or learn from.

## Business Opportunity

A well-structured reference solution lets the participant show a professional workflow (venv, pytest, CI, Doxygen, trilingual wiki) on a small problem, and gives S02 and S03 a readable example they can run in minutes.

## Objectives

1. Deliver a Tkinter application that converts miles to kilometers when the user presses the calculate button, using the assignment's layout and function names.
2. Keep the conversion rule testable without a display, with pytest tests.
3. Document set-up and use of a local `.venv` for Windows PowerShell, Debian Linux and macOS in the README.
4. Provide Doxygen comments in the source and a Doxyfile that builds the source documentation.
5. Provide a README (with screenshot) and a wiki in English, Danish and Bahasa Malaysia (with screenshots).
6. Publish the repository with a description and topics on the git host.
7. Bring the finished project to the common baseline of the framework: the adopted framework release, a wiki in English, Danish and Malay, complete licence metadata, a traceability matrix and review records ([MIL-005]).

## Scope

### In Scope

- Python application in `src/`, tests in `tests/`, documents in `docs/`.
- `constants.py` for constants, `pyproject.toml`, Python `.gitignore`, `Doxyfile`.
- Continuous-integration (CI) workflow running the tests.
- README from the project template, and a three-language wiki with screenshots.
- Repository description and topics.
- The baseline milestone [MIL-005]: framework release, wiki in English, Danish and Malay, README links to the project documents, licence metadata, traceability matrix and review records. It changes no behaviour of the converter.

### Out of Scope

- Other unit conversions (liters to gallons) and extra widgets such as radio buttons.
- Packaging for PyPI, installers or executables.
- Any runtime dependency beyond the Python standard library.
- Any change to `src/` or `tests/` in the baseline milestone [MIL-005].
- The `.env` file: it holds personal tokens, is never imported, tested or committed.

## Expected Benefits

### Tangible Benefits

- A runnable app and a green test suite from a clean clone with documented commands.
- A repository that passes the framework's README and language checks.

### Intangible Benefits

- A reusable template for the next Day-N assignments.
- Readable example code for S02 and S03.

## Strategic Alignment

The project supports the participant's goal of completing the 100 Days of Code course with work that is worth publishing, and the convention of one documented, tested project per course day.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | Conversion correctness | miles x 1.609 for every tested input | pytest passes, 0 failures |
| 2 | Runs from a clean clone | app starts with the README commands only | commands run on Windows PowerShell |
| 3 | Runtime dependencies | 0 packages outside the standard library | `pyproject.toml` has an empty `dependencies` list |
| 4 | Documentation languages | 3 wiki languages with screenshots | wiki pages Home, Getting-Started and Project-Documents exist in en, da, ms |
| 5 | Repository metadata | description and at least 3 topics set | git host API shows both |
| 6 | The baseline milestone is done (objective 7) | Wiki pages in 3 languages, `framework/scripts/check-readme.sh` exits with code 0, 100 % of the continuous integration (CI) checks of the pull request of [MIL-005] pass | Files in `docs/wiki/`, the script exit code and the pull request status on the git host |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Tkinter is missing on some Linux installs | S02 cannot run the app | README Debian section names the `python3-tk` package |
| Screenshot cannot be produced headless in continuous integration (CI) | README and wiki lack images | capture on the developer machine and commit the images under `docs/images/` |
| Token for the git host is missing or invalid | repository metadata and wiki cannot be published | stop and report; the user supplies the token in `.env` |
| Wiki is not enabled on the host | wiki cannot be pushed | stop and report; the user enables the wiki |
| Danish and Bahasa Malaysia wording has errors | readers misled | keep sentences short; S01 reviews the wording in the run summary |
| The documents of the baseline milestone [MIL-005] are reviewed by an AI stand-in for S01 | A defect is missed because the review is not independent | Every review record of the baseline says `Mode: autonomous, not independent`, and the end-of-run summary lists it for challenge |

## Assumptions

- Python 3.13 or newer with Tkinter is installed on the developer machine.
- The baseline milestone [MIL-005] is finished within one week of its own start, 2026-11-15, by 2026-11-22. For that milestone only, an AI stand-in for S01 reviews and accepts the changed documents.
- The Product Owner's language is English; the wiki translations are deliverables, not the language of the artifacts.
- The target repository is the `origin` remote of this clone.
- A Gitea token with repository scope is in `.env` as `GITEA_TOKEN`.

## Constraints

- Python greater than 3.13, a `venv` for the environment, pytest for tests, `constants.py` for constants.
- Folder layout `src/`, `tests/`, `docs/`.
- No runtime dependencies unless needed.
- Doxygen comments in source, with a Doxyfile.
- Work goes through branches and pull requests, one per milestone.
- The baseline milestone [MIL-005] is the exception to the review by S01: S01 has authorised the assistant to commit, push, open the pull request and merge it in autonomous mode.

## Cost–Benefit Assessment

| Costs | Benefits |
| --- | --- |
| About one working day of the participant's time; no licence or hosting cost | A published, tested reference solution and a reusable project template |

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Completes the assignment, owns the product, builds and reviews it |
| S02 | Reads, runs and compares the code |
| S03 | Browses the repository for ideas |

## Recommendation

Proceed — the scope is small, the constraints are clear and the benefit is a reusable reference repository.

---

[SA-001]: ./stakeholder-analysis.md
[04cc0e3]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/027-mile2km-converter/commit/04cc0e3e8494b836cd6445d64b0ff967354b2545
[PP-001]: ./project-plan.md
[MIL-001]: ./milestones/mil-001-project-baseline.md
[MIL-002]: ./milestones/mil-002-converter-application.md
[MIL-003]: ./milestones/mil-003-documentation-and-publication.md
[MIL-004]: ./milestones/mil-004-ci-gui-tests.md
[MIL-005]: ./milestones/mil-005-framework-baseline.md
