attempts = 0

while True:
    temperature = float(input("Enter temperature:"))

    if temperature == -1:
        print("check cancelled")
        break

    attempts += 1

    if temperature > 40:
        print("Warning: Temperature too high")
    else:
        print(attempts, "attempts")
        print("Equipment may start after", attempts, "attempts")
        break