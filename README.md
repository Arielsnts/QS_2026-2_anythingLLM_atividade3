# Avaliação de Qualidade de Software - Aplicação de IA Generativa

## Sobre esta Atividade

Esta é a **Atividade 3 (AV3) — Métricas automáticas versus avaliação humana (GQM)**, com foco em um único fluxo do **AnythingLLM** já utilizado nas atividades anteriores. O objetivo é executar um experimento comparando duas versões do mesmo fluxo (A, baseline, e B, com uma única mudança), usando os mesmos seis casos, e verificar até que ponto a métrica automática (F1 lexical) concorda com o julgamento humano.

A análise responde à pergunta norteadora: uma mudança simples melhora a qualidade das respostas, e até que ponto a métrica automática concorda com a avaliação humana? Ao final, é apresentada uma decisão experimental (manter A, levar B adiante ou revisar), fundamentada nas evidências.

**Projeto Avaliado:** AnythingLLM <br />
**Repositório Oficial:** [Link do repositório do projeto](https://github.com/Mintplex-Labs/anything-llm)

---

## Vídeo da Atividade

- [Clique Aqui para acessar o vídeo](video/video.md)

---

## Informações relevantes

- **[Contribuição Individual](info/contribuicoes.md)**
- **[Declaração de Uso de IA](info/declaracao-uso-ia.md)**

---

## Como Replicar esta Avaliação

### Passos

1. **Clone este repositório**

```bash
git clone https://github.com/Arielsnts/QS_2026-2_anythingLLM_atividade3
cd QS_2026-2_anythingLLM_atividade3
```

2. **Consulte a documentação técnica**

- Leia os arquivos da `docs/` na ordem: `01` a `06`.
- Revise o plano GQM e o critério τ antes dos resultados (`01-gqm.md`).
- Consulte as saídas brutas em `04-saidas.md` e `evidencias/`.

3. **Replique o experimento**

- Use o manifesto de cada versão em `03-versoes.md` (A e B).
- Execute os seis casos de `02-casos.md` uma vez em cada versão (12 saídas).
- Para calcular o F1 lexical, entre na pasta do script:

```bash
cd evidencias/f1-lexical
```

- Execute o comando abaixo para cada caso, informando primeiro o arquivo da saída e depois o arquivo da referência:

```bash
python3 f1.py saidas/ct-01A.txt referencias/ct-01.txt
```

- Repita o comando para os demais casos e versões, alterando os nomes dos arquivos.
- Registre as avaliações humanas e compare com as nossas em `05-avaliacao.md`.

4. **Valide a decisão**

- Revise a tabela consolidada, os gráficos e a análise de divergência em `06-analise-decisao.md`.
- Verifique se a decisão segue o critério definido antes da execução.
- Compare com o seu contexto de uso.

---

## Documentação Técnica

Navegue pelas seções principais:

- **[Plano GQM](docs/01-gqm.md)**
- **[Casos e Referências](docs/02-casos.md)**
- **[Versões A e B](docs/03-versoes.md)**
- **[Saídas e F1 Automático](docs/04-saidas.md)**
- **[Avaliação Humana (R1, R2 e Consenso)](docs/05-avaliacao.md)**
- **[Análise e Decisão](docs/06-analise-decisao.md)**

---

## Evidências

- Saídas brutas, contextos e scripts: [clique aqui](evidencias/)

---

## Relatório Final

- **[Relatório Técnico (PDF)](relatorio/)** - Versão compilada

---

## Referências

- **[Referências](info/referencias.md)**

---

## Outras informações

- **Disciplina:** Qualidade de Software
- **Período:** 2026.2
- **Docente:** Glauco de Figueiredo Carneiro
- **Data de Entrega:** 11/11/2026