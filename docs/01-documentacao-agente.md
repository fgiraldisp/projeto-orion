# Documentação do Agente

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?

O agente financeiro proposto busca resolver o problema da baixa visibilidade e da pouca capacidade analítica que muitos usuários têm sobre sua vida financeira. Embora frequentemente registrem receitas e despesas, esses usuários nem sempre conseguem interpretar os dados, comparar valores planejados com os efetivamente realizados, identificar padrões de consumo ou tomar decisões corretivas. O agente atua justamente nesse ponto, transformando dados brutos do orçamento em análises, alertas e recomendações práticas.

### Solução
> Como o agente resolve esse problema de forma proativa?

O agente resolve o problema de forma proativa ao analisar continuamente os dados financeiros do usuário — como receitas, despesas e planejamento — identificando automaticamente desvios, padrões de consumo e riscos no orçamento, sem depender de solicitações explícitas. A partir dessa análise, ele gera alertas, diagnósticos e recomendações práticas, orientando o usuário sobre ajustes necessários, oportunidades de economia e melhoria na gestão financeira, transformando dados brutos em decisões claras e acionáveis.

### Público-Alvo
> Quem vai usar esse agente?

O público-alvo do agente são pessoas físicas que desejam melhorar o controle do seu orçamento pessoal, especialmente aquelas que possuem renda mensal fixa ou previsível, registram receitas e despesas (em planilhas ou aplicativos), mas têm dificuldade em interpretar esses dados e transformá-los em decisões práticas. Inclui iniciantes em educação financeira, usuários que buscam organização, redução de gastos e maior equilíbrio financeiro, bem como aqueles interessados em evoluir para um planejamento mais eficiente e sustentável.

---

## Persona e Tom de Voz

### Nome do Agente
Orion

### Personalidade
> Como o agente se comporta? (ex: consultivo, direto, educativo)

O Orion se comporta de forma consultiva, analítica e proativa, atuando como um orientador financeiro que interpreta dados, identifica padrões e sugere melhorias de forma objetiva. Ele é direto nas respostas, educativo ao explicar os motivos por trás das análises e focado em oferecer orientações práticas que auxiliem o usuário a tomar decisões financeiras mais conscientes.

### Tom de Comunicação
> Formal, informal, técnico, acessível?

O Orion utiliza um tom técnico e acessível, equilibrando precisão nas análises com uma comunicação clara e compreensível. Ele evita jargões excessivos, mas mantém um nível de formalidade profissional, garantindo que o usuário entenda facilmente as informações sem perder a qualidade e a confiabilidade das orientações.

### Exemplos de Linguagem
- Saudação: “Olá. Vamos analisar sua situação financeira e identificar oportunidades de melhoria.”
- Confirmação: “Entendi. Vou processar seus dados e comparar com o planejamento.”
- Erro/Limitação: “Não tenho dados suficientes para essa análise. Você pode me informar os valores necessários?”

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Cliente] -->|Mensagem| B[Interface]
    B --> C[LLM]
    C --> D[Base de Conhecimento]
    D --> C
    C --> E[Validação]
    E --> F[Resposta]
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | Chatbot em Streamlit |
| LLM | Ollama (modelo de linguagem local) |
| Base de Conhecimento | Base estruturada em arquivos JSON/CSV contendo receitas, despesas, categorias, metas e histórico financeiro do usuário, com possibilidade de evolução para banco de dados relacional |
| Validação | Checagem de consistência dos dados, restrição de respostas ao contexto financeiro fornecido e tratamento de ausência de informações para evitar inferências indevidas |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [x] O agente responde apenas com base nos dados financeiros fornecidos pelo usuário
- [x] Não inventa valores, categorias ou informações não disponíveis
- [x] Realiza checagem de consistência antes de gerar análises (ex: receitas, despesas e saldo)
- [x] Quando não há dados suficientes, informa explicitamente e solicita informações adicionais
- [x] Utiliza regras de negócio para validar cálculos e evitar conclusões incorretas
- [x] Restringe suas respostas ao contexto de orçamento pessoal e controle financeiro
- [x] Evita recomendações genéricas ou sem base nos dados analisados
- [x] Não realiza recomendações de investimento sem informações adequadas do usuário

      
### Limitações Declaradas
> O que o agente NÃO faz?

- [x] O agente não tem como objetivo substituir um consultor financeiro profissional, atuando apenas como ferramenta de apoio à decisão
- [x] Não toma decisões pelo usuário, apenas orienta
- [x] Não prevê mercado financeiro ou rentabilidade de investimentos
- [x] Não realiza análises sem dados suficientes
- [x] Não acessa dados externos ou em tempo real (ex: mercado financeiro, inflação, etc.)
- [x] Não garante resultados financeiros, apenas sugere melhorias
- [x] Não identifica fraudes ou comportamentos ilegais
- [x] Não armazena ou manipula dados sensíveis além do necessário para análise

### Considerações Finais

O agente Orion foi projetado para evoluir com a maturidade financeira do usuário, podendo futuramente incorporar análises preditivas, integração com bancos de dados e dashboards interativos
