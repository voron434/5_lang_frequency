import os
import string

from collections import Counter


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as input_file:
        text = input_file.read()
    return text


def remove_symbols(text):
    symbols = string.punctuation + string.digits + '\n'
    for symbol in symbols:
        text = text.replace(symbol, ' ')
    return text


if __name__ == '__main__':
    path = input('Enter filepath to your file:')
    text = load_data(path)
    if text is None:
        print('No such file or directory.')
        raise SystemExit
    clean_text = remove_symbols(text).lower()
    words_list = clean_text.split(' ')
    words_list = [value for value in words_list if value]  # delete empty elements
    words_top = Counter(words_list).most_common(10)
    for word, count in words_top:
        print('{}  founded {} times'.format(word,count))
