from typing import Any, Dict

import pandas as pd


class AnalisadorFinanceiro:
    def __init__(
        self,
        transacoes: pd.DataFrame,
        planejamento_financeiro: Dict[str, Any],
    ) -> None:
        self.transacoes = transacoes.copy()
        self.planejamento = planejamento_financeiro

    def calcular_total_receitas(self) -> float:
        receitas = self.transacoes[self.transacoes["tipo"] == "receita"]
        return float(receitas["valor"].sum())

    def calcular_total_despesas(self) -> float:
        despesas = self.transacoes[self.transacoes["tipo"] == "despesa"]
        return float(despesas["valor"].sum())

    def calcular_saldo(self) -> float:
        return self.calcular_total_receitas() - self.calcular_total_despesas()

    def despesas_por_categoria(self) -> pd.Series:
        despesas = self.transacoes[self.transacoes["tipo"] == "despesa"]
        return despesas.groupby("categoria")["valor"].sum().sort_values(ascending=False)

    def comparar_planejado_realizado(self) -> Dict[str, float]:
        receita_planejada = float(self.planejamento.get("receita_planejada", 0.0))
        despesa_planejada = float(self.planejamento.get("despesa_planejada", 0.0))

        receita_realizada = self.calcular_total_receitas()
        despesa_realizada = self.calcular_total_despesas()

        return {
            "receita_planejada": round(receita_planejada, 2),
            "receita_realizada": round(receita_realizada, 2),
            "dif_receita": round(receita_realizada - receita_planejada, 2),
            "despesa_planejada": round(despesa_planejada, 2),
            "despesa_realizada": round(despesa_realizada, 2),
            "dif_despesa": round(despesa_realizada - despesa_planejada, 2),
        }
        
    def avaliar_meta_economia(self) -> Dict[str, Any]:
        meta = float(self.planejamento.get("meta_economia", 0.0))
        saldo_atual = self.calcular_saldo()

        return {
            "meta_economia": round(meta, 2),
            "saldo_atual": round(saldo_atual, 2),
            "meta_atingida": saldo_atual >= meta,
            "diferenca": round(saldo_atual - meta, 2),
        }

    def gerar_resumo_financeiro(self) -> Dict[str, Any]:
        return {
            "total_receitas": self.calcular_total_receitas(),
            "total_despesas": self.calcular_total_despesas(),
            "saldo": self.calcular_saldo(),
            "despesas_por_categoria": self.despesas_por_categoria().to_dict(),
            "planejado_vs_realizado": self.comparar_planejado_realizado(),
            "meta_economia": self.avaliar_meta_economia(),
        }