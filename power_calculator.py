def get_circuit_voltage(current, resistance):
    """
    Calculates voltage using Ohm's Law: V = I * R.
    Parameters:
        current (float): Current in Amperes (A)
        resistance (float): Resistance in Ohms (Ω)
    Returns:
        float: Voltage in Volts (V)
    """
    return current * resistance

def calculate_system_power(current, resistance):
    """
    Calculates power dissipation: P = V * I.
    Since V is not given, it calls get_circuit_voltage() to derive it first.
    Parameters:
        current (float): Current in Amperes (A)
        resistance (float): Resistance in Ohms (Ω)
    Returns:
        float: Power in Watts (W)
    """
    # Call the helper function to get voltage
    voltage = get_circuit_voltage(current, resistance)
    
    # Calculate power using the derived voltage
    power = voltage * current
    
    return power

if __name__ == "__main__":
    # Get user input
    i = float(input("Enter current (A): "))
    r = float(input("Enter resistance (Ω): "))
    
    # Calculate power using the pipeline
    power = calculate_system_power(i, r)
    
    # Display result
    print(f"System power = {power:.2f} W")