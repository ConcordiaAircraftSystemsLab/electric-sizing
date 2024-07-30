from electric_sizing.visualization.weight_plots import plot_lift_to_drag_sweep
from electric_sizing.initial_sizing import get_battery_mass_fraction_cruise
from electric_sizing.iterative_gross_takeoff_weight import (
    calculate_gross_takeoff_weight,
)


def main():

    flight_range = 125  # km, Pipistrel Velis Electro
    # The Electro's batteries are rated @ 12.4 kWh and weigh 70 kg each
    battery_specific_energy = 170
    total_system_efficiency = 0.88  # This is a guess
    propeller_efficiency = 0.85  # This is a guess

    guess_weight = 1000

    crew_weight = 80
    payload_weight = 80
    aircraft_type = "General aviation—single engine"

    plot_lift_to_drag_sweep(
        lift_to_drag_lower=10,
        lift_to_drag_upper=20,
        aircraft_range=flight_range,
        battery_specific_energy=battery_specific_energy,
        total_system_efficiency=total_system_efficiency,
        propeller_efficiency=propeller_efficiency,
        crew_weight=crew_weight,
        payload_weight=payload_weight,
        aircraft_type=aircraft_type,
        guess_weight=guess_weight,
        n_points=100,
        color="blue",
        marker="o",
    )


if __name__ == "__main__":
    main()
