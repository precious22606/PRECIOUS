voltages = [12.8, 11.4, 12.1, 10.9, 12.7, 11.8, 13.0, 11.2]

good_count = 0
marginal_count = 0
low_count = 0
low_voltages = []
reading_number = 1

for voltage in voltages:
    print("Reading", reading_number, ":", voltage, "V")
    if voltage > 12.5:
        print("GOOD")
        good_count +=1
    elif voltage>= 11.5:
        print("MARGINAL")
        marginal_count +=1
    else:
        print("LOW")
        low_count +=1
        low_voltages.append(voltages)

    reading_number +=1

total_voltage = sum(voltages)
average_voltage = total_voltage / len(voltages)
highest_voltage = max(voltages)
lowest_voltages = min(voltages)

print("\n-----battery dataset report-----")
print("GOOD:", good_count)
print("MARGINAL:", marginal_count)
print("LOW:", low_count)

    #search for the required value
if 12.1 in voltages:
        print("12.1 V was recorded")
else:
        print("12.1 was not recorded")