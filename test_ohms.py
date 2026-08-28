def calc_resistance(voltage, current):
	"""Calculate resistance using Ohm's law: R = V / I."""
	return voltage / current

result = calc_resistance(9, 0.03)
print("Resistance =", result,  "ohms")