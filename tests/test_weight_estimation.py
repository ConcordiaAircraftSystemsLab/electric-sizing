import pytest
from electric_sizing.weight_estimation import (
    get_gross_takeoff_weight,
    get_empty_weight_fraction,
)
from electric_sizing.empty_weight_table import get_empty_weight_fraction_params


def test_get_gross_takeoff_weight():
    result = get_gross_takeoff_weight(200, 800, 0.4, 0.1)
    expected = (200 + 800) / (1 - 0.1 - 0.4)
    assert result == pytest.approx(expected)


def test_get_empty_weight_fraction():
    # Test with a known aircraft type
    aircraft_type = "Jet transport"
    params = get_empty_weight_fraction_params(aircraft_type)
    assert params != "Aircraft type not found"  # Ensure valid aircraft type

    result = get_empty_weight_fraction(10000, aircraft_type, variable_sweep=True)
    expected = params["A-metric"] * (10000 ** params["C"]) * 1.04
    assert result == pytest.approx(expected)

    result = get_empty_weight_fraction(10000, aircraft_type, variable_sweep=False)
    expected = params["A-metric"] * (10000 ** params["C"])
    assert result == pytest.approx(expected)


def test_get_empty_weight_fraction_invalid_aircraft_type():
    # Test with an unknown aircraft type to check error handling
    aircraft_type = "Unknown aircraft"
    with pytest.raises(KeyError):
        get_empty_weight_fraction(10000, aircraft_type, variable_sweep=False)


if __name__ == "__main__":
    pytest.main()
