import re

def normalize(text, casefold=True, yo2e=True):
    result = text
    if casefold:
        result = result.lower()
    
    if yo2e:
        result = result.replace('ё', 'е')
        result = result.replace('Ё', 'Е')
    
    return result

def tokenize(text):
    pattern = r'\b[а-яa-z]+\b'
    tokens = re.findall(pattern, text, re.IGNORECASE)
    return tokens

def count_freq(tokens):
    freq = {}
    for token in tokens:
        if token in freq:
            freq[token] += 1
        else:
            freq[token] = 1
    return freq

def top_n(freq, n=5):
    items = list(freq.items())
    items.sort(key=lambda x: (-x[1], x[0]))
    top_items = items[:n]
    return top_items