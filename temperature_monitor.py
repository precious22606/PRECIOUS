def evaluate_thermal_limit(temperature):
    """
    Evaluates a temperature reading and returns a status label.
    Returns 'CRITICAL' if temperature > 85, otherwise 'NORMAL'.
    """
    if temperature > 85:
        return "CRITICAL"
    else:
        return "NORMAL"

if __name__ == "__main__":
    print("Enter temperatures one at a time. Type -999 to quit.")
    
    while True:
        # Get input from user
        entry = float(input("Temperature (°C): "))
        
        # Check for sentinel value to stop the loop
        if entry == -999:
            print("Monitoring session ended.")
            break
        
        # Pass the temperature to the function and get the status
        status = evaluate_thermal_limit(entry)
        
        # Display the result
        print(f"Status: {status}")