## Base de Conhecimento

### Dados Utilizados

| Arquivo | Formato | Utilização no Agente |
|--------|--------|----------------------|
| historico_interacoes.csv | CSV | Contextualizar interações anteriores e manter continuidade nas análises do usuário |
| perfil_usuario.json | JSON | Personalizar as respostas com base no perfil, objetivos financeiros e preferências do usuário |
| planejamento_financeiro.json | JSON | Servir como referência para comparação entre valores planejados e realizados |
| transacoes.csv | CSV | Analisar receitas, despesas, saldo, padrões de consumo e gerar insights financeiros |
| categorias_financeiras.json | JSON | Padronizar categorias e subcategorias, garantindo consistência na análise dos dados |

---

### Adaptações nos Dados

As principais adaptações foram:

- Alteração de arquivos como `perfil_investidor.json` para `perfil_usuario.json`, focando em objetivos financeiros pessoais  
- Substituição de `produtos_financeiros.json` por `planejamento_financeiro.json`, permitindo comparação entre orçamento planejado e realizado  
- Criação do arquivo `categorias_financeiras.json` para padronização de receitas e despesas  
- Estruturação do arquivo `transacoes.csv` com campos como tipo, categoria, valor e forma de pagamento  
- Inclusão de `historico_interacoes.csv` para manter contexto das análises feitas pelo agente  

Essas adaptações permitem que o agente Orion atue como um **analista financeiro pessoal**, e não apenas como um recomendador de produtos.

---

### Estratégia de Integração

#### Como os dados são carregados?

Os arquivos JSON e CSV são carregados no início da execução do sistema utilizando bibliotecas como `pandas` (para CSV) e `json` (para arquivos estruturados).

Esses dados são organizados em estruturas internas (DataFrames e dicionários) que permitem rápida consulta e análise.

---

#### Como os dados são usados no prompt?

Os dados **não são inseridos diretamente no system prompt completo**.

Em vez disso, o agente utiliza uma abordagem híbrida:

- O Python realiza o processamento dos dados (cálculo de saldo, comparação entre planejado e realizado, identificação de padrões)  
- Apenas um **resumo estruturado** dessas informações é enviado ao modelo de linguagem  
- O modelo é utilizado principalmente para gerar explicações e recomendações em linguagem natural  

Essa abordagem reduz custo, melhora performance e evita envio de dados desnecessários ao modelo.

---

### Exemplo de Contexto Montado

**Dados do Usuário:**

- Nome: Flavio  
- Renda mensal: R$ 5.000  
- Objetivos: reduzir gastos desnecessários, melhorar controle do orçamento  

**Resumo Financeiro do Mês:**

- Receita total: R$ 5.000  
- Despesa total: R$ 625,40  
- Saldo atual: R$ 4.374,60  

**Comparação com Planejamento:**

- Alimentação: R$ 320,50 (dentro do limite de R$ 700)  
- Transporte: R$ 180,00 (dentro do limite de R$ 400)  
- Assinaturas: R$ 39,90 (dentro do limite de R$ 120)  
- Lazer: R$ 85,00 (dentro do limite de R$ 250)  

**Insights Identificados:**

1. Nenhuma categoria ultrapassou o orçamento até o momento  
2. O saldo atual está positivo e acima da meta de economia parcial  

---

### Observação Estratégica

O agente Orion utiliza uma abordagem híbrida, onde o processamento dos dados financeiros é realizado localmente em Python, enquanto o modelo de linguagem é utilizado apenas para geração de insights e explicações, garantindo maior eficiência, menor custo e maior controle sobre as análises.
