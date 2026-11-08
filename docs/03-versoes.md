# Versionamento (Versões A e B)

---

## 1. Caracterização e Paridade Experimental

Para assegurar a validade do experimento de avaliação de qualidade de software generativo e a comparabilidade entre as duas execuções, foram mantidas estritamente idênticas as seguintes condições experimentais nas Versões A e B:

* **Ferramenta e Orquestrador:** AnythingLLM (espaço de trabalho *"Meu Workspace"*).
* **Modelo e Provedor:** Gemini 2.5 Flash.
* **Parâmetros do Modelo:** Configuração padrão do sistema mantida sem alterações (sem definição de temperatura personalizada, limites de tokens customizados ou outros parâmetros avançados).
* **Base Documental de Contexto (RAG):** Os mesmos três arquivos em formato PDF carregados no workspace:
  1. *ISTQB CTFL Syllabus v4.0.1*
  2. *NIST AI 600-1 Generative Artificial Intelligence Profile*
  3. *OWASP Web Security Testing Guide (WSTG) v4.2*
* **Casos de Teste Avaliados:** A bateria de testes completa composta pelos 6 casos de teste (CT01 a CT06), executados uma vez na Versão A e uma vez na Versão B, totalizando as 12 saídas brutas do experimento.

---

## 2. Detalhamento das Versões

### Versão A — Baseline (Original)

A Versão A representa o comportamento padrão e baseline da aplicação. O prompt utilizado foca na restrição de contexto e abstenção explícita diante de informações ausentes.

* **Prompt Original (Versão A):**
  > *"Com base exclusivamente no documento [Nome do Documento] disponível neste workspace, explique [Pergunta do Caso]. Para cada informação apresentada, indique a seção ou página do documento que a fundamenta. Se não encontrar alguma informação no documento, informe isso explicitamente. Não utilize conhecimento externo."*
* **Modelo e Revisão:** Gemini 2.5 Flash.
* **Parâmetros:** Padrão do sistema (sem alteração de temperatura ou controle de tokens).
* **Fonte / Contexto:** Meu Workspace (ISTQB CTFL v4.0.1, NIST AI 600-1 e OWASP WSTG v4.2).
* **Data de Execução:** Novembro de 2026.

### Versão B — Versão Modificada (Fator Único)

Conforme exigido pelo protocolo experimental, a Versão B introduz **uma única mudança declarada** (isolamento de um único fator) em relação à Versão A.

* **A Única Mudança Declarada:** Inclusão de instrução explícita no prompt para estruturação da resposta em tópicos diretos e objetivos, mantendo inalterada a restrição de abstenção.
* **Justificativa da Mudança:** Avaliar se a exigência de uma estrutura em tópicos melhora as avaliações humanas nas dimensões de **Relevância** e **Suporte** (facilitando a leitura e a localização das seções/páginas citadas), verificando se o modelo mantém a rigidez do critério de abstenção quando os trechos recuperados forem insuficientes (ex: CT05).
* **Prompt Modificado (Versão B):**
  > *"Com base exclusivamente nos documentos do workspace, responda à pergunta [Pergunta do Caso] de forma direta e estruturada em tópicos, indicando a seção ou página correspondente. Caso os trechos recuperados sejam insuficientes, declare abstenção explicitamente, sem recorrer a conhecimentos externos."*
* **Modelo e Revisão:** Gemini 2.5 Flash (idêntico à Versão A).
* **Parâmetros:** Padrão do sistema (idêntico à Versão A).
* **Fonte / Contexto:** Meu Workspace (os mesmos 3 PDFs) (idêntico à Versão A).
* **Data de Execução:** Novembro de 2026.

---

## 3. Manifestos de Execução (Artefatos de Versionamento)

### 3.1. Manifesto da Versão A (Baseline)

#### 1. Informações Gerais
* **Versão:** A (Baseline)
* **Data de Execução:** Novembro de 2026
* **Status:** Executado

#### 2. Configuração do Ambiente e Modelo
* **Aplicação / Orquestrador:** AnythingLLM
* **Workspace:** Meu Workspace
* **Modelo de Linguagem (LLM):** Gemini 2.5 Flash
* **Revisão do Modelo:** Padrão via API do AnythingLLM
* **Parâmetros de Inferência:** Temperatura padrão do sistema (não alterada); limite de tokens padrão.

#### 3. Base Documental (Contexto / RAG)
1. `ISTQB CTFL Syllabus v4.0.1.pdf`
2. `NIST AI 600-1 Generative Artificial Intelligence Profile.pdf`
3. `OWASP Web Security Testing Guide (WSTG) v4.2.pdf`

#### 4. Casos de Teste Executados
* CT01 a CT06 (6 casos de teste)

#### 5. Estrutura do Prompt Utilizado
> *"Com base exclusivamente no documento [Nome do Documento] disponível neste workspace, explique [Pergunta do Caso]. Para cada informação apresentada, indique a seção ou página do documento que a fundamenta. Se não encontrar alguma informação no documento, informe isso explicitamente. Não utilize conhecimento externo."*

---

### 3.2. Manifesto da Versão B (Modificada)

#### 1. Informações Gerais
* **Versão:** B (Modificada)
* **Data de Execução:** Novembro de 2026
* **Status:** Executado

#### 2. Fator Alterado (Mudança Única Declarada)
* **Fator Modificado:** Diretriz de formatação no Prompt (exigência explícita de respostas estruturadas em tópicos diretos e objetivos).
* **Justificativa:** Avaliar se a estruturação em tópicos melhora as avaliações humanas nas dimensões de Relevância e Suporte (facilitando a leitura e a localização das seções/páginas citadas), verificando se o modelo mantém a rigidez do critério de abstenção quando os trechos recuperados forem insuficientes (ex: CT05).

#### 3. Paridade Experimental (Condições Mantidas Idênticas à Versão A)
* **Aplicação / Orquestrador:** AnythingLLM *(idêntico à Versão A)*
* **Workspace:** Meu Workspace *(idêntico à Versão A)*
* **Modelo de Linguagem (LLM):** Gemini 2.5 Flash *(idêntico à Versão A)*
* **Revisão do Modelo:** Padrão via API do AnythingLLM *(idêntico à Versão A)*
* **Parâmetros de Inferência:** Padrão do sistema sem alterações *(idêntico à Versão A)*
* **Base Documental (RAG):** ISTQB CTFL v4.0.1, NIST AI 600-1, OWASP WSTG v4.2 *(idêntico à Versão A)*
* **Casos de Teste Executados:** CT01 a CT06 *(idêntico à Versão A)*

#### 4. Estrutura do Prompt Utilizado
> *"Com base exclusivamente nos documentos do workspace, responda à pergunta [Pergunta do Caso] de forma direta e estruturada em tópicos, indicando a seção ou página correspondente. Caso os trechos recuperados sejam insuficientes, declare abstenção explicitamente, sem recorrer a conhecimentos externos."*