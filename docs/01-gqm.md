## Plano GQM

> **Registro de pré-definição:** este plano foi fixado **antes** da bateria final ( data do commit `<2026-11-06>`). Nenhum valor abaixo (τ, regras, critérios) foi ajustado após ver os resultados.

### 1. Objetivo e perguntas

**Objetivo:** Analisar as respostas do fluxo de **perguntas e respostas com fontes (RAG) do AnythingLLM**, nas versões **A** (prompt direto, baseline) e **B** (prompt estruturado, única mudança principal), com o propósito de avaliar se a mudança melhora a qualidade das respostas e se uma métrica automática simples representa essa qualidade, do ponto de vista da equipe de Qualidade de Software.

| Pergunta | Medida |
|---|---|
| **Q1.** A versão B atende melhor à tarefa do que a versão A? | M2 — Taxa de aprovação humana |
| **Q2.** O sinal automático representa a adequação das respostas? | M1 — F1 lexical e M3 — Concordância auto–humano |

### 2. Escopo do experimento

| Item | Definição |
|---|---|
| **Fluxo** | Usuário → prompt → recuperação de contexto (busca vetorial nos documentos do workspace) → modelo → resposta + fontes |
| **Versão A** | Prompt direto: apenas a pergunta |
| **Versão B** | Prompt estruturado: objetivo, contexto, restrições (responder só com base no documento, não inventar valores, declarar quando não houver evidência) e formato. O mesmo molde é aplicado aos seis casos. |
| **Fatores mantidos fixos** | Gemini 2.5 Flash, workspace, documentos indexados, configuração padrão do workspace e sessão limpa a cada execução |
| **Casos** | CT01–CT04: perguntas funcionais com resposta presente nos documentos; CT05: pergunta sem evidência nos documentos (resposta esperada: declarar o limite); CT06: paráfrase ou erro de digitação de CT01 |
| **Execuções** | 6 casos × 2 versões = 12 saídas, uma execução por caso/versão |


### 3. Medidas

| | M1 — F1 lexical | M2 — Taxa de aprovação humana | M3 — Concordância auto–humano |
|---|---|---|---|
| **Unidade** | Adimensional, 0 a 1, por saída (agregado por versão: média e mediana) | Proporção (n/6) ou %, por versão | Proporção (n/12) |
| **Fórmula** | `P = comuns / tokens_resposta`; `R = comuns / tokens_referência`; `F1 = 2·P·R / (P+R)`; `F1 = 0` se não houver sobreposição ou a resposta for vazia | `aprovadas_humano / 6`, calculada para A e para B. Aprovada = Correção 2, Relevância 2, Suporte 2 **e** falha crítica = 0 | `decisões iguais / 12` (6 casos × 2 versões), comparando a decisão automática com a decisão humana final |
| **Denominador** | 1 por saída; 6 saídas por versão | 6 por versão | 12 |
| **Limitação** | Mede só sobreposição de palavras, não significado. Respostas do RAG tendem a ser longas e a citar fontes, o que reduz a precisão lexical mesmo quando corretas. A versão B, por ser mais estruturada, pode alterar o F1 só pelo formato. Paráfrase correta pode ter F1 baixo, e trocar "R$ 55 milhões" por "R$ 45 milhões" mantém muitas palavras, mas muda o fato. Em CT05 (abstenção), a redação varia e o F1 tende a ser instável. | Apenas 6 casos por versão: cada caso vale ~16,7 p.p., então diferenças são grosseiras e sem poder estatístico. CT06 é variação de CT01 (não é observação independente). Em 8 das 12 saídas a decisão vem de um único avaliador (R1). O cegamento pode ser parcial, pois o formato da resposta de B tende a revelar a versão. | Depende diretamente do valor de τ. Não corrige concordância ao acaso (sem kappa). Com poucos casos, uma única divergência altera muito o valor. As duas decisões são binárias e perdem a nuance das notas 0/1/2. |

**Decisão humana final** (usada em M2 e M3): em CT01 e CT05, o consenso justificado de R1 e R2 quando houver divergência (R1 e R2 originais são preservados); nas demais saídas, a nota de R1.

**Falha crítica (0/1), regra prévia.** Vale 1 se a saída: (a) afirma como certo um valor ou fato contrário à fonte; (b) inventa dado, ou atribui a resposta a documento/fonte inexistente ou sem relação com o tema; ou (c) em CT05, responde com conteúdo fabricado em vez de declarar que não há informação nos documentos. Saída vazia ou com falha de execução **não** é falha crítica por si só, mas é registrada e reprovada (Relevância 0). Os documentos do workspace são sintéticos e sem dados pessoais.

### 4. Limiar do sinal automático (τ)

- **Regra:** o sinal automático **aprova** a saída se `F1 ≥ τ`; caso contrário, **reprova**.
- **Valor:** **τ = 0,5**.
- **Justificativa:** valor didático aceito pela atividade. Como as referências são curtas e revisadas por pessoa, exigir F1 ≥ 0,5 significa que ao menos cerca de metade dos tokens da resposta e da referência coincidem, nível intermediário que evita aprovar sobreposição acidental sem exigir cópia literal. Não há conjunto de calibração novo; τ foi fixado antes da bateria e **não será alterado** após ver os resultados. Eventuais ajustes seriam apenas discutidos como análise posterior, sem substituir o resultado oficial.

### 5. Normalização e referência vazia

**Normalização e tokenização:**
1. Normalização Unicode **NFC**.
2. **`casefold`** sem remover acentos.
3. Tokens de **palavras** (sequências alfanuméricas; pontuação descartada; números são tokens, e "R$ 55" gera os tokens `r` e `55`).
4. Sem stemming, sem remoção de stopwords.
5. Tokens em comum = **interseção de multiconjuntos** (cada token conta no máximo o número de vezes que aparece nos dois textos).
6. O F1 é calculado sobre o **texto da resposta** exibido no chat; a lista de fontes e as indicações visuais da interface ficam de fora.

**Casos especiais:**
- Resposta vazia ou sem sobreposição: `F1 = 0` e sinal automático **reprova**.
- Referência sem tokens após normalização: o caso é **corrigido antes da bateria** (a referência é revisada por pessoa). Se ocorrer depois, o caso é declarado inválido e registrado, **sem inventar score** de F1.
- Falha de execução: registrada como saída vazia e tratada pelos critérios acima; nunca descartada.

### 6. Critério de avanço e bloqueio

A decisão se baseia na **avaliação humana**. O F1 e a concordância informam a Q2, mas não decidem sobre a versão B.

| Decisão | Condição (definida antes do teste) |
|---|---|
| **Levar B à próxima etapa** | Aprovação humana de B **≥ aprovação de A + 1/6** (ao menos um caso aprovado a mais) **e** nenhuma falha crítica em B |
| **Manter A** | Aprovação de B ≤ aprovação de A (sem ganho), ou B apresenta falha crítica em caso em que A não falhou |
| **Revisar** | Houver ganho de B, mas também falha crítica em B; ou falhas críticas em ambas as versões; ou o F1 de B subir sem melhora na aprovação humana (indício de ganho apenas na métrica) |

**Condição de bloqueio:** qualquer **falha crítica em B** bloqueia o avanço de B, independentemente de F1 ou taxa de aprovação.

