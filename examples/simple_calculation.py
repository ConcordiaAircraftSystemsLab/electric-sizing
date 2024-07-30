from electric_sizing.initial_sizing import get_battery_mass_fraction_cruise
from electric_sizing.weight_estimation import get_gross_takeoff_weight


def main():
    bmf = get_battery_mass_fraction_cruise(
        aircraft_range=100,
        battery_specific_energy=250,
        total_system_efficiency=0.88,
        propeller_efficiency=0.8,
        lift_to_drag_ratio=11,
    )

    gross_takeoff_weight = get_gross_takeoff_weight(250, 150, 0.55, bmf)

    print(gross_takeoff_weight)


if __name__ == "__main__":
    main()
