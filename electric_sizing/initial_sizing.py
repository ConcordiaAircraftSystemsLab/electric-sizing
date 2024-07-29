def get_battery_mass_fraction(
    known_run_time: float,
    battery_specific_energy: float,
    total_system_efficiency: float,
    power_used: float,
    aircraft_mass: float,
):
    """
    Calculate the mass fraction of the battery in an electric aircraft.

    Args:
        known_run_time (float): The known run time of the aircraft in hours.
        battery_specific_energy (float): The specific energy of the battery in Wh/kg.
        total_system_efficiency (float): The overall efficiency of the aircraft.
        power_used (float): The power consumed by the aircraft in kW.
        aircraft_mass (float): The total mass of the aircraft in kg.

    Returns:
        float: The mass fraction of the battery in the aircraft.
    """

    return (
        1000
        * known_run_time
        * power_used
        / (battery_specific_energy * total_system_efficiency * aircraft_mass)
    )


def get_battery_mass_fraction_loiter(
    loiter_time,
    velocity,
    battery_specific_energy,
    total_system_efficiency,
    propeller_efficiency,
    lift_to_drag_ratio,
    gravitational_acceleration: float = 9.81,
):
    """
    Calculate the mass fraction of the battery during loiter phase in an electric aircraft.

    Args:
        loiter_time (float): The time the aircraft spends in loiter phase in hours.
        velocity (float): The velocity of the aircraft in km/hr.
        battery_specific_energy (float): The specific energy of the battery in Wh/kg.
        total_system_efficiency (float): The total efficiency of the system.
        propeller_efficiency (float): The efficiency of the propeller.
        lift_to_drag_ratio (float): The lift-to-drag ratio of the aircraft.
        gravitational_acceleration (float, optional): The gravitational acceleration in m/s^2.
                                                      Default is 9.81.

    Returns:
        float: The mass fraction of the battery during the loiter phase.
    """

    return (
        loiter_time
        * velocity
        * gravitational_acceleration
        / (
            3.6
            * battery_specific_energy
            * total_system_efficiency
            * propeller_efficiency
            * lift_to_drag_ratio
        )
    )


def get_battery_mass_fraction_cruise(
    range: float,
    battery_specific_energy: float,
    total_system_efficiency: float,
    propeller_efficiency: float,
    lift_to_drag_ratio: float,
    gravitational_acceleration: float = 9.81,
):
    """
    Calculate the mass fraction of the battery during cruise phase in an electric aircraft.

    Args:
        range (float): The range the aircraft can cover in km.
        battery_specific_energy (float): The specific energy of the battery in Wh/kg.
        total_system_efficiency (float): The total efficiency of the system.
        propeller_efficiency (float): The efficiency of the propeller.
        lift_to_drag_ratio (float): The lift-to-drag ratio of the aircraft.
        gravitational_acceleration (float, optional): The gravitational acceleration in m/s^2.
                                                      Default is 9.81.

    Returns:
        float: The mass fraction of the battery during the cruise phase.
    """

    return (
        range
        * gravitational_acceleration
        / (
            3.6
            * battery_specific_energy
            * total_system_efficiency
            * propeller_efficiency
            * lift_to_drag_ratio
        )
    )


def get_battery_mass_fraction_climb(
    climb_altitude: float,
    power_used: float,
    rate_of_climb: float,
    battery_specific_energy: float,
    total_system_efficiency: float,
    aircraft_mass: float,
):
    """
    Calculate the mass fraction of the battery during the climb phase in an electric aircraft.

    Args:
        climb_altitude (float): The altitude gained during the climb in meters.
        power_used (float): The power used by the aircraft in kW.
        rate_of_climb (float): The rate of climb of the aircraft in km/hr.
        battery_specific_energy (float): The specific energy of the battery in Wh/kg.
        total_system_efficiency (float): The total efficiency of the system.
        aircraft_mass (float): The total mass of the aircraft in kg.

    Returns:
        float: The mass fraction of the battery during the climb phase.
    """

    return (
        climb_altitude
        * power_used
        / (
            3.6
            * rate_of_climb
            * battery_specific_energy
            * total_system_efficiency
            * aircraft_mass
        )
    )
