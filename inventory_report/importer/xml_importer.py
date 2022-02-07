import xml.etree.ElementTree as ET

from inventory_report.importer.importer import Importer


# https://www.geeksforgeeks.org/reading-and-writing-xml-files-in-python/
class XmlImporter(Importer):
    def import_data(path):
        with open(path) as file:
            if path.endswith(".xml"):
                tree = ET.parse(file)
                file_root = tree.getroot()
                data = []
                for item in file_root:
                    new_item = {}
                    for index in item:
                        new_item[index.tag] = index.text
                    data.append(new_item)
                return data
            raise ValueError("Arquivo inválido")
