# Store functions for text processing (e.g., word count, character count, find word, replace word) 
# in a dictionary. Write a function process_text(text, operation, **kwargs) that uses 
# this dictionary to perform the requested text processing operation.
def word_count(text):
    res = len(text.split())
    return res
def characret_count(text):
    for i in range(len(text)):
        res = i+1
    return res
def find_word(text, **kwargs):
    if word in text:
        return f"yes, there is [{word}] in the [{text}]"
    else:
        return f"no, there isn't [{word}] in the [{text}]"
def replace_word(text, **kwargs):
    res = text.replace(word1, word2)
    return res

def process_text(text, operation, **kwargs):
    dict = {
        "word count":word_count,
        "character count": characret_count,
        "find word": find_word,
        "replace word":replace_word
    }
    res = dict[operation](text, **kwargs)
    return res


text=input("Enter text: ")
operation=input("Enter the operation: ")
if operation == "find word":
    word = input("Enter the word that you want to find: ")
    print(process_text(text=text, operation=operation, word = word))
if operation == "replace word":
    word1 = input("Enter the word that you want to change: ")
    word2 = input("Enter the word that you want to be in the text: ")
    print(process_text(text=text,operation=operation, word1=word1, word2=word2))
if operation == "word count":
    print(process_text(text,operation))
if operation == "character count":
    print(process_text(text,operation))







