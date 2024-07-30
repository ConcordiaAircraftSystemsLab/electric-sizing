AIRCRAFT_DATA = {
    "Sailplane—unpowered": {"A-metric": 0.83, "C": -0.05},
    "Sailplane—powered": {"A-metric": 0.88, "C": -0.05},
    "Homebuilt—metal/wood": {"A-metric": 1.11, "C": -0.09},
    "Homebuilt—composite": {"A-metric": 1.07, "C": -0.09},
    "General aviation—single engine": {"A-metric": 2.05, "C": -0.18},
    "General aviation—twin engine": {"A-metric": 1.4, "C": -0.10},
    "Agricultural aircraft": {"A-metric": 0.72, "C": -0.10},
    "Twin turboprop": {"A-metric": 0.92, "C": -0.03},
    "Flying boat": {"A-metric": 1.05, "C": -0.05},
    "Jet trainer": {"A-metric": 1.47, "C": -0.10},
    "Jet fighter": {"A-metric": 2.11, "C": -0.13},
    "Military cargo/bomber": {"A-metric": 0.88, "C": -0.07},
    "Jet transport": {"A-metric": 0.97, "C": -0.06},
    "UAV—Tac Recce & UCAV": {"A-metric": 1.47, "C": -0.16},
    "UAV—high altitude": {"A-metric": 2.39, "C": -0.18},
    "UAV—small": {"A-metric": 0.93, "C": -0.06},
}


def get_empty_weight_fraction_params(aircraft_type: str):
    if aircraft_type not in AIRCRAFT_DATA:
        raise KeyError(f"Aircraft type '{aircraft_type}' not found in AIRCRAFT_DATA")
    return AIRCRAFT_DATA[aircraft_type]
