def execute_advanced_conversion(value_mm, target_unit="in"):
    """
    Converts millimetres to either inches or centimetres.
    Default target_unit is "in" for backward compatibility.
    """
    if target_unit == "cm":
        return value_mm / 10.0
    else:
        # Default to inches for "in" or any other value
        return value_mm / 25.4

if __name__ == "__main__":
    # Get input
    mm = float(input("Enter length in millimetres: "))
    
    # Test 1: Default conversion (inches)
    inches = execute_advanced_conversion(mm)
    print(f"{mm} mm = {inches:.4f} inches (default)")
    
    # Test 2: Explicit centimeter conversion
    cm = execute_advanced_conversion(mm, target_unit="cm")
    print(f"{mm} mm = {cm:.4f} cm")