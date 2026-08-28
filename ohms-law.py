def calc_resistance(voltage, current):
    """
    Args:
    voltage(float): voltage across thr component in volts (V).
    current9float): current through the component in amperes (A).
Returns:
    float: Resistance in ohms (Ω).
    Notes:
     The function raises a ZeroDivisionError if current is 0.
     """

    return voltage / current