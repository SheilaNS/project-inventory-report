from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        1,
        "Sheila",
        "Leonor inc.",
        "1984-10-18",
        "2070-10-18",
        "FILHA002",
        "temperatura mínima 24 graus",
    )
    product_report = (
        f"O produto {product.nome_do_produto} "
        f"fabricado em {product.data_de_fabricacao} "
        f"por {product.nome_da_empresa} "
        f"com validade até {product.data_de_validade} "
        f"precisa ser armazenado {product.instrucoes_de_armazenamento}."
    )

    assert repr(product) == product_report
