def concatenate_words(words):
    return ' '.join(words)

words = ["Hey", "I", "am", "Lucifer", "from" , "California"]
print(concatenate_words(words))

############################################################################

def reverse_string(s):
    return s[::-1]

print(reverse_string("Criminology"))

############################################################################

def count_words(sentence):
    return len(sentence.split())

print(count_words("I studied Forensic Science from Jain University Banglore"))

############################################################################

import string

def is_pangram(s):
    alphabet = set(string.ascii_lowercase)
    return alphabet <= set(s.lower())

print(is_pangram("The quick brown fox jumps over the lazy dog"))

############################################################################

def remove_vowels(s):
    vowels = "aeiouAEIOU"
    return ''.join([ch for ch in s if ch not in vowels])

print(remove_vowels("She was about to go"))

############################################################################

def longest_word_length(sentence):
    words = sentence.split()
    return len(max(words, key=len))

print(longest_word_length("Zumba makes your body feel relax"))

############################################################################

def reverse_sentence(sentence):
    words = sentence.split()
    return ' '.join(reversed(words))

print(reverse_sentence("He is dancing"))

############################################################################

def count_vowel_names(names):
    vowels = "AEIOUaeiou"
    return sum(name[0] in vowels for name in names)

names = ["Adi", "Ayush", "Gau", "Krushna", "Manu"]
print(count_vowel_names(names))

############################################################################

def remove_duplicates(s):
    result = ""
    for ch in s:
        if ch not in result:
            result += ch
    return result

print(remove_duplicates("addresser"))

############################################################################


def word_in_sentence(sentence, word):
    return word.lower() in sentence.lower().split()

print(word_in_sentence("She is happy", "healty"))

