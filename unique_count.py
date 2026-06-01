#Program to count number of unique words in a given sentence using sets.

sentence = input("Enter a sentence: ")

words = sentence.lower().split()
unique_words_count = len(set(words))

print(f"Number of unique words: {unique_words_count}")
