import os
import re


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, mode='r') as my_file:
        text = re.split(' |\n', my_file.read())
        return text


def remove_symbols(text):
    symbols = '!@#$%^&*()_+-=0987654321:;"?/>.<,| \n'
    for symbol in symbols:
        text = text.replace(symbol, '')
    return text


def get_most_frequent_words(text):
    words_chart = {}
    for word in text:
        word = word.lower()
        word = remove_symbols(word)
        if not word:  # if was only symbols
            continue
        if word in words_chart:
            words_chart[word] += 1
        else:
            words_chart[word] = 1
    return words_chart


if __name__ == '__main__':
    print('Enter filepath to your database:')
    path = input()
    text = load_data(path)
    if not text:
        print('File not found, sorry...')
        raise SystemExit
    most_frequent_words = get_most_frequent_words(text)
    for word in sorted(most_frequent_words, key=lambda word: most_frequent_words[word], reverse=True):
        print(word, most_frequent_words[word])
