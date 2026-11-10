## Introdução

Este documento apresenta a avaliação da qualidade de geração aumentada por recuperação (RAG) do modelo AnythingLLM aplicado a documentos organizacionais internos (Políticas de Benefícios, Manuais e Relatórios). O objetivo é avaliar a aderência das respostas aos documentos fornecidos, contrastando o comportamento padrão da IA (Versão A) com o comportamento sob um system prompt restrito (Versão B).   

A avaliação utiliza três métricas principais, pontuadas de 0 a 2: Correção (C), Relevância (R) e Suporte (S), além da identificação de Falhas Críticas (como alucinações ou fabricação de dados).
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

- (pessoa 6): quatro anotações (CT01 e CT05 nas versões A e B), feitas sem consultar a R1
- consenso: só para as divergências, com a justificativa do acordo. As notas originais de R1 e R2 não são apagadas.
