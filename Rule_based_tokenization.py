import nltk

text = "That U.S.A. poster-print costs $12.40..."

pattern = r'''(?x)                     # verbose mode
    (?:[A-Z]\.)+                      # abbreviations like U.S.A.
  | \w+(?:-\w+)*                      # words with hyphen
  | \$?\d+(?:\.\d+)?%?                # numbers like $12.40 or 82%
  | \.\.\.                            # ellipsis ...
  | [][.,;"'?():-_`]                  # punctuation
'''

tokens = nltk.regexp_tokenize(text, pattern)

print(tokens)