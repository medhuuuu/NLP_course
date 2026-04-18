def bpe_algorithm(corpus, num_merges):
    # Initialize the vocabulary with unique symbols in the corpus
    vocab = set(" ".join(corpus).split())
    # print("Initial Vocabulary:", vocab)

    # List to keep track of the merges performed for encoding later
    merges = []

    # Perform the specified number of merges
    for i in range(num_merges):
        pairs = {}
        
        # Count frequency of adjacent symbol pairs
        for word in corpus:

            # Split the word into symbols (initially, each character is a symbol)
            symbols = word.split()

            # range(len(symbols) - 1) to avoid index out of range when accessing symbols[j + 1]
            # This loop will iterate through the symbols in the word and create pairs of adjacent symbols.
            for j in range(len(symbols) - 1):
                pair = (symbols[j], symbols[j + 1])

                # count the frequency of each pair in the corpus
                if pair in pairs:
                    pairs[pair] += 1
                else:
                    pairs[pair] = 1
        
        # Find the most frequent pair
        most_frequent_pair = max(pairs, key=pairs.get)
        
        # Merge the most frequent pair        
        # Add the new symbol to the vocabulary and record the merge
        merges.append(most_frequent_pair) 
        new_symbol = ''.join(most_frequent_pair)
        vocab.add(new_symbol)
        
        # Replace occurrences of the most frequent pair in the corpus
        new_corpus = []
        for word in corpus:
            new_word = word.replace(' '.join(most_frequent_pair), new_symbol)
            new_corpus.append(new_word)
        
        corpus = new_corpus
    return  corpus, merges

# Example usage
corpus = ["l o w", "l o w e r", "n e w e s t", "w i d e s t"]
updated_corpus = bpe_algorithm(corpus, 10)
print("Updated Corpus:", updated_corpus)



def bpe_encode(word, merges):
    # Split the word into tokens (initially, each character is a token)
    tokens = word.split()
    
    for merge in merges:
        # Create a new token by merging the pair of tokens
        new_token = ''.join(merge)

        # Replace occurrences of the pair in the tokens list with the new token
        # This list comprehension iterates through the tokens and checks if the current token and the next token match the pair to be merged.
        # If they do, it replaces them with the new token; otherwise, it keeps the original token.
        # The condition i < len(tokens) - 1 ensures that we do not go out of bounds when checking the next token.
        # The result is a new list of tokens where the specified pair has been merged into a single token.
        tokens = [new_token if (tokens[i] == merge[0] and i < len(tokens) - 1 and
                                 tokens[i + 1] == merge[1]) else tokens[i] for i in range(len(tokens))]
    return ' '.join(tokens)


# Example usage of encoding
corpus = ["l o w", "l o w e r", "n e w e s t", "w i d e s t"]
corpus, merges = bpe_algorithm(corpus, 10)
print("Merges:", merges)
print("Encoded:", bpe_encode("lower", merges))

