# 📊 Orion — Agente Financeiro Inteligente

## 🧠 Descrição

Esta pasta contém o código fonte do **Orion**, desenvolvido para análise de orçamento pessoal com suporte a processamento local em Python e geração de respostas em linguagem natural. Ele é um agente financeiro inteligente desenvolvido para auxiliar no controle e análise de orçamento pessoal, transforando dados de receitas, despesas e planejamento financeiro em **insights claros, objetivos e acionáveis**, permitindo ao usuário tomar decisões financeiras mais conscientes.

---

## 🎯 Objetivo

O objetivo do Orion é resolver a dificuldade que muitos usuários têm em:

- interpretar seus dados financeiros  
- comparar valores planejados com realizados  
- identificar padrões de consumo  
- tomar decisões financeiras práticas  

O agente atua como um **analista financeiro pessoal automatizado**, focado em clareza e eficiência.

---

## ⚙️ Arquitetura

O Orion utiliza uma abordagem híbrida:

### 📊 Processamento local em Python

- cálculo de saldo  
- análise de despesas  
- comparação com planejamento  

### 🤖 Modelo de linguagem (IA)

- geração de explicações  
- recomendações em linguagem natural  

Essa arquitetura reduz custo, melhora performance e aumenta a confiabilidade das respostas.

---

## 📁 Estrutura do Projeto

```bash
.
├── data/                 # Base de conhecimento (JSON e CSV)
├── src/                  # Código da aplicação
│   ├── app.py
│   ├── agente.py
│   ├── analisador.py
│   ├── carregador_dados.py
│   └── config.py
├── requirements.txt
```
---
## Descrição dos Arquivos

- ***app.py***
  Responsável por executar a interface do Orion em Streamlit, permitindo interação com o usuário.
- ***agente.py***
  Contém a lógica de comunicação com o modelo de linguagem e a montagem das respostas do agente.
- ***analisador.py***
  Implementa a análise financeira local, incluindo cálculo de saldo, comparação entre planejado e realizado e geração de insights.
- ***carregador_dados.py***
  Faz a leitura dos arquivos da pasta data, como `transacoes.csv`, `perfil_usuario.json` e `planejamento_financeiro.json`.
- ***config.py***
  Centraliza configurações como nome do agente, caminhos dos arquivos e possíveis parâmetros do modelo.
- ***requirements.txt***
  Lista as bibliotecas necessárias para execução do projeto.
---
## Exemplo de `requirenents.txt`
  - `streamlit`
  - `pandas`
  - `python-dotenv`
  - `requests`
---
## Como rodar

 - Instalar dependências
    - `pip install -> requirements.txt`
 - Executar a aplicação
    - `streamlit run src/app.py`
---
    

