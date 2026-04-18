import regex as re

def pre_tokenization_bpe(text):
    pattern = re.compile(
        r"'s|'t|'re|'ve|'m|'ll|'d"      # contractions
        r"| ?\p{L}+"                    # words
        r"| ?\p{N}+"                    # numbers
        r"| ?[^\s\p{L}\p{N}]+"          # punctuation
        r"|\s+(?!\S)|\s+"               # whitespace
    )
    
    # Find all tokens in the text using the regex pattern
    tokens = pattern.findall(text)
    return tokens

text = "We're 350 dogs! Um, lunch?"
tokens = pre_tokenization_bpe(text)

print("Tokens:", tokens)