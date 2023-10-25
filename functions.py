import re


# This function reads words from files and
# stores them in a dictionary.
def read_files(file_names):
    words = {}

    # Iterate through the file_names
    for file_name, pos in file_names:
        with open(file_name, 'r') as f:
            indexes = f.readlines()

        # Update the 'words' dictionary with words from the file.
        # Words are extracted by splitting each line at the '|' character.
        # Words that pass the 'has_no_numbers_and_special_chars' check are
        # included in the dictionary.
        words.update({word.split('|')[0]: pos for word in indexes
                      if has_no_numbers_and_special_chars(word.split('|')[0])})

    return words


# This function generates all permutations
# of a given word.
def find_permutations(word):
    all_permutations = ['']

    # Generate permutations by inserting the character at different positions
    # within each existing permutation.
    for char in word:
        all_permutations = [perm[:i] + char + perm[i:] for perm in
                            all_permutations for i in range(len(perm) + 1)]

    return set(all_permutations)


# This function checks if a word contains numbers or special characters.
# Use regular expression to search for digits, underscores, and
# hyphens in the 'word'.If any of these characters are found, the function
# returns False.
def has_no_numbers_and_special_chars(word):
    return not bool(re.search(r'[\d._-]', word))
