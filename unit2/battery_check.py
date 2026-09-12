technician_name = "A. Petersen"
voltage_input = input("Enter the measured voltage (V): ")
voltage = float(voltage_input)
print("Technician:", technician_name)
print(technician_name, "recorded voltage:", voltage)

voltage_input = input("enter the measured voltage: ")
voltage = float(voltage_input)

if voltage > 12.0:
    print("battery status: good")
elif voltage < 11.8:
    print("battery status: marginal")
else:
    print("battery status: low")