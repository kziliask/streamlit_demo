import csv
import random
import math


def generate_sale_amount(hour):
    """
    Returns a random sale amount based on the hour,
    simulating busier midday/early evening and quieter early morning/late night.
    """
    # Base amounts by time of day (rough pattern)
    # We'll use a sine-like wave just for demonstration, and add some randomness
    # Scale: 6:00 -> lower, 12:00 -> higher, 18:00 -> higher, etc.

    # Convert hour to radians for a sine function
    # For a rough day pattern, let's shift so peak is around midday and early evening
    amplitude = 5.0  # how "tall" the wave is
    midpoint = 5.0  # baseline
    # We'll create a wave that peaks around 13:00 and 19:00 (just for demonstration)
    # A quick trick: sin( (hour-13)*something ) + sin( (hour-19)*something ) ...

    wave = (
        math.sin((hour - 13) * math.pi / 6)  # peak around hour=13
        + math.sin((hour - 19) * math.pi / 6)
    )  # another peak around hour=19

    base_sale = midpoint + amplitude * wave

    # Add random noise
    return round(random.uniform(base_sale - 1.5, base_sale + 1.5), 2)


def generate_random_time():
    """
    Generate a random time between 06:00 and 22:59 (24-hour format).
    Returns a string HH:MM.
    """
    hour = random.randint(6, 22)
    minute = random.randint(0, 59)
    return f"{hour:02d}:{minute:02d}"


def generate_flavor():
    """
    Randomly select one of three flavors.
    """
    flavors = ["chocolate", "butterfinger", "pineapple"]
    return random.choice(flavors)


def generate_frozen_yogurt_data(filename="frozen_yogurt_sales.csv", num_rows=100):
    """
    Generates a CSV file with the specified number of rows of fake frozen yogurt sales data.
    Each row includes:
      - time in 24-hour format (HH:MM)
      - sale_amount (float)
      - flavor (string)
    """
    with open(filename, mode="w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        # Write header
        writer.writerow(["time", "sale_amount", "flavor"])

        # We can generate times either randomly or by sorting them to simulate a timeline
        # Here, we'll generate them randomly but keep them in ascending order
        rows = []

        for _ in range(num_rows):
            time_str = generate_random_time()

            # Extract the hour (integer) from the time_str
            hour = int(time_str.split(":")[0])
            sale_amount = generate_sale_amount(hour)
            flavor = generate_flavor()

            rows.append((time_str, sale_amount, flavor))

        # Sort by time (optional, to make data go in chronological order)
        def time_key(row):
            h, m = row[0].split(":")
            return int(h) * 60 + int(m)

        rows.sort(key=time_key)

        # Write data rows
        for row in rows:
            writer.writerow(row)


# Example usage:
if __name__ == "__main__":
    generate_frozen_yogurt_data(filename="frozen_yogurt_sales_1.csv", num_rows=120)
    print("CSV file 'frozen_yogurt_sales.csv' generated!")
