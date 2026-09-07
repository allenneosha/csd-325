import csv
from datetime import datetime
import sys
from matplotlib import pyplot as plt

filename = 'sitka_weather_2018_simple.csv'

# This part of the program is loading the data
dates, highs, lows = [], [], []
try:
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # Map index positions based on standard sitka_weather_2018_simple headers
        # Row[2] = Date, Row[5] = TMAX (High), Row[6] = TMIN (Low)
        for row in reader:
            try:
                current_date = datetime.strptime(row[2], '%Y-%m-%d')
                high = int(row[5])
                low = int(row[6])
            except (ValueError, IndexError):
                continue
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)
except FileNotFoundError:
    print(f"\nError: The file '{filename}' was not found.")
    sys.exit()

# This is the interactive menu loop of the program, letting the user know
# what to enter for their selection.
print("--- Weather Data Viewer Initialized ---")
while True:
    print("\n=== Main Menu ===")
    print("1. Type 'highs' to view high temperatures (Red graph)")
    print("2. Type 'lows' to view low temperatures (Blue graph)")
    print("3. Type 'exit' to exit the application")

# User enters their selection in this part of code.

    user_choice = input("Enter your selection: ").strip().lower()

    if user_choice == 'highs':
        print("Generating high temperatures graph...")
        fig, ax = plt.subplots()
        ax.plot(dates, highs, c='red')
        plt.title("Daily High Temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.show()

    elif user_choice == 'lows':
        print("Generating low temperatures graph...")
        fig, ax = plt.subplots()
        ax.plot(dates, lows, c='blue')
        plt.title("Daily Low Temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.show()

    elif user_choice == 'exit':
        print("\nThank you for using the Weather Data Viewer. Exiting program now. Goodbye!")
        sys.exit()

    else:
        print("Invalid input. Please enter 'highs', 'lows', or 'exit'.")