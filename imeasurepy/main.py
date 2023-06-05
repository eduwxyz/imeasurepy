import re

import spacy

nlp = spacy.load("pt_core_news_sm")

def frequency_intj(texto: str):
    """
    Dado um texto, retorna a quantidade de intejeições que existe nele.
    """

    doc = nlp(texto)
    qntd_interjeicao = [token.text for token in doc if token.pos_ == "INTJ"]

    qntd_exclamacao = [token.text for token in doc if "!" in token.text]

    return len(qntd_interjeicao) + len(qntd_exclamacao)

def frequency_emoji(texto: str):
    """
    Dado um texto, retorna a quantidade de emojis que tem nele.
    """
    emoji_pattern = re.compile(
        "[\U0001F300-\U0001F64F" "\U0001F680-\U0001F6FF" "\u2600-\u26FF\u2700-\u27BF]+",
        flags=re.UNICODE,
    )

    count = re.findall(emoji_pattern, texto)
   
    return len(count)