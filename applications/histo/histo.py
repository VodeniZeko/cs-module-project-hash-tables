# Your code here

import sys


def count_occurences(string):
    table = {}
    current_word = ''
    longest_word = ''
    for i in range(len(string)):
        if string[i].lower() >= 'a' and string[i].lower() <= 'z' or string[i] == "'":
            current_word = current_word + string[i].lower()
        else:
            if string[i] == "'":
                pass
            if current_word != '':
                if len(current_word) > len(longest_word):
                    longest_word = current_word
                if current_word in table:
                    table[current_word] += 1
                    current_word = ''
                else:
                    table[current_word] = 1
                    current_word = ''

    return (table, longest_word)


def print_histogram(table, longest):
    sorted_words = sorted(table.items(), key=lambda word: (-word[1], word[0]))
    for word in sorted_words:
        line = word[0]
        if len(line) < len(longest):
            line = line + (' ' * (len(longest) - len(line)))
        line = line + '  ' + ('#' * word[1])
        print(line)


input_filename = sys.argv[1]

input_file = open(input_filename, 'r')

input_string = input_file.read()

(table, longest_word) = count_occurences(input_string)

print_histogram(table, longest_word)
