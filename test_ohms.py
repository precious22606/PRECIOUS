def calc_power(voltage, current):
	return voltage * current

result = calc_power(12, 6)
print("Power =", result, "watts")

result = calc_power(24, 12)
print("Power =", result, "watts")

print(calc_power.__doc__)