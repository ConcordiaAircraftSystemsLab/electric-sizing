from scipy.optimize import fsolve

from electric_sizing.weight_estimation import (
    get_empty_weight_fraction,
    get_gross_takeoff_weight,
)


def calculate_gross_takeoff_weight(
    battery_mass_fraction: float,
    crew_weight: float,
    payload_weight: float,
    aircraft_type: str,
    guess_weight: float,
):
    """
    Calculate the gross takeoff weight of an aircraft iteratively based on battery mass fraction and other parameters.

    Args:
        bmf (float): The battery mass fraction of the aircraft.
        crew_weight (float): The weight of the crew in kg.
        payload_weight (float): The weight of the payload in kg.
        aircraft_type (str): The type of the aircraft.
        guess_weight (float): The initial guess for the gross takeoff weight in kg.

    Returns:
        float: The calculated gross takeoff weight of the aircraft.
    """

    # Define the target function to solve for gross takeoff weight
    def target_function(w0):
        empty_weight_fraction = get_empty_weight_fraction(w0, aircraft_type)
        return w0 - get_gross_takeoff_weight(
            crew_weight, payload_weight, empty_weight_fraction, battery_mass_fraction
        )

    # Use fsolve to find the root of the target function (the gross takeoff weight)
    return fsolve(target_function, x0=guess_weight)[0]
