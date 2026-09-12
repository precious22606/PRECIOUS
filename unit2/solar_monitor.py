total = 0
low_count = 0
moderate_count = 0
high_count = 0

for i in range(1, 9):
    power = float(input("Enter power reading " + str(i) + " (W): "))
    total = total + power

    if power < 150:
        print("LOW")
        low_count += 1
    elif power < 300:
        print("MODERATE")
        moderate_count = moderate_count + 1
    else:
        print("HIGH")
        high_count = high_count + 1

print("Total energy:", total, "Wh")
print("LOW readings:", low_count)
print("MODERATE readings:", moderate_count)
print("HIGH readings:", high_count)
print("Average power:", total / 8, "W")