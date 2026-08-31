def calculate_pressure(force, area):
    return force / area


if __name__ == "__main__":
    f = float(input("Enter force (N): "))
    a = float(input("Enter area (m²): "))
    pressure = calculate_pressure(f, a)
    print(f"Pressure = {pressure:.2f} Pa")