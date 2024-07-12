import csv
def calculate_average(csv_file, column_index):
    try:
        with open(csv_file, 'r') as file:
            reader = csv.reaader(file)
            column_values = [float(row[column_index]) for row in reader]
    except FileNotFoundError:
        return None
    except (IndexError,ValueError):
        return None
csv_file = 'data.csv'
column_index = 2
average = calculate_average(csv_file, column_index)
if average is not None:
    print(f"Average of column {column_index + 1} in '{csv_file}': {average}")
else:
    print("An error occurred")
