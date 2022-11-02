import csv
from inventory_report.reports.complete_report import CompleteReport

from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @classmethod
    def import_data(cls, path: str, type: str):
        with open(path, "r", encoding="utf-8") as file:
            file_reader = csv.DictReader(file)
            prod_list = list(file_reader)
        if type == "simples":
            return SimpleReport.generate(prod_list)
        return CompleteReport.generate(prod_list)
