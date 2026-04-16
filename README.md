# 📊 Orion — Agente Financeiro Inteligente

## 🧠 Visão Geral

O **Orion** é um agente financeiro inteligente desenvolvido para analisar dados de orçamento pessoal e transformar informações financeiras em **insights claros, objetivos e acionáveis**.

O projeto combina:

- **processamento local em Python** para cálculo e consolidação dos dados
- **modelo de linguagem** para interpretar os resultados e gerar respostas em linguagem natural
- **interface interativa em Streamlit** para consulta via chat e visualização dos resultados

O objetivo é oferecer uma experiência de análise financeira assistida, com foco em clareza, confiabilidade e organização arquitetural.

---

## 🎯 Objetivo do Projeto

O Orion foi criado para ajudar o usuário a:

- interpretar receitas e despesas
- comparar valores planejados com valores realizados
- identificar padrões de consumo
- avaliar saldo e metas financeiras
- receber explicações e recomendações com apoio de IA

Na prática, o Orion atua como um **analista financeiro pessoal automatizado**, utilizando dados estruturados como base para gerar respostas contextualizadas.

---

## ⚙️ Arquitetura

O projeto adota uma arquitetura híbrida, separando claramente as responsabilidades do sistema.

### 📊 Processamento local em Python

A camada local é responsável por:

- leitura dos arquivos de dados
- validação da estrutura dos dados
- cálculo de saldo
- consolidação de receitas e despesas
- comparação entre planejado e realizado
- geração do resumo financeiro base

### 🤖 Camada de IA

A IA é utilizada para:

- interpretar os resultados calculados localmente
- explicar a situação financeira em linguagem natural
- sugerir recomendações com base no contexto recebido

### 🖥️ Interface

A interface é construída com **Streamlit** e permite:

- exibição dos dados processados
- interação em formato de chat
- apresentação da análise final do agente

---

## 🧩 Decisões Técnicas Importantes

Durante o desenvolvimento, algumas decisões arquiteturais se mostraram fundamentais:

- o cálculo financeiro é feito localmente, sem depender da IA
- a IA não é responsável pela lógica de negócio
- a aplicação controla a renderização da resposta final
- a estratégia evoluiu de **texto livre** para **saída estruturada**
- a abordagem mais confiável é baseada em **JSON estruturado + renderização controlada**

### Por que isso foi importante?

Respostas em texto livre geradas por modelos de linguagem podem apresentar problemas como:

- quebras indevidas de linha
- números fragmentados
- palavras coladas
- markdown inconsistente

Por isso, o projeto passou a priorizar uma estrutura em que:

1. a análise financeira é gerada localmente
2. a IA retorna conteúdo estruturado
3. a aplicação interpreta e renderiza o resultado de forma controlada

Essa abordagem reduz falhas visuais e aumenta a robustez do sistema.

---

## 📁 Estrutura do Projeto

```bash
.
├── data/                        # Arquivos de entrada do projeto (CSV e JSON)
├── src/                         # Código-fonte da aplicação
│   ├── app.py                   # Interface principal em Streamlit
│   ├── agente.py                # Integração com o modelo de linguagem
│   ├── analisador.py            # Processamento e análise dos dados financeiros
│   ├── carregador_dados.py      # Leitura e validação dos arquivos de dados
│   └── config.py                # Configurações gerais do sistema
├── docs/                        # Documentação adicional do projeto
├── requirements.txt             # Dependências do projeto
├── .env.example                 # Exemplo de configuração de variáveis de ambiente
└── README.md                    # Documentação principal
```

---

## 📄 Descrição dos Arquivos Principais

### `src/app.py`
Responsável por iniciar a interface do Orion em Streamlit, organizar a interação com o usuário e exibir os resultados da análise.

### `src/agente.py`
Contém a lógica de integração com o modelo de linguagem, incluindo envio de contexto, recebimento de resposta e tratamento da saída gerada.

### `src/analisador.py`
Implementa a análise financeira local, com foco em consolidação dos dados, cálculo de métricas e preparação do resumo financeiro.

### `src/carregador_dados.py`
Faz a leitura dos arquivos de entrada, como CSVs e JSONs, e pode incluir validações de estrutura e integridade dos dados.

### `src/config.py`
Centraliza caminhos, nomes de arquivos, parâmetros gerais e configurações utilizadas pelo sistema.

---

## 🗂️ Dados de Entrada

O Orion trabalha com arquivos estruturados contendo informações financeiras do usuário.

| Arquivo | Formato | Finalidade |
|---------|---------|------------|
| `transacoes.csv` | CSV | Registra receitas e despesas |
| `planejamento_financeiro.json` | JSON | Define valores planejados de orçamento |
| `perfil_usuario.json` | JSON | Armazena perfil e objetivos financeiros |
| `categorias_financeiras.json` | JSON | Padroniza categorias utilizadas na análise |
| `historico_interacoes.csv` | CSV | Registra interações anteriores, se aplicável |

---

## ✅ Funcionalidades

- [x] Leitura de dados financeiros estruturados
- [x] Cálculo automático de saldo
- [x] Comparação entre planejado e realizado
- [x] Identificação de padrões de consumo
- [x] Geração de insights financeiros
- [x] Recomendações em linguagem natural
- [x] Interface interativa em Streamlit

---

## 💬 Exemplo de Uso

### Exemplo de entrada
- Receita total: **R$ 5.000,00**
- Despesa total: **R$ 625,40**

### Exemplo de saída
- Saldo positivo de **R$ 4.374,60**
- Nenhuma categoria ultrapassou o orçamento planejado
- Situação financeira considerada estável

### Exemplo de pergunta ao Orion
> “Como está minha situação financeira neste mês?”

### Exemplo de resposta esperada
> “Seu saldo mensal está positivo. As despesas permanecem abaixo do valor planejado, o que indica controle financeiro adequado no período analisado.”

---

## 🔐 Confiabilidade da Abordagem

O Orion foi projetado para **reduzir erros e alucinações**, adotando algumas estratégias importantes:

- prioriza dados fornecidos localmente
- realiza o processamento financeiro antes de consultar a IA
- restringe a interpretação da IA ao contexto calculado
- evita depender de texto livre para informações críticas
- pode solicitar mais contexto quando os dados são insuficientes

---

## ⚠️ Limitações

O Orion possui limitações importantes que devem ser consideradas:

1. não substitui um consultor financeiro profissional
2. não realiza previsões de mercado por padrão
3. não acessa dados externos em tempo real, salvo futura integração específica
4. depende da qualidade e consistência dos dados fornecidos
5. a camada de linguagem natural ainda pode exigir refinamentos visuais em alguns casos

---

## 🧪 Aprendizados Técnicos do Projeto

O desenvolvimento do Orion trouxe alguns aprendizados importantes:

- validar a estrutura dos arquivos de entrada é essencial
- não é seguro depender integralmente de texto livre gerado por IA
- separar análise, interface e integração com modelo torna o sistema mais robusto
- a renderização controlada da resposta final melhora a confiabilidade do produto
- sistemas reais com IA tendem a funcionar melhor com **estrutura + validação + apresentação controlada**

---

## 🛠️ Tecnologias Utilizadas

- Python
- Streamlit
- Pandas
- JSON
- CSV
- Python Dotenv
- Requests
- OpenAI API
n
---

## 🚀 Como Executar

### 1. Clonar o repositório
```bash
git clone https://github.com/fgiraldisp/projeto-orion.git
cd projeto-orion
```

### 2. Criar e ativar um ambiente virtual

#### Windows
```bash
python -m venv .venv
.venv\Scripts\activate
```

#### Linux / macOS
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar as dependências
```bash
pip install -r requirements.txt
```

### 4. Configurar as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto com base no arquivo `.env.example`.

Exemplo:
```env
OPENAI_API_KEY=sua_chave_aqui
MODEL_NAME=gpt-5.4
```

### 5. Executar a aplicação
```bash
streamlit run src/app.py
```

---

## 📌 Requisitos

- Python 3.10 ou superior
- ambiente virtual recomendado
- chave de API configurada, se houver uso de modelo externo
- arquivos de dados disponíveis na pasta `data/`

---

## 🔮 Próximos Passos

Evoluções previstas para o projeto:

- dashboard com gráficos financeiros
- validação mais rígida da saída estruturada da IA
- análises automáticas mais avançadas
- integração com fontes de dados reais
- expansão para nível de produto

---

## 👨‍💻 Autor

Projeto desenvolvido como estudo e aplicação prática de **Inteligência Artificial aplicada à análise financeira pessoal**.
