def calc_current(voltage, resistance):
    """
    calculate the current using I = V/ R

    Parameters:
    voltage(float): voltage across the resistor in volts
    resistance(float): resistance in ohms

    Returns:
    float: current in amperes
    """

    current = voltage / resistance
    return current

def calc_power(voltage, resistance):
    """
    calculate power dissipated in a resistor usiing P = V* I

    Parameters:
    voltage(float): voltage across the resistor in volts
    resistance(float): resistance in ohms

    Returns:
    float: power in watts
    """

    current = calc_current(voltage, resistance)
    power = voltage * current
    return power


if __name__ == "__main__":
    power = calc_power(1, 5)
    print(calc_power.__doc__)