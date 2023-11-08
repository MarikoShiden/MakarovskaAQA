import csv
import json


"""class CSVConverter:
    def __init__(self):
        self.__lines = []

    def read_file(self, filename):
        with open(filename, 'r') as csv_file:
            lines = csv.DictReader(csv_file)
            for line in lines:
                self.__lines.append(line)
                print(line)

    def write_file(self, filename):
        with open(filename, 'w') as writer:
            json.dump(self.__lines, writer, indent=4)
            self.cleanup()

    def cleanup(self):
        self.__lines = []


converter = CSVConverter()
converter.read_file('example.csv')
converter.write_file('example.json')"""


class JSONConverter:
    def __init__(self):
        self.__lines = []

    def read_file(self, filename):
        with open(filename, 'r') as json_file:
            lines = json.load(json_file)
            for line in lines:
                self.__lines.append(line)
                print(line)

    def write_file(self, filename):
        with open(filename, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)

            count = 0
            for line in self.__lines:
                if count == 0:
                    header = line.keys()
                    csv_writer.writerow(header)
                    count += 1
                csv_writer.writerow(line.values())

    def cleanup(self):
        self.__lines = []


converter = JSONConverter()
converter.read_file('example.json')
converter.write_file('example.csv')
