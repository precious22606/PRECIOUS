def convert_mm_to_inch(millimetres):
    return millimetres / 25.4


if __name__ == "__main__":
    mm = float(input("Enter length in millimetres: "))
    converted_dimension = convert_mm_to_inch(mm)
    print(f"Converted length = {converted_dimension:.4f} inches")