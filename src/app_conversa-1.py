import streamlit as st

from carregador_dados import CarregadorDados
from analisador import AnalisadorFinanceiro
from agente import AgenteOrion
from config import OLLAMA_MODEL


def inicializar_estado() -> None:
    if "mensagens" not in st.session_state:
        st.session_state.mensagens = [
            {
                "role": "assistant",
                "content": (
                    "Olá! Eu sou o Orion, seu agente financeiro inteligente.\n\n"
                    "Posso analisar seus dados financeiros e responder perguntas "
                    "sobre saldo, despesas, receitas, planejamento e meta de economia."
                ),
            }
        ]


def main() -> None:
    st.set_page_config(
        page_title="Orion — Agente Financeiro Inteligente",
        page_icon="📊",
        layout="centered",
    )

    st.title("📊 Orion — Agente Financeiro Inteligente")
    st.caption(
        "Converse com o Orion. As respostas são geradas por IA com base "
        "nos dados financeiros carregados localmente."
    )

    try:
        carregador = CarregadorDados()
        dados = carregador.carregar_todos()

        analisador = AnalisadorFinanceiro(
            transacoes=dados["transacoes"],
            planejamento_financeiro=dados["planejamento_financeiro"],
        )

        resumo = analisador.gerar_resumo_financeiro()

        modelo = st.sidebar.text_input("Modelo Ollama", value=OLLAMA_MODEL)

        st.sidebar.markdown("### Exemplos de perguntas")
        st.sidebar.markdown(
            """
- Como está meu saldo atual?
- Minha meta de economia foi atingida?
- Em qual categoria eu gastei mais?
- Estou acima ou abaixo do planejado?
- O que os meus dados mostram sobre meu orçamento?
            """
        )

        inicializar_estado()

        agente = AgenteOrion(
            resumo_financeiro=resumo,
            modelo=modelo,
        )

        for mensagem in st.session_state.mensagens:
            with st.chat_message(mensagem["role"]):
                st.markdown(mensagem["content"])

        pergunta = st.chat_input("Digite sua pergunta para o Orion")

        if pergunta:
            st.session_state.mensagens.append(
                {"role": "user", "content": pergunta}
            )

            with st.chat_message("user"):
                st.markdown(pergunta)

            with st.chat_message("assistant"):
                with st.spinner("O Orion está analisando seus dados..."):
                    resposta = agente.responder(pergunta)
                    st.markdown(resposta)

            st.session_state.mensagens.append(
                {"role": "assistant", "content": resposta}
            )

        if st.sidebar.button("Nova conversa"):
            st.session_state.mensagens = [
                {
                    "role": "assistant",
                    "content": (
                        "Olá! Eu sou o Orion, seu agente financeiro inteligente.\n\n"
                        "Posso analisar seus dados financeiros e responder perguntas "
                        "sobre saldo, despesas, receitas, planejamento e meta de economia."
                    ),
                }
            ]
            st.rerun()

    except Exception as erro:
        st.error(f"Erro ao carregar ou processar os dados: {erro}")


if __name__ == "__main__":
    main()