import random
import importlib

try:
    tabulate = importlib.import_module("tabulate").tabulate
except ModuleNotFoundError:
    def tabulate(rows, headers=None, tablefmt=None):
        if not rows:
            return ""

        if headers is None:
            headers = []

        data_rows = [[str(cell) for cell in row] for row in rows]
        header_row = [str(header) for header in headers]

        column_count = max(len(row) for row in data_rows)
        if header_row:
            column_count = max(column_count, len(header_row))

        widths = [0] * column_count
        for row in data_rows:
            for index, value in enumerate(row):
                widths[index] = max(widths[index], len(value))
        for index, value in enumerate(header_row):
            widths[index] = max(widths[index], len(value))

        def format_row(row):
            padded = []
            for index, value in enumerate(row):
                padded.append(str(value).ljust(widths[index]))
            while len(padded) < column_count:
                padded.append("".ljust(widths[len(padded)] if len(padded) < len(widths) else 0))
            return " | ".join(padded)

        lines = []
        if header_row:
            lines.append(format_row(header_row))
            lines.append("-+-".join("-" * width for width in widths))
        for row in data_rows:
            while len(row) < column_count:
                row = row + [""]
            lines.append(format_row(row))
        return "\n".join(lines)

# Dictionary: stores each component ID and its measured voltage.
components = {
    "ECU-101": 4.96,
    "ECU-102": 5.08,
    "ECU-103": 4.88,
    "ECU-104": 5.02,
    "ECU-105": 5.15,
    "ECU-106": 4.99,
    "ECU-107": 4.91,
    "ECU-108": 5.05
}

# Tuple: stores the fixed minimum and maximum permitted voltage.
voltage_tolerance = (4.90, 5.10)

# Makes the random selection repeatable.
random.seed(42)

# Randomly select four different component IDs.
selected_components = random.sample(list(components.keys()), 4)

# Tuple unpacking stores the minimum and maximum voltage.
minimum_voltage, maximum_voltage = voltage_tolerance

# List: stores the inspection results for the table.
inspection_rows = []

# Set: stores failed component IDs without duplicates.
failed_components = set()

pass_count = 0
fail_count = 0
total_voltage = 0

for component_id in selected_components:
    voltage = components[component_id]

    if minimum_voltage <= voltage <= maximum_voltage:
        result = "PASS"
        pass_count += 1
    else:
        result = "FAIL"
        fail_count += 1
        failed_components.add(component_id)

    inspection_rows.append([component_id, voltage, result])
    total_voltage += voltage

# Display the inspection rows using tabulate.
print("\n--- Component Inspection Results ---")
print(tabulate(
    inspection_rows,
    headers=["Component ID", "Voltage (V)", "Result"],
    tablefmt="grid"
))

# Calculate the average voltage.
average_voltage = total_voltage / len(selected_components)

print("\nAverage voltage:", round(average_voltage, 2), "V")
print("PASS:", pass_count)
print("FAIL:", fail_count)
print("Failed components:", failed_components)

# Dictionary: connects component IDs to measured voltages.
# Tuple: stores fixed voltage tolerance limits.
# List: stores inspection results in rows.
# Set: stores failed component IDs uniquely.
# Virtual environment: isolates packages such as tabulate.