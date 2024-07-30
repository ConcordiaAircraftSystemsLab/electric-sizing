from scipy.optimize import fsolve

from electric_sizing.initial_sizing import get_battery_mass_fraction_cruise
from electric_sizing.iterative_gross_takeoff_weight import (
    calculate_gross_takeoff_weight,
)


def main():
    bmf = get_battery_mass_fraction_cruise(
        range=125,  # km, Pipistrel Velis Electro
        battery_specific_energy=170,  # The Electro's batteries are rated @ 12.4 kWh and weigh 70 kg each
        total_system_efficiency=0.88,  # This is a guess
        propeller_efficiency=0.85,  # This is a guess
        lift_to_drag_ratio=15,  # Pipistrel Velis Electro
    )

    guess_weight = 1000

    calculated_weight = calculate_gross_takeoff_weight(
        battery_mass_fraction=bmf,
        crew_weight=80,
        payload_weight=80,
        aircraft_type="General aviation—single engine",
        guess_weight=guess_weight,
    )

    print(f"Calculated gross takeoff weight: {calculated_weight:.2f} kg")
    print("Compare to the Pipistrel Velis Electric's MTOW of 600 kg")


if __name__ == "__main__":
    main()
