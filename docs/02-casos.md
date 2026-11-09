# Plano de Casos de Teste — AnythingLLM

## Introdução

Esta seção apresenta os seis casos de teste que serão utilizados na avaliação funcional do fluxo de perguntas e respostas com fontes (RAG) do AnythingLLM.

Os testes serão realizados utilizando como contexto os documentos fictícios anexados ao workspace, referentes à Empresa Exemplo S.A. Os documentos contêm informações organizacionais, políticas de benefícios e dados financeiros, permitindo formular perguntas com respostas previamente conhecidas e verificar a capacidade do sistema de recuperar informações relevantes.

Os casos foram definidos para contemplar perguntas funcionais com evidências disponíveis (CT01–CT04), uma pergunta sem evidência suficiente para responder (CT05) e uma variação de pergunta por paráfrase (CT06).

O objetivo desta etapa é estabelecer os prompts e suas respectivas respostas de referência, que serão utilizados posteriormente nas execuções e avaliações das versões A e B do experimento.

## Casos de teste

| ID | Tipo | Pergunta (prompt) | Fonte esperada | Resposta esperada |
|---|---|---|---|---|
| CT01 | Funcional — informação direta | Qual é o valor do vale-refeição oferecido pela empresa por dia útil trabalhado? | Política de Benefícios, seção 2 — Vale-refeição, página 1. | R$ 50,00 por dia útil trabalhado. |
| CT02 | Funcional — informação direta | Qual é a missão da Empresa Exemplo S.A.? | Manual Organizacional, seção 2 — Missão, página 1. | Simplificar a gestão de pequenas e médias empresas por meio de soluções digitais acessíveis, seguras e fáceis de usar, contribuindo para o crescimento sustentável dos clientes. |
| CT03 | Funcional — informação numérica | Qual foi a receita líquida da empresa no exercício de 2025? | Relatório Financeiro 2025, seção 2 — Demonstração de resultado 2025, página 1. | R$ 48,6 milhões. |
| CT04 | Funcional — informação direta | Após quanto tempo de contratação os colaboradores passam a ter direito ao plano de saúde? | Política de Benefícios, seção 3 — Plano de saúde, página 1. | Após o período de experiência de 90 dias. |
| CT05 | Sem evidência suficiente — abstenção | Qual foi o valor do bônus anual por desempenho pago aos colaboradores em 2025? | Nenhum dos documentos do workspace apresenta informações sobre bônus anual por desempenho. | O sistema deve declarar explicitamente que não encontrou informações sobre o pagamento ou o valor de bônus anual por desempenho nos documentos disponíveis. Não deve inventar valores, confirmar a existência do benefício ou apresentar informações não sustentadas pelas fontes. |
| CT06 | Variação funcional — paráfrase | Quanto a empresa disponibiliza de auxílio-refeição para cada dia útil trabalhado? | Política de Benefícios, seção 2 — Vale-refeição, página 1. Caso de origem: CT01. | R$ 50,00 por dia útil trabalhado. A pergunta utiliza uma formulação diferente da original, mantendo a intenção de consultar o mesmo benefício e sua quantia. |

## Documentos utilizados no workspace

Os seguintes documentos fictícios serão indexados no workspace e utilizados como base de conhecimento para a execução dos casos de teste.

| Documento | Conteúdo utilizado |
|---|---|
| Manual-Organizacional.pdf | Missão, visão, valores e objetivos estratégicos da empresa. |
| Politica-Beneficios.pdf | Vale-refeição, plano de saúde, home office e demais benefícios oferecidos aos colaboradores. |
| Relatorio-Financeiro-2025.pdf  | Resultados financeiros, indicadores e comparação com as metas do exercício de 2025. |
