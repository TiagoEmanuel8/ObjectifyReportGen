from typing import Counter
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def generate(list_products):
        heir_simple_report = SimpleReport.generate(list_products)

        company_list = [row["nome_da_empresa"] for row in list_products]

        company_counter = Counter(company_list)
        # print(products_counter)
        # print(products_counter.items())

        products_message = "Produtos estocados por empresa: \n"
        for product, count in company_counter.items():
            products_message += f"- {product}: {count}\n"

        return f"{heir_simple_report}\n{products_message}"


test = [
  {
    "id": "1",
    "nome_do_produto": "Nicotine Polacrilex",
    "nome_da_empresa": "Target Corporation",
    "data_de_fabricacao": "2020-02-18",
    "data_de_validade": "2022-03-17",
    "numero_de_serie": "CR25 1551 4467 2549 4402 1",
    "instrucoes_de_armazenamento": "instrucao 1"
  },
  {
    "id": "2",
    "nome_do_produto": "fentanyl citrate",
    "nome_da_empresa": "Target Corporation",
    "data_de_fabricacao": "2019-12-06",
    "data_de_validade": "2022-02-25",
    "numero_de_serie": "FR29 5951 7573 74OY XKGX 6CSG D20",
    "instrucoes_de_armazenamento": "instrucao 2"
  },
  {
    "id": "3",
    "nome_do_produto": "NITROUS OXIDE",
    "nome_da_empresa": "Galena Biopharma",
    "data_de_fabricacao": "2019-12-22",
    "data_de_validade": "2023-11-07",
    "numero_de_serie": "CZ09 8588 0858 8435 9140 2695",
    "instrucoes_de_armazenamento": "instrucao 3"
  }]

objeto = CompleteReport.generate(test)

print(objeto)
