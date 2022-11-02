class SimpleReport:
    def __get_oldest_manufacturing(prod_list):
        return min([prod["data_de_fabricacao"] for prod in prod_list])

    def __get_closest_validate(prod_list):
        return min([prod["data_de_validade"] for prod in prod_list])

    def __get_company(prod_list):
        company_list = dict()
        for prod in prod_list:
            if prod["nome_da_empresa"] in company_list.keys():
                company_list[prod["nome_da_empresa"]] += 1
            else:
                company_list[prod["nome_da_empresa"]] = 1
        return max(company_list, key=company_list.get)

    @classmethod
    def generate(cls, products):
        oldest_manufacturing = cls.__get_oldest_manufacturing(products)
        closest_validate = cls.__get_closest_validate(products)
        company = cls.__get_company(products)
        return (
            f"Data de fabricação mais antiga: {oldest_manufacturing}\n"
            f"Data de validade mais próxima: {closest_validate}\n"
            f"Empresa com mais produtos: {company}"
        )
