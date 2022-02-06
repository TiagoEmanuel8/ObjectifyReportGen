from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
# from  ..reports.simple_report import SimpleReport
import csv
import json
import xml.etree.ElementTree as ET


def csv_file(file_path):
    list_report = []
    if file_path.endswith('csv'):
        with open(file_path, "r", encoding="utf8") as file:
            jobs_result = csv.DictReader(file, delimiter=",")
            for row in jobs_result:
                list_report.append(row)
    return list_report


def json_file(file_path):
    list_report = []
    if file_path.endswith('json'):
        with open(file_path) as file:
            content = file.read()
            list_report = json.loads(content)
    return list_report


# referencia de código:
# https://github.com/tryber/sd-011-inventory-report/pull/100/files#diff
# -38906d25b4c36219f93f3eef13fb393577eda7c68fdce22fb74e7902712b0920
def xml_file(file_path):
    list_report = []
    with open(file_path) as file:
        xml_tree = ET.parse(file)
        root = xml_tree.getroot()
        for record in root:
            entry = {}
            for attribute in record:
                entry[attribute.tag] = attribute.text
            list_report.append(entry)
    return list_report


class Inventory:
    def import_data(file_path, type_report):
        file = file_path.split('.')
        file_extension = file[-1]

        report_archive = list()

        if file_extension == 'csv':
            report_archive = csv_file(file_path)

        if file_extension == 'json':
            report_archive = json_file(file_path)

        if file_extension == 'xml':
            report_archive = xml_file(file_path)

        if type_report == 'completo':
            return CompleteReport.generate(report_archive)
        else:
            return SimpleReport.generate(report_archive)


# report = Inventory.import_data('inventory_report/data/inventory.csv',
#                                    'completo')

# print(report)
