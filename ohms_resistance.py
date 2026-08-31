def calc_resistance(voltage, current):
    """
    Calculates electrical resistance using Ohm's Law (R = V / I).
    Returns 0.0 if current is 0 to prevent ZeroDivisionError.
    """
    if current == 0:
        return 0.0
    return voltage / current

if __name__ == "__main__":
    # Test normal case
    r1 = calc_resistance(12, 2)
    print(f"Resistance (12V, 2A) = {r1:.2f} Ω")
    
    # Test zero-current case (defensive check)
    r2 = calc_resistance(12, 0)
    print(f"Resistance (12V, 0A) = {r2:.2f} Ω ← handled safely")