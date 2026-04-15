from carregador_dados import CarregadorDados
from analisador import AnalisadorFinanceiro
from agente import AgenteOrion


carregador = CarregadorDados()
dados = carregador.carregar_todos()

analisador = AnalisadorFinanceiro(
    transacoes=dados["transacoes"],
    planejamento_financeiro=dados["planejamento_financeiro"],
)

resumo = analisador.gerar_resumo_financeiro()

agente = AgenteOrion(resumo)
resposta = agente.gerar_resposta_textual()

print(resposta)