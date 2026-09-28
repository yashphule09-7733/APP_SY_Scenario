import csv
import sys

# Check command-line argument
if len(sys.argv) != 2:
    print("Usage: python sports.py sports.csv")
    exit()

filename = sys.argv[1]

# Read CSV file
try:
    with open(filename, "r") as file:
        data = csv.DictReader(file)

        equipment = list(data)

        # Display all equipment
        print("Sports Equipment Details:")
        for e in equipment:
            print(e)

        # Search Equipment ID
        search_id = input("\nEnter Equipment ID to search: ")

        found = False

        for e in equipment:
            if e["Equipment_ID"] == search_id:
                print("\nEquipment Found:")
                print("Equipment ID:", e["Equipment_ID"])
                print("Name:", e["Name"])
                print("Sport:", e["Sport"])
                print("Quantity:", e["Quantity"])
                found = True
                break

        if not found:
            print("Equipment not found.")

except FileNotFoundError:
    print("File not found.")
