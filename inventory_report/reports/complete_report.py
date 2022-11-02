from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def __get_prod_qtt(prod_list):
        company_list_str = ""
        company_list = dict()
        for prod in prod_list:
            if prod["nome_da_empresa"] in company_list.keys():
                company_list[prod["nome_da_empresa"]] += 1
            else:
                company_list[prod["nome_da_empresa"]] = 1
        for company_name, company_qtt in company_list.items():
            company_list_str += f"- {company_name}: {company_qtt}\n"
        return company_list_str

    @classmethod
    def generate(cls, products):
        simple_report = super().generate(products)
        prod_qtt = cls.__get_prod_qtt(products)
        return (
            f"{simple_report}\n"
            "Produtos estocados por empresa:\n"
            f"{prod_qtt}"
        )
