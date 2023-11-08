import csv
from homework_18.hw_18_1 import JSONConverter


def add_row_to_csv(filename, row_data):
    with open(filename, 'a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(row_data)


def delete_row_from_csv(filename, row_data):
    with open(filename, 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        rows = list(csv_reader)

    new_rows = [row for row in rows if row != row_data]

    with open(filename, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(new_rows)


converter = JSONConverter()
converter.read_file('example.json')
converter.write_file('example.csv')
