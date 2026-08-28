def convert_units(value, from_unit, to_unit):
    """Convert between supported units."""
    conversions = {
        ("m", "cm"): 100,
        ("cm", "m"): 0.01,
        ("km", "m"): 1000,
        ("m", "km"): 0.001,
    }

    key = (from_unit, to_unit)

    if key not in conversions:
        raise ValueError("Unsupported conversion")

    return value * conversions[key]