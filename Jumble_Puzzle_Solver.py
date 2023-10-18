import time
import functions as f


found = False
file_names = [('AdjIndex.txt', 'ADJECTIVE'), ('AdvIndex.txt', 'ADVERB'),
              ('NounsIndex.txt', 'NOUN'), ('VerbsIndex.txt', 'VERB')]
words = f.read_files(file_names)

while True:
    user_input = input(
        "Enter the Jumble Puzzle Word: (<enter> to quit) ").lower()

    if user_input == "":
        break

    print(f"Start time: {time.strftime('%H:%M:%S', time.localtime())}")
    found = False
    possible_permutations = f.find_permutations(user_input)
    for perm in possible_permutations:
        if perm in words:
            found = True
            print(perm.upper(), words[perm])

    if not found:
        print("<Not found>")

    print(f"Finish time: {time.strftime('%H:%M:%S', time.localtime())}\n")
