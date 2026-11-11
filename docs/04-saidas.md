# Registro das Saídas — AnythingLLM

## Introdução

Esta seção apresenta as saídas obtidas nas execuções dos seis casos de teste, contemplando as versões A (baseline) e B (prompt estruturado) do AnythingLLM.

Para cada execução, foram registrados a resposta bruta retornada pelo sistema, o resultado do F1 lexical e a respectiva evidência visual, armazenada no diretório `evidencias/saidas/`.

O cálculo do F1 lexical foi realizado por meio de um script Python, utilizando os arquivos `.txt` contendo a resposta de referência e a saída gerada pela IA. O script aplica normalização Unicode NFC, conversão para letras minúsculas com `casefold` e tokenização por expressões regulares (`\w+`). Em seguida, calcula a interseção dos tokens considerando suas frequências, obtendo precisão, revocação e a média harmônica entre ambas (F1).

Os resultados são apresentados com três casas decimais. A avaliação qualitativa das respostas, incluindo correção, relevância, suporte nas fontes e identificação de falhas críticas, será realizada posteriormente no documento `05-avaliacao.md`.

## Resultados das execuções

| ID | Resposta bruta | F1 lexical | F1 aplicado a τ (0,5) | Evidência |
|---|---|---:|---|---|
| CT01-A | A empresa concede vale-refeição no valor de R$ 50,00 por dia útil trabalhado. | 0.636 | Aprovado | [Imagem](evidencias/saidas/ct-01A.png) |
| CT01-B | A empresa concede vale-refeição no valor de R$ 50,00 por dia útil trabalhado, creditado mensalmente em cartão benefício. Fonte: Politica-Beneficios.pdf | 0.452 | Reprovado | [Imagem](evidencias/saidas/ct-01B.png) |
| CT02-A | A missão da Empresa Exemplo S.A. é "Simplificar a gestão de pequenas e médias empresas por meio de soluções digitais acessíveis, seguras e fáceis de usar, contribuindo para o crescimento sustentável dos nossos clientes." | 0.852 | Aprovado | [Imagem](evidencias/saidas/ct-02A.png) |
| CT02-B | A missão da Empresa Exemplo S.A. é simplificar a gestão de pequenas e médias empresas por meio de soluções digitais acessíveis, seguras e fáceis de usar, contribuindo para o crescimento sustentável dos clientes. Fonte: Manual-Organizacional.pdf | 0.813 | Aprovado | [Imagem](evidencias/saidas/ct-02B.png) |
| CT03-A | A receita líquida da Empresa Exemplo S.A. no exercício de 2025 foi de R$ 48,6 milhões. | 0.364 | Reprovado | [Imagem](evidencias/saidas/ct-03A.png) |
| CT03-B | Não foi possível determinar a receita líquida da empresa no exercício de 2025 com base nas informações disponíveis. | 0.000 | Reprovado | [Imagem](evidencias/saidas/ct-03B.png) |
| CT04-A | Os colaboradores terão direito ao plano de saúde após o período de experiência de 90 dias. | 0.667 | Aprovado | [Imagem](evidencias/saidas/ct-04A.png) |
| CT04-B | Os colaboradores passam a ter direito ao plano de saúde após o período de experiência de 90 dias. Fonte: Politica-Beneficios.pdf | 0.533 | Aprovado | [Imagem](evidencias/saidas/ct-04B.png) |
| CT05-A | Não encontrei informações sobre o valor do bônus anual por desempenho pago aos colaboradores em 2025 nos documentos disponíveis. | 0.000 | Reprovado | [Imagem](evidencias/saidas/ct-05A.png) |
| CT05-B | Não foi possível encontrar informações sobre o valor do bônus anual por desempenho pago aos colaboradores em 2025 nos documentos disponíveis. | 0.000 | Reprovado | [Imagem](evidencias/saidas/ct-05B.png) |
| CT06-A | A empresa concede vale-refeição no valor de R$ 50,00 por dia útil trabalhado. O crédito é feito mensalmente em cartão benefício, até o 5º dia útil de cada mês. Colaboradores com salário de até R$ 6.000,00 não têm desconto em folha; acima desse valor, o desconto é de 10% do valor do benefício. O auxílio-refeição não é pago em dias de férias, licença ou afastamento, e o saldo não utilizado acumula por até 60 dias. | 0.335 | Reprovado | [Imagem](evidencias/saidas/ct-06A.png) |
| CT06-B | A empresa disponibiliza R$ 50,00 de vale-refeição por dia útil trabalhado. Este valor é creditado mensalmente em cartão benefício até o 5º dia útil de cada mês. O benefício não é pago nos dias de férias, licença ou afastamento. | 0.292 | Reprovado | [Imagem](evidencias/saidas/ct-06B.png) |

## Conclusão das saídas

Os resultados do F1 lexical demonstraram diferenças na sobreposição entre as respostas geradas e as referências esperadas. Considerando o limiar de aprovação estabelecido (τ = 0,5), a Versão A obteve três resultados aprovados (CT01, CT02 e CT04), enquanto a Versão B obteve dois (CT02 e CT04).

A Versão A apresentou valores de F1 superiores aos da Versão B em CT01, CT02, CT04 e CT06. Em CT03, a Versão A também obteve resultado superior, embora ambas tenham ficado abaixo do limiar. Em CT05, as duas versões obtiveram F1 igual a zero. Esse resultado evidencia uma limitação da métrica na avaliação de respostas de abstenção, pois diferentes formulações podem expressar corretamente a ausência de informação sem apresentar grande sobreposição lexical com a referência.

Destaca-se o CT06, no qual a Versão A obteve F1 de 0,335, enquanto a Versão B alcançou 0,292. Apesar da maior sobreposição lexical da Versão A, ambas ficaram abaixo do limiar. Além disso, a presença de informações adicionais nas respostas pode influenciar o cálculo, sem necessariamente representar maior qualidade ou precisão.

De modo geral, os resultados indicam que, neste conjunto de testes, a Versão A apresentou melhor desempenho lexical que a Versão B. Entretanto, o F1 lexical, isoladamente, não é suficiente para determinar a qualidade das respostas do AnythingLLM. A métrica pode penalizar diferenças de redação e respostas semanticamente equivalentes, além de não avaliar adequadamente a correção factual ou a pertinência das fontes. Portanto, será necessária a avaliação humana para verificar se as respostas atendem aos critérios de correção, relevância e suporte documental, conforme definido no plano GQM.

A avaliação humana e a análise comparativa entre as versões serão documentadas em `05-avaliacao.md`.