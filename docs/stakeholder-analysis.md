# Stakeholder Analysis

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001], [MIL-005] |
| Language | en |
| Domain | education |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [04cc0e3] |
| 2026-11-15 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Added concern IDs CN-001 to CN-006 (QC-SA-001 criterion 9), the baseline concern CN-007, the baseline milestone in the communication table, a conflict about the stand-in reviewer and the traceability of the concerns; set the domain to education; reviewed in autonomous mode, not independent | pending |

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

| Concern ID | Stakeholder | Concern | FURPS+ attribute |
| --- | --- | --- | --- |
| CN-001 | S01 | Conversion is correct and the GUI follows the assignment | Functionality |
| CN-002 | S01 | Tests and CI prove it works | Reliability |
| CN-003 | S02 | The assignment's function names are kept | Functionality |
| CN-004 | S02 | Clear run instructions per operating system | Usability |
| CN-005 | S03 | Clear description, topics and README | Usability |
| CN-006 | S03 | No runtime dependencies | Implementation constraint |
| CN-007 | S01 | The project follows the common baseline of the framework, with a wiki in English, Danish and Malay | Supportability |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| S01 | Chat and pull-request review | Per milestone | Run summary, review records | MIL-001 to MIL-003 |
| S02 | README and wiki (en, da, ms) | Once, at publication | Run instructions, screenshots | MIL-003 |
| S03 | Repository description, topics, README | Once, at publication | Metadata and README | MIL-003 |
| S01 | Pull request on the git host and end-of-run summary in chat | Once, for the baseline milestone | Documents, wiki and review records to read, and the stand-in decisions | MIL-005 |
| S02, S03 | Wiki in English, Danish and Malay | Once, updated on change | Wiki pages | MIL-005 |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| Richer GUI features versus a minimal assignment-faithful solution | S01, S02 | Keep to the assignment; extra conversions are out of scope in [BC-001] |
| Tooling (Doxygen, CI) versus "no dependencies" | S01, S03 | Tooling is development-only; runtime has zero dependencies |
| The documents of the baseline milestone are accepted by an AI stand-in for S01, so that review is not independent | S01 | S01 authorised the stand-in for the baseline milestone only; every review record says `Mode: autonomous, not independent`, and the end-of-run summary lists each stand-in decision so that S01 can challenge it |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | Correct converter (CN-001, CN-002) | [BC-001] Objectives 1, 2 |
| S02 | Run instructions (CN-003, CN-004) | [BC-001] Objectives 3, 5 |
| S03 | Repository clarity (CN-005, CN-006) | [BC-001] Objectives 5, 6 |
| S01 | The project follows the common baseline of the framework (CN-007) | [BC-001] Objective 7 |

## Sign-Off

| Stakeholder | Decision | Date |
| --- | --- | --- |
| S01 | Accepted in chat | 2026-10-13 |
| S01 (AI as stand-in, autonomous, not independent) | Accepted the changes of MIL-005 after RC-013 (Go) | 2026-11-15 |

---

[BC-001]: ./business-case.md
[04cc0e3]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/027-mile2km-converter/commit/04cc0e3e8494b836cd6445d64b0ff967354b2545
[MIL-005]: ./milestones/mil-005-framework-baseline.md
