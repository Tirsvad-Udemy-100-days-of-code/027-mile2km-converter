"""Tests of the display-free conversion rule."""

import pytest

from mile2km.constants import KM_PER_MILE
from mile2km.converter import convert_text, format_km, miles_to_km, parse_miles


def test_miles_to_km_converts_ten_miles() -> None:
    assert miles_to_km(10) == pytest.approx(16.09)


def test_miles_to_km_of_zero_is_zero() -> None:
    assert miles_to_km(0) == 0


def test_miles_to_km_keeps_the_sign_of_a_negative_distance() -> None:
    assert miles_to_km(-2) == pytest.approx(-2 * KM_PER_MILE)


def test_miles_to_km_converts_a_fraction() -> None:
    assert miles_to_km(0.5) == pytest.approx(0.8045)


def test_format_km_rounds_to_two_decimals() -> None:
    assert format_km(16.0899) == "16.09"


def test_parse_miles_accepts_surrounding_spaces() -> None:
    assert parse_miles("  3.5 ") == 3.5


@pytest.mark.parametrize("text", ["", "abc", "1,5", "nan", "inf", "-inf"])
def test_parse_miles_rejects_text_that_is_not_a_finite_number(text: str) -> None:
    with pytest.raises(ValueError):
        parse_miles(text)


def test_convert_text_returns_formatted_kilometers() -> None:
    assert convert_text("10") == "16.09"


def test_convert_text_raises_for_invalid_input() -> None:
    with pytest.raises(ValueError):
        convert_text("ten")
