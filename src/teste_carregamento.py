from carregador_dados import CarregadorDados

carregador = CarregadorDados()
dados = carregador.carregar_todos()

for chave, valor in dados.items():
    print(f"\n--- {chave} ---")
    print(type(valor))

    if hasattr(valor, "head"):
        print(valor.head())
        print("\nTipos de dados:")
        print(valor.dtypes)
    else:
        print(valor)