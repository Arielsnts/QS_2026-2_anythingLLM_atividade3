# Plano de Execução — Versões A e B

## Introdução

Esta seção apresenta as configurações das duas versões do experimento que serão utilizadas na avaliação do fluxo de perguntas e respostas com fontes (RAG) do AnythingLLM.

A **Versão A** será utilizada como baseline, empregando um prompt direto, contendo apenas a pergunta do usuário. A **Versão B** utilizará um prompt estruturado, mantendo todas as demais condições do experimento e alterando exclusivamente a formulação do prompt.

Cada um dos seis casos de teste (CT01–CT06) será executado uma vez em cada versão, totalizando 12 saídas. Todas as respostas, incluindo eventuais falhas de execução ou saídas vazias, serão registradas sem descarte ou substituição.

## Configuração das versões

### Versão A — Baseline

| Item | Configuração |
|---|---|
| Identificação | Versão A |
| Tipo | Baseline |
| Prompt | Prompt direto, contendo apenas a pergunta original do caso de teste, sem instruções adicionais. |
| Modelo | Gemini 2.5 Flash |
| Revisão | Não aplicável ao prompt direto. |
| Parâmetros | Configuração padrão do workspace, sem alterações específicas para os casos. |
| Fonte/contexto | Documentos fictícios indexados no workspace: Manual Organizacional v1.0, Política de Benefícios v2.0 e Relatório Financeiro 2025. O contexto efetivamente recuperado será registrado em cada execução. |
| Data | 09/11/2026 |

**Prompt utilizado:**

```text
{pergunta do caso de teste}
```

### Versão B — Prompt estruturado

| Item | Configuração |
|---|---|
| Identificação | Versão B |
| Tipo | Experimental |
| Prompt | Prompt estruturado, contendo objetivo, contexto, restrições e formato de resposta. |
| Modelo | Gemini 2.5 Flash |
| Revisão | Prompt estruturado — versão 1.0. |
| Parâmetros | Mesma configuração padrão do workspace utilizada na Versão A. |
| Fonte/contexto | Os mesmos documentos fictícios indexados no workspace da Versão A. O contexto efetivamente recuperado será registrado em cada execução. |
| Data | 09/11/2026 |

**Prompt utilizado:**

```text
Objetivo:
Responder à pergunta do usuário utilizando as informações disponíveis nos documentos do workspace.

Contexto:
Considere os documentos recuperados pelo sistema como fonte de informação para elaborar a resposta.

Restrições:
- Responda somente com base nas informações presentes nos documentos.
- Não invente informações, valores ou dados que não estejam disponíveis nas fontes.
- Caso não encontre evidências suficientes para responder, declare explicitamente essa limitação.
- Não utilize conhecimento externo para complementar as informações.

Formato:
Apresente uma resposta objetiva e direta, incluindo as fontes utilizadas para fundamentá-la.

Pergunta:
{pergunta do caso de teste}
```

## Fator de mudança e justificativa

A única mudança principal entre as versões A e B será a **formulação do prompt**.

Na Versão A, o sistema recebe somente a pergunta do usuário. Na Versão B, são adicionadas instruções explícitas sobre objetivo, contexto, restrições e formato esperado da resposta.

A alteração foi escolhida para avaliar se instruções mais estruturadas melhoram a qualidade das respostas, especialmente quanto à precisão factual, à utilização das fontes e à capacidade de reconhecer a ausência de evidências.

Nenhuma outra configuração será intencionalmente modificada entre as versões.

## Condições de comparabilidade

As seguintes condições serão mantidas idênticas nas duas versões:

- **Modelo:** Gemini 2.5 Flash.
- **Casos de teste:** CT01, CT02, CT03, CT04, CT05 e CT06.
- **Workspace:** mesmo workspace e mesmos documentos indexados.
- **Parâmetros:** configuração padrão do workspace.
- **Condições de execução:** sessão limpa a cada execução.
- **Quantidade:** uma execução por caso em cada versão.

O CT06 será tratado como uma variação do CT01, não sendo considerado uma observação independente.
