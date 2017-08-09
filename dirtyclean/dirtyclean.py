from unicodedata import category, normalize
from sys import maxunicode
from re import sub

letter_categories = set(["Lu", "Ll", "Lt", "Lo"])

translation_dictionary = {x: " " for x in range(maxunicode) if category(chr(x)) not in letter_categories}

def clean(s, simplify_letters = False):
    if simplify_letters:
        s = normalize("NFKD", s)
    else:
        s = normalize("NFKC", s)
    cleaned = s.translate(translation_dictionary).expandtabs(tabsize=1).strip()
    tidied = sub(r"\s{2,}", " ", cleaned)
    return tidied
