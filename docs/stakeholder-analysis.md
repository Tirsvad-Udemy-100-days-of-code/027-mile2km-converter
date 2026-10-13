# Stakeholder Analysis

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Purpose

Identify who is affected by the miles-to-kilometers converter project and what each needs from it, using a power/interest grid. It supports the Business Case [BC-001] and gives every other artifact stable stakeholder IDs.

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Course participant: Product Owner, developer and reviewer | Tirsvad | HIGH | HIGH | Manage Closely | A correct, tidy assignment solution worth publishing |
| S02 | Udemy coursists | Fellow course participants | Udemy course community | LOW | HIGH | Keep Informed | Readable, runnable code with the assignment's function names, and README instructions to run it |
| S03 | GitHub viewers | Repository visitors | Public | LOW | LOW | Monitor | A clear repository description, topics and README, and no runtime dependencies |

## Power/Interest Classification Rationale

- **Manage Closely (S01):** decides scope, builds and reviews everything.
- **Keep Informed (S02):** cannot change the project but depends on its usability; gets the README and wiki.
- **Monitor (S03):** casual visitors; the repository metadata and README are enough.

## Primary Concerns and FURPS+ Mapping

| ID | Concern | FURPS+ attribute |
| --- | --- | --- |
| S01 | Conversion is correct and the GUI follows the assignment | Functionality |
| S01 | Tests and CI prove it works | Reliability |
| S02 | The assignment's function names are kept | Functionality |
| S02 | Clear run instructions per operating system | Usability |
| S03 | Clear description, topics and README | Usability |
| S03 | No runtime dependencies | Implementation constraint |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| S01 | Chat and pull-request review | Per milestone | Run summary, review records | MIL-001 to MIL-003 |
| S02 | README and wiki (en, da, ms) | Once, at publication | Run instructions, screenshots | MIL-003 |
| S03 | Repository description, topics, README | Once, at publication | Metadata and README | MIL-003 |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| Richer GUI features versus a minimal assignment-faithful solution | S01, S02 | Keep to the assignment; extra conversions are out of scope in [BC-001] |
| Tooling (Doxygen, CI) versus "no dependencies" | S01, S03 | Tooling is development-only; runtime has zero dependencies |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | Correct converter | [BC-001] Objectives 1, 2 |
| S02 | Run instructions | [BC-001] Objectives 3, 5 |
| S03 | Repository clarity | [BC-001] Objectives 5, 6 |

## Sign-Off

| Stakeholder | Decision | Date |
| --- | --- | --- |
| S01 | pending review | |

---

[BC-001]: ./business-case.md
