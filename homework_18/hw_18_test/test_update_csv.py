import csv

from homework_18.hw_18_test.hw_18_2 import add_row_to_csv
from homework_18.hw_18_test.hw_18_2 import delete_row_from_csv


class TestUpdateCSV:
    def test_add(self):
        add_row_to_csv('example.csv', ['Test', 'Name', '666'])
        with open('example.csv', 'r', newline='') as csv_file:
            csv_reader = csv.reader(csv_file)
            rows = list(csv_reader)
            assert ['Test', 'Name', '666'] in rows

    def test_remove(self):
        delete_row_from_csv('example.csv', ['Test', 'Name', '666'])
        with open('example.csv', 'r', newline='') as csv_file:
            csv_reader = csv.reader(csv_file)
            rows = list(csv_reader)
            assert ['Test', 'Name', '666'] not in rows
