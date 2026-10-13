"""Static checks of the CI workflow: valid YAML, required keys, explicit permissions and runner."""

from pathlib import Path
from typing import Any, cast

import yaml

WORKFLOW = Path(__file__).resolve().parents[1] / ".gitea" / "workflows" / "ci.yml"


def _load() -> dict[Any, Any]:
    return cast(dict[Any, Any], yaml.safe_load(WORKFLOW.read_text(encoding="utf-8")))


def test_workflow_declares_name_triggers_and_jobs() -> None:
    workflow = _load()
    assert workflow["name"] == "CI"
    assert True in workflow or "on" in workflow  # YAML 1.1 parses the key `on` as True
    assert "test" in workflow["jobs"]


def test_workflow_has_least_privilege_and_bounded_jobs() -> None:
    workflow = _load()
    assert workflow["permissions"] == {"contents": "read"}
    job = workflow["jobs"]["test"]
    assert job["runs-on"] == "ubuntu-latest"
    assert job["timeout-minutes"] <= 15


def test_actions_are_pinned_to_exact_tags() -> None:
    steps = _load()["jobs"]["test"]["steps"]
    for step in steps:
        uses = step.get("uses")
        if uses:
            assert "@v" in uses and uses.count(".") >= 2, uses
