from electric_sizing.initial_sizing import get_battery_mass_fraction_cruise
from electric_sizing.weight_estimation import (
    get_gross_takeoff_weight,
    get_empty_weight_fraction,
)

from scipy.optimize import fsolve


def main():
    bmf = get_battery_mass_fraction_cruise(
        range=100,
        battery_specific_energy=250,
        total_system_efficiency=0.88,
        propeller_efficiency=0.8,
        lift_to_drag_ratio=11,
    )

    guess_weight = 1000

    target_function = lambda w0: w0 - get_gross_takeoff_weight(
        250, 150, get_empty_weight_fraction(w0, "General aviation—single engine"), bmf
    )

    result = fsolve(target_function, x0=guess_weight)

    print(result)


if __name__ == "__main__":
    main()
