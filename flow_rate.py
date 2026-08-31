def calculate_flow_rate(volume_liters, time_seconds):
    """Calculate flow rate from volume in litres and time in seconds.

    Parameters:
        volume_liters (float): Volume in litres (L).
        time_seconds (float): Time in seconds (s).

    Returns:
        float: Flow rate in litres per second (L/s).
    """
    return volume_liters / time_seconds


if __name__ == "__main__":
    vol = float(input("Enter volume (L): "))
    t = float(input("Enter time (s): "))
    rate = calculate_flow_rate(vol, t)
    print(f"Flow rate = {rate:.3f} L/s")

    print("\nFunction documentation:")
    print(calculate_flow_rate.__doc__)