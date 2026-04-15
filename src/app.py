import os
import streamlit as st
from dotenv import load_dotenv

from carregador_dados import CarregadorDados
from analisador import AnalisadorFinanceiro
from agente import AgenteOrion
from config import OPENAI_MODEL


load_dotenv()

load_dotenv()

api_key_disponivel = bool(os.getenv("OPENAI_API_KEY", "").strip())

MENSAGEM_INICIAL = (
    "Olá! Eu sou o Orion, seu agente financeiro inteligente.\n\n"
    "Posso analisar seus dados financeiros e responder perguntas "
    "sobre saldo, despesas, receitas, planejamento e meta de economia."
)


def inicializar_estado() -> None:
    if "mensagens" not in st.session_state:
        st.session_state.mensagens = [
            {
                "role": "assistant",
                "content": MENSAGEM_INICIAL,
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

    inicializar_estado()

    api_key = os.getenv("OPENAI_API_KEY", "").strip()
    api_key_disponivel = bool(api_key)

    if not api_key_disponivel:
        st.warning(
            "A chave da API da OpenAI não foi encontrada. "
            "A interface foi carregada, mas o Orion não conseguirá responder "
            "até que OPENAI_API_KEY seja definida no arquivo .env."
        )

    st.sidebar.markdown("### Configuração")
    st.sidebar.text_input("Modelo OpenAI", value=OPENAI_MODEL, disabled=True)

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

    try:
        carregador = CarregadorDados()
        dados = carregador.carregar_todos()

        analisador = AnalisadorFinanceiro(
            transacoes=dados["transacoes"],
            planejamento_financeiro=dados["planejamento_financeiro"],
        )

        resumo = analisador.gerar_resumo_financeiro()

    except Exception as erro:
        st.error(f"Erro ao carregar ou processar os dados locais: {erro}")
        return

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
            if not api_key_disponivel:
                resposta = (
                    "Não consigo responder porque a chave da API da OpenAI "
                    "não está configurada no arquivo .env."
                )
                st.markdown(resposta)
            else:
                try:
                    agente = AgenteOrion(
                        resumo_financeiro=resumo,
                        modelo=OPENAI_MODEL,
                    )

                    with st.spinner("O Orion está analisando seus dados..."):
                        resposta = agente.responder(pergunta)

                    st.markdown(resposta)

                except Exception as erro:
                    resposta = f"Erro ao inicializar ou consultar o agente: {erro}"
                    st.markdown(resposta)

        st.session_state.mensagens.append(
            {"role": "assistant", "content": resposta}
        )

    if st.sidebar.button("Nova conversa"):
        st.session_state.mensagens = [
            {
                "role": "assistant",
                "content": MENSAGEM_INICIAL,
            }
        ]
        st.rerun()


if __name__ == "__main__":
    main()