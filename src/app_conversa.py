import streamlit as st

from carregador_dados import CarregadorDados
from analisador import AnalisadorFinanceiro
from agente import AgenteOrion


def formatar_moeda(valor: float) -> str:
    valor_formatado = f"{valor:,.2f}"
    valor_formatado = valor_formatado.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {valor_formatado}"


def responder_pergunta(pergunta: str, resumo: dict, agente: AgenteOrion) -> str:
    pergunta_normalizada = pergunta.strip().lower()

    if not pergunta_normalizada:
        return "Por favor, digite uma pergunta para que eu possa analisar seu orçamento."

    if "saldo" in pergunta_normalizada:
        saldo = resumo["saldo"]
        if saldo >= 0:
            return f"Seu saldo atual está positivo em {formatar_moeda(saldo)}."
        return f"Seu saldo atual está negativo em {formatar_moeda(abs(saldo))}."

    if "receita" in pergunta_normalizada or "ganhei" in pergunta_normalizada:
        return f"O total de receitas no período foi de {formatar_moeda(resumo['total_receitas'])}."

    if "despesa" in pergunta_normalizada or "gastei" in pergunta_normalizada:
        return f"O total de despesas no período foi de {formatar_moeda(resumo['total_despesas'])}."

    if "categoria" in pergunta_normalizada or "gastei mais" in pergunta_normalizada:
        despesas = resumo.get("despesas_por_categoria", {})
        if despesas:
            categoria = max(despesas, key=despesas.get)
            valor = despesas[categoria]
            categoria = categoria.replace("_", " ").capitalize()
            return f"A categoria com maior gasto foi {categoria}, totalizando {formatar_moeda(valor)}."
        return "Não identifiquei despesas por categoria no período analisado."

    if "meta" in pergunta_normalizada or "economia" in pergunta_normalizada:
        meta = resumo["meta_economia"]
        if meta["meta_atingida"]:
            return (
                f"Sua meta de economia foi atingida. "
                f"A diferença positiva foi de {formatar_moeda(meta['diferenca'])}."
            )
        return (
            f"Sua meta de economia ainda não foi atingida. "
            f"Faltam {formatar_moeda(abs(meta['diferenca']))} para alcançá-la."
        )

    if "planejado" in pergunta_normalizada or "orçamento" in pergunta_normalizada:
        planejamento = resumo["planejado_vs_realizado"]
        if planejamento["dif_despesa"] > 0:
            return (
                f"Suas despesas ficaram acima do planejado em "
                f"{formatar_moeda(planejamento['dif_despesa'])}."
            )
        return (
            f"Suas despesas ficaram abaixo do planejado em "
            f"{formatar_moeda(abs(planejamento['dif_despesa']))}."
        )

    return agente.gerar_resposta_textual()


def main() -> None:
    st.set_page_config(
        page_title="Orion — Agente Financeiro Inteligente",
        page_icon="📊",
        layout="centered",
    )

    st.title("📊 Orion — Agente Financeiro Inteligente")
    st.write(
        "Converse com o Orion para entender melhor seu orçamento pessoal "
        "e receber análises em linguagem natural."
    )

    try:
        carregador = CarregadorDados()
        dados = carregador.carregar_todos()

        analisador = AnalisadorFinanceiro(
            transacoes=dados["transacoes"],
            planejamento_financeiro=dados["planejamento_financeiro"],
        )

        resumo = analisador.gerar_resumo_financeiro()
        agente = AgenteOrion(resumo)

        st.subheader("Faça sua pergunta ao Orion")

        pergunta = st.text_input(
            "Digite sua pergunta:",
            placeholder="Ex.: Como está meu saldo? Em que categoria gastei mais?",
        )

        if st.button("Consultar Orion"):
            resposta = responder_pergunta(pergunta, resumo, agente)

            st.subheader("Resposta do Orion")
            st.markdown(resposta)

        with st.expander("Exemplos de perguntas"):
            st.markdown(
                """
- Como está meu saldo?
- Quanto eu gastei no período?
- Em que categoria gastei mais?
- Minha meta de economia foi atingida?
- Estou acima ou abaixo do planejado?
                """
            )

    except Exception as erro:
        st.error(f"Erro ao carregar ou processar os dados: {erro}")


if __name__ == "__main__":
    main()