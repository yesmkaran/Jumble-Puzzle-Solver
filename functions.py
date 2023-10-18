import re


def read_files(file_names):
    words = {}

    for file_name, pos in file_names:
        with open(file_name, 'r') as f:
            indexes = f.readlines()

        words.update({word.split('|')[0]: pos for word in indexes
                      if has_no_numbers_and_special_chars(word.split('|')[0])})

    return words


def find_permutations(word):
    all_permutations = ['']

    for char in word:
        all_permutations = [perm[:i] + char + perm[i:] for perm in
                            all_permutations for i in range(len(perm) + 1)]
    return set(all_permutations)


def has_no_numbers_and_special_chars(word):
    return not bool(re.search(r'[\d._-]', word))
