voltages = [12.8, 11.4, 12.1, 10.9, 12.7, 11.8, 13.0, 11.2]

good_count = 0
marginal_count = 0
low_count = 0
low_voltages = []

def classify_voltage(voltage):
    if voltage >= 12.5:
        return "GOOD"
    elif voltage >= 11.5:
        return "MARGINAL"
    else:
        return "LOW"

def calculate_average(readings):
    return sum(readings) / len(readings)

for voltage in voltages:
    classification = classify_voltage(voltage)
    if classification == "GOOD":
        good_count += 1
    elif classification == "MARGINAL":
        marginal_count += 1
    else:
        low_count += 1
        low_voltages.append(voltage)

average_voltage = calculate_average(voltages)

print("GOOD:", good_count)
print("MARGINAL:", marginal_count)
print("LOW:", low_count)
print("Low-voltage readings:", low_voltages)
print("Highest voltage:", max(voltages))
print("Lowest voltage:", min(voltages))
print("Average voltage:", average_voltage)
print("12.1 recorded:", 12.1 in voltages)
