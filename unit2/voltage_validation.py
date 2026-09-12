total = 0
invalid_count = 0
valid_count = 0

for i in range(5):
    while True:
        voltage = float(input("Enter voltage: "))

        if 0 <= voltage<= 15:
            total += voltage
            valid_count += 1
            break
        else:
            invalid_count += 1
            print("Invalid reading. Enter a value between 0 and 15.")

            average= total / valid_count

            print("Average reading:", round(average, 2))
            print("Number of invalid readings:", invalid_count)