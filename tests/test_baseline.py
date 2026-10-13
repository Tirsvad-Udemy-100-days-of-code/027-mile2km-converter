"""Baseline check that the package is importable, so CI has a test to run."""

import mile2km


def test_package_is_importable() -> None:
    assert mile2km.__name__ == "mile2km"
