from .empty_weight_table import get_empty_weight_fraction_params


def get_gross_takeoff_weight(
    crew_weight: float,
    payload_weight: float,
    empty_weight_fraction: float,
    fuel_weight_fraction: float,
):
    """
    Calculate the gross takeoff weight of an aircraft based on weight fractions and payload.

    Args:
        crew_weight (float): The weight of the crew in kg.
        payload_weight (float): The weight of the payload in kg.
        empty_weight_fraction (float): The fraction of empty weight to gross weight.
        fuel_weight_fraction (float): The fraction of fuel weight to gross weight.

    Returns:
        float: The calculated gross takeoff weight of the aircraft.
    """

    return (crew_weight + payload_weight) / (
        1 - fuel_weight_fraction - empty_weight_fraction
    )


def get_empty_weight_fraction(
    gross_takeoff_weight: float,
    aircraft_type: str,
    variable_sweep: bool = False,
):
    """
    Calculate the empty weight fraction of an aircraft based on the gross takeoff weight and aircraft type.

    Args:
        gross_takeoff_weight (float): The gross takeoff weight of the aircraft in kg.
        aircraft_type (str): The type of the aircraft.
        variable_sweep (bool, optional): Indicates if the aircraft has variable sweep wings. Default is False.

    Returns:
        float: The calculated empty weight fraction of the aircraft.
    """

    regression_params = get_empty_weight_fraction_params(aircraft_type)

    if isinstance(regression_params, str):
        return (
            regression_params  # Return the error message if aircraft type is not found
        )

    return (
        regression_params["A-metric"]
        * (gross_takeoff_weight ** regression_params["C"])
        * (1.04 if variable_sweep else 1)
    )
