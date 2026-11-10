## Introdução

Este documento apresenta a avaliação da qualidade de geração aumentada por recuperação (RAG) do modelo AnythingLLM aplicado a documentos organizacionais internos (Políticas de Benefícios, Manuais e Relatórios). O objetivo é avaliar a aderência das respostas aos documentos fornecidos, contrastando o comportamento padrão da IA (Versão A) com o comportamento sob um system prompt restrito (Versão B).   

A avaliação utiliza três métricas principais, pontuadas de 0 a 2: Correção (C), Relevância (R) e Suporte (S), além da identificação de Falhas Críticas (como alucinações ou fabricação de dados).

## Avaliação (R1)
| ID | C (0/1/2) | R (0/1/2) | S (0/1/2) | Falha crítica (0/1) | Justificativa |
|---|:---:|:---:|:---:|:---:|---|
| CT01-A | 2 | 2 | 2 | 0 | A resposta informa corretamente o valor de R$ 50,00 por dia útil. |
| CT01-B | 2 | 2 | 2 | 0 | Valor correto, adicionando o detalhe do cartão benefício e a citação explícita da fonte. |
| CT02-A | 2 | 2 | 2 | 0 | A missão da empresa foi recuperada e transcrita corretamente. |
| CT02-B | 2 | 2 | 2 | 0 | Missão apresentada de forma direta, cumprindo a restrição de formato e citando a fonte. |
| CT03-A | 0 | 2 | 0 | 1 | **Falha Crítica:** A IA forneceu um valor financeiro (R$ 48,6 milhões) configurando alucinação ou uso de conhecimento externo não suportado pelas fontes. |
| CT03-B | 2 | 2 | 2 | 0 | Abstenção justificada; a IA declarou explicitamente a limitação conforme instruído no prompt. |
| CT04-A | 2 | 2 | 2 | 0 | Informou corretamente o período de experiência de 90 dias para o plano de saúde. |
| CT04-B | 2 | 2 | 2 | 0 | Resposta objetiva com o prazo correto e citação formal da política de benefícios. |
| CT05-A | 2 | 2 | 2 | 0 | Abstenção correta, indicando a falta de informações sobre o bônus de 2025. |
| CT05-B | 2 | 2 | 2 | 0 | Abstenção justificada, cumprindo rigorosamente a declaração de limitação exigida. |
| CT06-A | 2 | 2 | 2 | 0 | Informou o valor correto de R$ 50,00/dia útil e detalhou regras de crédito, acúmulo e faixas de desconto em folha. |
| CT06-B | 2 | 2 | 2 | 0 | Resposta objetiva com o valor correto de R$ 50,00/dia útil e condições de concessão, aderente aos documentos. | 

## Avaliação (R2)

O segundo avaliador analisou os quatro casos selecionados (CT01-A, CT01-B, CT05-A e CT05-B), utilizando os critérios de Correção (C), Relevância (R), Suporte (S) e Falha Crítica.

| Caso   |  C |  R |  S | Falha Crítica | Justificativa                                                                                                                         |
| ------ | -: | -: | -: | ------------: | ------------------------------------------------------------------------------------------------------------------------------------- |
| CT01-A |  2 |  2 |  2 |             0 | A resposta apresenta corretamente o valor de R$ 50,00 por dia útil trabalhado, conforme a Política de Benefícios.                     |
| CT01-B |  2 |  2 |  2 |             0 | A resposta informa corretamente o valor do benefício e o crédito mensal em cartão benefício, de acordo com o documento.               |
| CT05-A |  2 |  2 |  2 |             0 | A resposta reconhece que não há informações sobre o valor do bônus anual de 2025 nos documentos disponíveis, evitando inventar dados. |
| CT05-B |  2 |  2 |  2 |             0 | A resposta também realiza a abstenção corretamente, sem apresentar informações não comprovadas pelos documentos.                      |

## Concordância entre R1 e R2

Após a avaliação do segundo avaliador, foi realizada a comparação entre as pontuações de R1 e R2 nos quatro casos selecionados.

| Caso   | Avaliação R1 (C/R/S/FC) | Avaliação R2 (C/R/S/FC) | Concordância |
| ------ | ----------------------- | ----------------------- | ------------ |
| CT01-A | 2/2/2/0                 | 2/2/2/0                 | Sim          |
| CT01-B | 2/2/2/0                 | 2/2/2/0                 | Sim          |
| CT05-A | 2/2/2/0                 | 2/2/2/0                 | Sim          |
| CT05-B | 2/2/2/0                 | 2/2/2/0                 | Sim          |

**Resultado da concordância:**

- Casos avaliados: 4
- Casos com concordância: 4
- Casos com divergência: 0
- Taxa de concordância: **100%**

A taxa foi calculada pela seguinte fórmula:

`Concordância = (Casos com avaliações iguais / Total de casos) × 100`

`Concordância = (4 / 4) × 100 = 100%`

## Consenso entre os avaliadores

A comparação entre as avaliações de R1 e R2 apresentou concordância de 100%. Todos os quatro casos analisados receberam pontuações idênticas nos critérios de Correção, Relevância, Suporte e Falha Crítica.

Dessa forma, não foram identificadas divergências entre os avaliadores, não sendo necessária uma etapa adicional de consenso ou alteração das avaliações originais. As tabelas de R1 e R2 foram preservadas integralmente.

