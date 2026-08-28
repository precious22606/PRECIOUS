from unit_converter import cm_to_inches, inches_to_cm

def main():
    print("cm to inches:", cm_to_inches(10))
    print("inches to cm:", inches_to_cm(10))

    print("\nDocstring for cm_to_inches:")
    print(cm_to_inches.__doc__)

    print("\nDocstring for inches_to_cm:")
    print(inches_to_cm.__doc__)

if __name__ == "__main__":
    main()