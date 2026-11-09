import re
import unicodedata
from collections import Counter
import sys

def tokenizar(texto):
    texto = unicodedata.normalize("NFC", texto).casefold()
    return re.findall(r"\w+", texto)

def f1_lexical(resposta, referencia):
    tok_resp = tokenizar(resposta)
    tok_ref = tokenizar(referencia)

    if not tok_resp or not tok_ref:
        return 0.0, len(tok_resp), len(tok_ref), 0

    comuns = sum((Counter(tok_resp) & Counter(tok_ref)).values())
    if comuns == 0:
        return 0.0, len(tok_resp), len(tok_ref), 0

    p = comuns / len(tok_resp)
    r = comuns / len(tok_ref)
    f1 = 2 * p * r / (p + r)
    return f1, len(tok_resp), len(tok_ref), comuns

resposta = open(sys.argv[1], encoding="utf-8").read()
referencia = open(sys.argv[2], encoding="utf-8").read()

f1, n_resp, n_ref, comuns = f1_lexical(resposta, referencia)
print(f"tokens_resposta={n_resp}, tokens_referencia={n_ref}, comuns={comuns}, F1={f1:.3f}")