"""
Write a function that will find all the anagrams of a word from a list.
You'll be given two inputs, a word, and an array of words.
You should return an array of all the anagrams or an empty array if there are none.
"""
def anagrams(word, array):
    template_word = {str(char):word.count(char) for char in word}
    result = list()        
    for word in array:
        target_word = {str(char):word.count(char) for char in word}
        if target_word == template_word:
            result.append(word)
    return result

# Shortest possible solution
def a(w, l): return [i for i in l if sorted(i)==sorted(w)]
