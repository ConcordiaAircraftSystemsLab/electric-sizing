import pytest
from scipy.optimize import fsolve

from electric_sizing.empty_weight_table import get_empty_weight_fraction_params
from electric_sizing.iterative_gross_takeoff_weight import (
    calculate_gross_takeoff_weight,
)
from electric_sizing.weight_estimation import (
    get_empty_weight_fraction,
    get_gross_takeoff_weight,
)


# Mock the get_empty_weight_fraction function to return controlled outputs for testing
@pytest.fixture
def mock_get_empty_weight_fraction(monkeypatch):
    def mock_params(gross_takeoff_weight, aircraft_type):
        if aircraft_type == "General aviation—single engine":
            return 0.6  # Example value for testing
        raise KeyError(f"Aircraft type '{aircraft_type}' not found")

    monkeypatch.setattr(
        "electric_sizing.weight_estimation.get_empty_weight_fraction", mock_params
    )


# Mock the get_gross_takeoff_weight function to return controlled outputs for testing
@pytest.fixture
def mock_get_gross_takeoff_weight(monkeypatch):
    def mock_params(
        crew_weight, payload_weight, empty_weight_fraction, battery_mass_fraction
    ):
        return (crew_weight + payload_weight) / (
            1 - empty_weight_fraction - battery_mass_fraction
        )

    monkeypatch.setattr(
        "electric_sizing.weight_estimation.get_gross_takeoff_weight", mock_params
    )


def test_calculate_gross_takeoff_weight(
    mock_get_empty_weight_fraction, mock_get_gross_takeoff_weight
):
    # Test with a set of known parameters
    battery_mass_fraction = 0.15
    crew_weight = 80  # kg
    payload_weight = 80  # kg
    aircraft_type = "General aviation—single engine"
    guess_weight = 1000  # Initial guess for gross takeoff weight in kg

    result = calculate_gross_takeoff_weight(
        battery_mass_fraction,
        crew_weight,
        payload_weight,
        aircraft_type,
        guess_weight,
    )

    expected = fsolve(
        lambda w0: w0
        - (crew_weight + payload_weight)
        / (1 - get_empty_weight_fraction(w0, aircraft_type) - battery_mass_fraction),
        x0=guess_weight,
    )[0]
    assert result == pytest.approx(expected)


if __name__ == "__main__":
    pytest.main()
