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
## Base de conhecimento

  A base de conhecimento do Orion é composta por arquivos estruturados que armazenam dados do usuário e suas finanças.
  
  |Arquivo| Formato | Função |
  |-------|---------|--------|
  |`transacoes.csv`|CSV|Registra receitas e despesas|
  |`planejamento_financeiro.json`|JSON|Define orçamento planejado|
  |`perfil_usuario.json`|JSON|Contém perfil e objetivos do usuário|
  |`categorias_financeiras.json`|JSON|Padroniza categorias financeiras|
  |`historico_interacoes.csv`|CSV|Armazena interações anteriores|
---
## Funcionalidades

- [x] Cálculo automático de saldo
- [x] Comparação entre planejado e realizado
- [x] Identificação de padrões de consumo
- [x] Geração de insights financeiros
- [x] Recomendações práticas para o uusário
- [x] Interface Interativa com Streamlit
---
## Exemplo de Analise

  - Entrada:
    - Receita: R$ 5.000,00
    - Saída: R$ 625,40
  - Saída dp Orion:
    - Saldo positivo de R$ 4.374,60
    - Nenhuma categoria ultrapassou o orçamento
    - Situação financeira estável
---  
## Segurança e Confiabilidade
  O Orion foi projetado para minimizar erros e alucinações:
  - [x] Utiliza apenas dados fornecidos
  - [x] Não inventa informações
  - [x] Realiza processamento local antes da IA
  - [x] Solicita mais dados quando necessário
  - [x] Não faz recomendações sem contexto
---
## Limitações
  1. Não substitui um consultor financeiro profissional
  2. Não realiza previsões de mercado
  3. Não acessa dados externos em tempo real
  4. Depende da qualidade dos dados fornecidos
---
## Tecnologias Utilizadas
  1. Python
  2. Streamlit
  3. Pandas
  4. JSON/CSV
  5. Ollama(IA local) ou API de modelo de linguagem
---
## Como executar
  - Instalar dependências
    - `pip install - r requirements.txt`
  - Executar aplicação
    - `streamlit run src/app.py`
---
## Autor

  Projeto desenvolvido como parte de estudo em Inteligência Artificial aplicada a finanças.




