from os import system, name

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def read_words(file):
    word_list = open(file, "r").read().split(",")
    word_list.sort()
    for i in range(len(word_list)):
        word_list[i] = word_list[i].upper()
    return word_list
