import csv

from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    def import_data(path):
        with open(path) as file:
            if path.endswith(".csv"):
                data = list(csv.DictReader(file))
                return data
            raise ValueError("Arquivo inválido")
