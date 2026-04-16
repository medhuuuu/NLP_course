def bpe_algorithm(corpus, num_merges):
    # Initialize the vocabulary with unique symbols in the corpus
    vocab = set(corpus)
    # print("Initial Vocabulary:", vocab)

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
        new_symbol = ''.join(most_frequent_pair)
        vocab.add(new_symbol)
        
        # Replace occurrences of the most frequent pair in the corpus
        new_corpus = []
        for word in corpus:
            new_word = word.replace(' '.join(most_frequent_pair), new_symbol)
            new_corpus.append(new_word)
        
        corpus = new_corpus
    return  corpus

# Example usage
corpus = ["l o w", "l o w e r", "n e w e s t", "w i d e s t"]
updated_corpus = bpe_algorithm(corpus, 10)
print("Updated Corpus:", updated_corpus)