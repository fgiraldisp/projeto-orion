from pathlib import Path
from typing import Any, Dict
import json

import pandas as pd


class CarregadorDados:
    COLUNAS_TRANSACOES = {
        "id",
        "data",
        "tipo",
        "categoria",
        "subcategoria",
        "descricao",
        "valor",
        "forma_pagamento",
    }

    COLUNAS_HISTORICO = {
        "data_hora",
            "usuario",
    "pergunta",
        "resposta",
        "resumo_analise",
    }

    def __init__(self, pasta_dados: str = "data") -> None:
        self.pasta_dados = Path(pasta_dados)

    def _obter_caminho(self, nome_arquivo: str) -> Path:
        caminho = self.pasta_dados / nome_arquivo
        if not caminho.exists():
            raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")
        return caminho

    def carregar_csv(self, nome_arquivo: str) -> pd.DataFrame:
        caminho = self._obter_caminho(nome_arquivo)

        try:
            df = pd.read_csv(caminho)
        except Exception as exc:
            raise ValueError(f"Erro ao ler o arquivo CSV {caminho}: {exc}") from exc

        return df

    def carregar_json(self, nome_arquivo: str) -> Dict[str, Any]:
        caminho = self._obter_caminho(nome_arquivo)

        try:
            with open(caminho, "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
        except Exception as exc:
            raise ValueError(f"Erro ao ler o arquivo JSON {caminho}: {exc}") from exc

        if not isinstance(dados, dict):
            raise TypeError(f"O arquivo JSON {caminho} deve conter um objeto JSON.")

        return dados

    def _validar_colunas(
        self,
        df: pd.DataFrame,
        colunas_obrigatorias: set,
        nome_arquivo: str,
    ) -> None:
        colunas_ausentes = colunas_obrigatorias - set(df.columns)
        if colunas_ausentes:
            raise ValueError(
                f"O arquivo {nome_arquivo} não possui as colunas obrigatórias: "
                f"{sorted(colunas_ausentes)}"
            )

    def carregar_transacoes(self) -> pd.DataFrame:
        df = self.carregar_csv("transacoes.csv")
        self._validar_colunas(df, self.COLUNAS_TRANSACOES, "transacoes.csv")

        df["data"] = pd.to_datetime(df["data"], errors="coerce")
        if df["data"].isna().any():
            raise ValueError("Há datas inválidas em transacoes.csv")

        df["tipo"] = df["tipo"].astype(str).str.strip().str.lower()
        df["categoria"] = df["categoria"].astype(str).str.strip().str.lower()
        df["subcategoria"] = df["subcategoria"].astype(str).str.strip().str.lower()
        df["descricao"] = df["descricao"].astype(str).str.strip()
        df["forma_pagamento"] = df["forma_pagamento"].astype(str).str.strip().str.lower()
        df["valor"] = pd.to_numeric(df["valor"], errors="coerce")

        if df["valor"].isna().any():
            raise ValueError("Há valores inválidos em transacoes.csv")

        return df

    def carregar_historico_interacoes(self) -> pd.DataFrame:
        df = self.carregar_csv("historico_interacoes.csv")
        self._validar_colunas(df, self.COLUNAS_HISTORICO, "historico_interacoes.csv")

        df["data_hora"] = pd.to_datetime(df["data_hora"], errors="coerce")
        if df["data_hora"].isna().any():
            raise ValueError("Há datas/horas inválidas em historico_interacoes.csv")

        return df

    def carregar_perfil_usuario(self) -> Dict[str, Any]:
        return self.carregar_json("perfil_usuario.json")

    def carregar_planejamento_financeiro(self) -> Dict[str, Any]:
        return self.carregar_json("planejamento_financeiro.json")

    def carregar_categorias_financeiras(self) -> Dict[str, Any]:
        return self.carregar_json("categorias_financeiras.json")

    def carregar_todos(self) -> Dict[str, Any]:
        return {
            "transacoes": self.carregar_transacoes(),
            "historico_interacoes": self.carregar_historico_interacoes(),
            "perfil_usuario": self.carregar_perfil_usuario(),
            "planejamento_financeiro": self.carregar_planejamento_financeiro(),
            "categorias_financeiras": self.carregar_categorias_financeiras(),
        }