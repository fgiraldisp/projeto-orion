import os
import json
from typing import Any, Dict

from dotenv import load_dotenv
from openai import OpenAI

from config import SYSTEM_PROMPT_PATH, OPENAI_MODEL


load_dotenv()


class AgenteOrion:
    def __init__(
        self,
        resumo_financeiro: Dict[str, Any],
        modelo: str = OPENAI_MODEL,
    ) -> None:
        self.resumo = resumo_financeiro
        self.modelo = modelo
        self.system_prompt = self._carregar_system_prompt()

        self.api_key = os.getenv("OPENAI_API_KEY", "").strip()
        if not self.api_key:
            raise ValueError("A variável de ambiente OPENAI_API_KEY não foi definida.")

        self.client = OpenAI(api_key=self.api_key)

    def _carregar_system_prompt(self) -> str:
        with open(SYSTEM_PROMPT_PATH, "r", encoding="utf-8") as arquivo:
            return arquivo.read().strip()

    def _formatar_valores(self, valor: Any) -> Any:
        if isinstance(valor, float):
            return round(valor, 2)

        if isinstance(valor, dict):
            return {
                chave: self._formatar_valores(valor_item)
                for chave, valor_item in valor.items()
            }

        if isinstance(valor, list):
            return [self._formatar_valores(item) for item in valor]

        return valor

    def _montar_contexto(self) -> str:
        resumo_tratado = self._formatar_valores(self.resumo)

        return (
            "Contexto financeiro do usuário:\n"
            f"{json.dumps(resumo_tratado, ensure_ascii=False, indent=2)}"
        )

    def responder(self, pergunta: str) -> str:
        pergunta = pergunta.strip()

        if not pergunta:
            return "Por favor, digite uma pergunta para que eu possa responder."

        mensagem_usuario = (
            f"{self._montar_contexto()}\n\n"
            f"Pergunta do usuário: {pergunta}"
        )

        try:
            resposta = self.client.responses.create(
                model=self.modelo,
                input=[
                    {
                        "role": "system",
                        "content": self.system_prompt,
                    },
                    {
                        "role": "user",
                        "content": mensagem_usuario,
                    },
                ],
            )

            return resposta.output_text.strip()

        except Exception as exc:
            return (
                "Erro ao consultar a API da OpenAI.\n\n"
                f"Detalhes técnicos: {exc}"
            )