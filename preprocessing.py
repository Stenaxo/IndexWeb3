import re

def tokenize(text):
    # Tokenisation simple basée sur les espaces et normalisation
    return re.findall(r'\w+', text.lower())
