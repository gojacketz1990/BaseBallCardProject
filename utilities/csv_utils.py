import csv

def read_csv(file_path):
    """
    Reads a CSV file and returns a list of dictionaries where each dictionary represents a row.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        List[Dict]: List of rows as dictionaries with column names as keys.
    """
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        return [row for row in csv_reader]
