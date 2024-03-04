# Store a list of words
word_list = ["apple", "banana", "orange", "grape", "kiwi", "pear", "Pineapple"]

# Use list comprehension to create a new list with words of odd length
odd_length_words = [word for word in word_list if len(word) % 2 != 0]

# Print the result
print("Words with an odd number of characters:", odd_length_words)
