import matplotlib.pyplot as plt
import numpy as np

from electric_sizing.initial_sizing import get_battery_mass_fraction_cruise
from electric_sizing.iterative_gross_takeoff_weight import (
    calculate_gross_takeoff_weight,
)


def plot_lift_to_drag_sweep(
    lift_to_drag_lower: float,
    lift_to_drag_upper: float,
    aircraft_range: float,
    battery_specific_energy: float,
    total_system_efficiency: float,
    propeller_efficiency: float,
    crew_weight: float,
    payload_weight: float,
    aircraft_type: str,
    guess_weight=1000,
    n_points: int = 10,
    **plot_kwargs,
):
    """
    Plot the relationship between lift-to-drag ratio and gross takeoff weight for an aircraft.

    Args:
        lift_to_drag_lower (float): The lower bound of lift-to-drag ratio to sweep.
        lift_to_drag_upper (float): The upper bound of lift-to-drag ratio to sweep.
        aircraft_range (float): The range the aircraft can cover in km.
        battery_specific_energy (float): The specific energy of the battery in Wh/kg.
        total_system_efficiency (float): The total efficiency of the system.
        propeller_efficiency (float): The efficiency of the propeller.
        crew_weight (float): The weight of the crew in kg.
        payload_weight (float): The weight of the payload in kg.
        aircraft_type (str): The type of the aircraft.
        guess_weight (float, optional): The initial guess for the gross takeoff weight in kg. Default is 1000.
        n_points (int, optional): The number of points to plot. Default is 10.

    Returns:
        None
    """

    lift_to_drag_ratios = np.linspace(lift_to_drag_lower, lift_to_drag_upper, n_points)
    gross_weights = np.zeros(len(lift_to_drag_ratios))

    for i, l_d in enumerate(lift_to_drag_ratios):
        bmf = get_battery_mass_fraction_cruise(
            aircraft_range=aircraft_range,
            battery_specific_energy=battery_specific_energy,
            total_system_efficiency=total_system_efficiency,
            propeller_efficiency=propeller_efficiency,
            lift_to_drag_ratio=l_d,
        )

        calculated_weight = calculate_gross_takeoff_weight(
            battery_mass_fraction=bmf,
            crew_weight=crew_weight,
            payload_weight=payload_weight,
            aircraft_type=aircraft_type,
            guess_weight=guess_weight,
        )

        gross_weights[i] = calculated_weight

    plt.plot(lift_to_drag_ratios, gross_weights, **plot_kwargs)
    plt.xlabel("Lift to drag ratio [-]")
    plt.ylabel("Estimated gross take-off weight")

    plt.show()
