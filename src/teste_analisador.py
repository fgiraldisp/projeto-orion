from carregador_dados import CarregadorDados
from analisador import AnalisadorFinanceiro


carregador = CarregadorDados()
dados = carregador.carregar_todos()

analisador = AnalisadorFinanceiro(
    transacoes=dados["transacoes"],
    planejamento_financeiro=dados["planejamento_financeiro"],
)

resumo = analisador.gerar_resumo_financeiro()

for chave, valor in resumo.items():
    print(f"\n--- {chave} ---")
    print(valor)