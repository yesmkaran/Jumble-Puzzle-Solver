import time
import functions as f

# list of .txt files to load into the dictionary
file_names = [('AdjIndex.txt', 'ADJECTIVE'), ('AdvIndex.txt', 'ADVERB'),
              ('NounsIndex.txt', 'NOUN'), ('VerbsIndex.txt', 'VERB')]

# read all txt files &
# store word:pos pairs in dictionary
words = f.read_files(file_names)

# loop until the user presses "enter" key
while True:
    user_input = input(
        "Enter the Jumble Puzzle Word: (<enter> to quit) ").lower()

    if not user_input:
        break

    print(f"Start time: {time.strftime('%H:%M:%S', time.localtime())}")

    # flag to check if a word is found in the dictionary
    found = False

    # find all possible permutations of an inputted word
    # check if the word exist in the dictionary
    possible_permutations = f.find_permutations(user_input)
    for perm in possible_permutations:
        if perm in words:
            found = True
            print(perm.upper(), words[perm])

    # print "Not Found" when a word doesn't exist
    if not found:
        print("<Not found>")

    print(f"Finish time: {time.strftime('%H:%M:%S', time.localtime())}\n")
