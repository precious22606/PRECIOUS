def build_menu():
    """
    Build and return the menu options.
    """
    options = (
        "calculate resistance",
        "calculate power",
        "convert mm to inches",
        "convert inches to mm",
        "convert cm to inches",
        "convert inches to cm",
        "Exit",
    )

    return options

def display_menu():
    """
    Display the menu options.
    """
    options = build_menu()
    print("Menu:")

    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")