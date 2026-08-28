def calc_power(voltage, resistance):
    """Calculate power dissipated in a resistor.
    
    Args:
        voltage (float): Voltage across the resistor in volts (V).
        resistance (float): Resistance of the resistor in ohms (Ω).
    
    Returns:
        float: Power dissipated in watts (W).
    """
    current = voltage / resistance
    return voltage * current