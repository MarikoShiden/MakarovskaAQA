import os
import xml.etree.ElementTree as ET


class XMLProcessor:
    def __init__(self, xml_file=None):
        self.tree = None
        if xml_file:
            self.load_from_file(xml_file)

    def load_from_file(self, xml_file):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        xml_path = os.path.join(current_directory, xml_file)

        self.tree = ET.parse(xml_path)

    def convert_to_string(self):
        if self.tree is not None:
            return ET.tostring(self.tree.getroot(), encoding='utf8').decode('utf-8')
        else:
            return "XML not loaded."

    def update_element(self, xml_file):
        btmn = self.tree.find(".//movie[@title='Batman Returns']")

        if btmn is not None:
            btmn.attrib["title"] = "Batman vs. Superman"
            self.tree.write(xml_file, encoding='utf-8', xml_declaration=True)
        else:
            raise Exception("Movie 'Batman Returns' not found.")

        for movie in self.tree.iter('movie'):
            print(movie.attrib)


xml_processor = XMLProcessor(xml_file='movies.xml')

# Convert xml file to string
xml_string = xml_processor.convert_to_string()
print("XML to String:")
print(xml_string)

# Append new element
print("\nPerforming Operations:")
xml_processor.update_element(xml_file='movies.xml')
