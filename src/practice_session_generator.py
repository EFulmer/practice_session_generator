# TODO:
# * weight exercises to avoid repeating the same one too frequently?
# * randomly generate exercises?
# * check what OS the user is on and change the default arg to generate_practice_session accordingly
# * choose random song to learn
# * start up Guitar Pro or somesuch

import os
import random
import sys

keys = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
maj_min = ['major', 'minor']

def user_chosen_exercises(dirs):
    """
    Makes a list containing one randomly chosen file from each directory in
    dirs.
    """
    result = []
    random.shuffle(dirs)
    for d in dirs:
        exercises = os.listdir(directory)
        random.shuffle(exercises)
        directory.split('/')
        result.append(exercises[0])
    return result

def random_exercise():
    """
    """
    # thoughts:
    # current way of randomly getting keys seems very unpythonic
    # add in more options - harmonic/melodic minor? starting fret/string?
    # "modes"; easy mode might always start on 6th string and never have 
    # harmonic or melodic minor or something.
    return 'Play a' + keys[ random.randint(0, len(keys) - 1) ] + 
        maj_min[random.randint(0, len(maj_min) - 1) ] + 'scale.'

def main():
    print("-" * 10, "Welcome to the Guitar Practice Session Generator!", "-" * 10)
    choice = ''
    while choice != 'Q':
        print("1. Choose from one of my own exercises.")
        print("2. Choose a truly random exercise!")
        print("Q. Quit.")
        choice = input("Your choice: ")
        if choice == '1':
            print('I should actually write this.')
        elif choice == '2':
            print(random_exercise())
        elif choice != 'Q':
            print('That doesn\'t seem like a valid choice.')

if __name__ == '__main__':
    main()
