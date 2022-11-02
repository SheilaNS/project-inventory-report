from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        1,
        "Sheila",
        "Leonor inc.",
        "1984-10-18",
        "2070-10-18",
        "FILHA002",
        "temperatura mínima 24 graus",
    )

    assert product.id == 1
    assert product.nome_do_produto == "Sheila"
    assert product.nome_da_empresa == "AGA Tecnologia"
    assert product.data_de_fabricacao == "1984-10-18"
    assert product.data_de_validade == "2070-10-18"
    assert product.numero_de_serie == "FILHA002"
    assert product.instrucoes_de_armazenamento == "temperatura mínima 24 graus"
