from datetime import datetime


class SimpleReport:
    def generate(list_products):
        today = datetime.now().strftime("%Y-%m-%d")
        oldest_fabrication = []
        newest_validity = []
        # referencia da lógica: 
        # https://github.com/tryber/sd-011-inventory-report/pull/100/files
        products_by_company = dict()
        for item in list_products:
            oldest_fabrication.append(item["data_de_fabricacao"])

            if item["data_de_validade"] > today:
                newest_validity.append(item["data_de_validade"])

            if item['nome_da_empresa'] in products_by_company:
                products_by_company[item['nome_da_empresa']] += 1
            else:
                products_by_company[item['nome_da_empresa']] = 1

        return(
          f"Data de fabricação mais antiga: {min(oldest_fabrication)}\n"
          f"Data de validade mais próxima: {min(newest_validity)}\n"
          "Empresa com maior quantidade de produtos "
          f"estocados: {max(products_by_company)}\n"
          )


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

objeto = SimpleReport.generate(test)

print(objeto)
