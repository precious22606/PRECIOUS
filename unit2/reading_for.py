total = 0

for i in range(1,6):
    reading = input("Enter reading " + str(i) + ": ")
    print("Reading number:", i)
    voltage = float(reading)

    if voltage < 12.0:
        print("Warning: reading", i, "is low!")
    else:
        print("Reading", i, "acceptable.")

    total = total + voltage

print("Average:", total / 5) 