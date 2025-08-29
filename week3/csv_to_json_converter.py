import csv
import pandas as pd
import json
def create_csv():
    data = [
        ["id", "name", "age", "grade"],
        [1, "Meena", 22, "A"],
        [2, "John", 23, "B"],
        [3, "Pooja", 21, "A+"]
    ]  
    try:
        with open("students.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(data)
        print("CSV file 'students.csv' created successfully!")
    except Exception as e:
        print(f"Error creating CSV file: {e}")
def csv_to_json():
    try:
        csv_file = "students.csv"  # Using the CSV we just created
        data = pd.read_csv(csv_file)
        json_file = "students.json"  # Output JSON file
        json_data = data.to_json(orient='records', indent=4)
        with open(json_file, 'w') as f:
            f.write(json_data)
        print("CSV file 'students.csv' has been successfully converted to JSON 'students.json'.")
    except FileNotFoundError:
        print(" Error: CSV file not found.")
    except pd.errors.EmptyDataError:
        print("Error: CSV file is empty.")
    except pd.errors.ParserError:
        print(" Error: CSV file is corrupted or wrongly formatted.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
create_csv()   # Step 1: create CSV
csv_to_json()  # Step 2: convert to JSON

