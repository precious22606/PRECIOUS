reentries = 0

pressure = float(input("Enter pressure (bar): "))
print("Pressure is out of range.")
pressure = float(input("Enter pressure again (bar): "))
reentries = reentries + 1

temperature = float(input("Enter temperature (celsius): "))

while temperature >= 80:
    print("Temperature is too high.")
    temperature = float(input("Enter temperature again (celsius): "))
    reentries = reentries + 1

    fault_code = int(input("Enter fault code (0 = no fault): "))

    while fault_code != 0:
        print("Fault code detected.")
        fault_code = int(input("Enter fault code again (0 = no fault): "))
        reentries = reentries + 1

    print("Pump checks passes. Pump may start.")
print("Total re-entries:", reentries)  