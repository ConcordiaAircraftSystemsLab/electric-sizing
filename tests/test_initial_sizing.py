import pytest
from electric_sizing.initial_sizing import (
    get_battery_mass_fraction,
    get_battery_mass_fraction_loiter,
    get_battery_mass_fraction_cruise,
    get_battery_mass_fraction_climb,
)


def test_get_battery_mass_fraction():
    result = get_battery_mass_fraction(1, 200, 0.85, 50, 1000)
    expected = 1000 * 1 * 50 / (200 * 0.85 * 1000)
    assert result == pytest.approx(expected)


def test_get_battery_mass_fraction_loiter():
    result = get_battery_mass_fraction_loiter(1, 300, 200, 0.85, 0.9, 15)
    expected = 1 * 300 * 9.81 / (3.6 * 200 * 0.85 * 0.9 * 15)
    assert result == pytest.approx(expected)


def test_get_battery_mass_fraction_cruise():
    result = get_battery_mass_fraction_cruise(500, 200, 0.85, 0.9, 15)
    expected = 500 * 9.81 / (3.6 * 200 * 0.85 * 0.9 * 15)
    assert result == pytest.approx(expected)


def test_get_battery_mass_fraction_climb():
    result = get_battery_mass_fraction_climb(1000, 50, 300, 200, 0.85, 1000)
    expected = 1000 * 50 / (3.6 * 300 * 200 * 0.85 * 1000)
    assert result == pytest.approx(expected)


if __name__ == "__main__":
    pytest.main()
