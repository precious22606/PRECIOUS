def calculate_beam_volume(width, length, height):
    return width * length * height


if __name__ == "__main__":
    w = float(input("Enter width (m): "))
    l = float(input("Enter length (m): "))
    h = float(input("Enter height (m): "))
    volume = calculate_beam_volume(w, l, h)
    print(f"Beam volume = {volume:.3f} m³")