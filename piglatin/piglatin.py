import logging
import string


def findFirstVowel(given_word):
     for i in range(len(given_word)):
         if checkVowel(given_word[i]) == True:
             return i

def piglatin_word(input_string):
    firstVowel = findFirstVowel(input_string)
    if firstVowel == None:
        translated = (input_string + "ay")
    elif firstVowel == 0:
        translated = (input_string + "yay")
    elif firstVowel >= 1:
        translated = (input_string[firstVowel:] + input_string[:firstVowel] + "ay")
        print(input_string[firstVowel:])
        print(input_string[:firstVowel])
    else:
        pass
    if input_string.istitle():
        translated = translated.capitalize()

    return translated

def checkVowel(char):
    vowels="AaEeIiOoUu"
    for vowel_test in vowels:
        if char == vowel_test:
            return True
    return False

def piglatin_para(text):
    for word in text.split():
        word = word.strip()
        punctuation = None
        if word[-1] in string.punctuation:
            word, punctuation = word[:-1], word[-1:]
        word = piglatin_word(word)
        if punctuation:
            word = ''.join([word, punctuation])
        yield word

def check_if_starts_with_vowel(word):
    vowels="AaEeIiOoUu"
    if word[0] in vowels:
        return True
    return False

def translate(text):
    pig_words = piglatin_para(text.strip())
    pig_text = ' '.join(pig_words)
    return pig_text

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)
