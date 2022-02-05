from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
# from  ..reports.simple_report import SimpleReport
import csv

class Inventory:
    def import_data(file_path, type_report):
        list_report= []
        with open(file_path, "r", encoding="utf8") as file:
            jobs_result = csv.DictReader(file, delimiter=",")
            for row in jobs_result:
                list_report.append(row)
        if type_report == 'completo':
            return CompleteReport.generate(list_report)
        else:
            return SimpleReport.generate(list_report)


# report = Inventory.import_data('inventory_report/data/inventory.csv',
#                                    'completo')

# print(report)