from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
# from  ..reports.simple_report import SimpleReport
import csv
import json
import xml.etree.ElementTree as ET

class Inventory:
    def import_data(file_path, type_report):
        list_report = []
        if file_path.endswith('csv'):
            with open(file_path, "r", encoding="utf8") as file:
                jobs_result = csv.DictReader(file, delimiter=",")
                for row in jobs_result:
                    list_report.append(row)
        if file_path.endswith('json'):
            with open(file_path) as file:
                content = file.read()
                list_report = json.loads(content)
        if file_path.endswith('xml'):
            #referencia de código:
            #https://github.com/tryber/sd-011-inventory-report/pull/100/files#diff-38906d25b4c36219f93f3eef13fb393577eda7c68fdce22fb74e7902712b0920
            with open(file_path) as file:
                xml_tree = ET.parse(file)
                root = xml_tree.getroot()
                for record in root:
                    entry = {}
                    for attribute in record:
                        entry[attribute.tag] = attribute.text
                    list_report.append(entry)
        if type_report == 'completo':
            return CompleteReport.generate(list_report)
        else:
            return SimpleReport.generate(list_report)


# report = Inventory.import_data('inventory_report/data/inventory.csv',
#                                    'completo')

# print(report)
