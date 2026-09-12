voltage = float(input("Enter battery voltage: "))

if voltage > 12.5:
    print("GOOD")
elif voltage >= 11.5:
    print("MARGINAL")
else:
    print("LOW")