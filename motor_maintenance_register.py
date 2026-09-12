# Exercise 2: Motor maintenance register

# A dictionary is appropriate because each motor has a unique ID
# and labelled information such as location, temperature, and status.
# Lists are appropriate for storing multiple fault codes for each motor.
# A set is appropriate for storing unique fault codes without duplicates.

motors = {
    "M-101": {
        "location": "Workshop A",
        "rated_power_kw": 5.5,
        "temperature": 72,
        "status": "RUNNING",
        "fault_codes": ["F01", "F03", "F01"]
    },

    "M-102": {
        "location": "Workshop B",
        "rated_power_kw": 7.5,
        "temperature": 88,
        "status": "RUNNING",
        "fault_codes": ["F07", "F03"]
    },

    "M-103": {
        "location": "Pump Station",
        "rated_power_kw": 11.0,
        "temperature": 79,
        "status": "SERVICE REQUIRED",
        "fault_codes": ["F12", "F07"]
    }
}

# 1. Display the complete record for M-102
print("Complete record for M-102:")
print(motors["M-102"])

# 2. Update M-102 status to OVERHEAT
motors["M-102"]["status"] = "OVERHEAT"
print("Updated M-102 status:", motors["M-102"]["status"])

# 3. Display ID, location, temperature and status for every motor
print("\nMotor information:")

for motor_id, motor in motors.items():
    print(
        motor_id,
        "| Location:", motor["location"],
        "| Temperature:", motor["temperature"], "°C",
        "| Status:", motor["status"]
    )

# 4. Count motors above 85 °C
overheated_count = 0

for motor in motors.values():
    if motor["temperature"] > 85:
        overheated_count = overheated_count + 1

print("\nMotors above 85 °C:", overheated_count)

# 5. Combine all fault codes into one set of unique codes
unique_faults = set()

for motor in motors.values():
    unique_faults.update(motor["fault_codes"])

# 6. Display unique fault codes and number of unique codes
print("Unique fault codes:", unique_faults)
print("Number of unique faults:", len(unique_faults))