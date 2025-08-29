import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import csv
# Step 1: Create a sample CSV file
def create_sample_csv():
    data = [
        ["id", "name", "age", "grade", "marks"],
        [1, "Meena", 22, "A", 95],
        [2, "John", 23, "B", 85],
        [3, "Pooja", 21, "A+", 98],
        [4, "Alex", 22, "B", 80],
        [5, "Sara", 23, "A", 90]
    ]
    try:
        with open("students.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(data)
        print("Sample CSV file 'students.csv' created successfully!")
    except Exception as e:
        print(f"Error creating CSV file: {e}")
# Step 2: Interactive Data Visualizer
def interactive_visualizer():
    try:
        csv_file = "students.csv"
        data = pd.read_csv(csv_file)
        print("\nHere is a preview of your data:")
        print(data.head())
        print("\nColumns available for visualization:")
        print(list(data.columns))
        # Ask user which column for X and Y axis
        x_col = input("Enter the column name for X-axis: ")
        y_col = input("Enter the column name for Y-axis: ")
        # Ask user for chart type
        print("\nSelect chart type:")
        print("1. Bar Chart")
        print("2. Line Chart")
        print("3. Pie Chart (Y-axis column only)")
        choice = input("Enter choice (1/2/3): ")
        if choice == "1":
            plt.figure(figsize=(8,5))
            sns.barplot(x=x_col, y=y_col, data=data, palette="viridis")
            plt.title(f"{y_col} vs {x_col} (Bar Chart)")
            plt.show()
        elif choice == "2":
            plt.figure(figsize=(8,5))
            sns.lineplot(x=x_col, y=y_col, data=data, marker="o")
            plt.title(f"{y_col} vs {x_col} (Line Chart)")
            plt.show()
        elif choice == "3":
            # Pie chart only makes sense for Y-axis values
            plt.figure(figsize=(6,6))
            pie_data = data[y_col].value_counts()
            plt.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%',
                    colors=sns.color_palette('pastel'))
            plt.title(f"{y_col} Distribution (Pie Chart)")
            plt.show()
        else:
            print("Invalid chart choice.")
    except FileNotFoundError:
        print("CSV file not found.")
    except KeyError:
        print("Column not found in CSV.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the project
create_sample_csv()         # Create CSV
interactive_visualizer()    # Visualize data interactively

