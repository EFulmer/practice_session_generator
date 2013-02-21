# TODO:
# * weight exercises to avoid repeating the same one too frequently?
# * randomly generate exercises?
# * check what OS the user is on and change the default arg to generate_practice_session accordingly
# * choose random song to learn
# * start up Guitar Pro or somesuch

from os import listdir
from random import shuffle
from sys import argv

# take a default argument listing the directories my exercises are in
# hooray for modularity!
def generate_practice_session(dirs=
                              ["E:\Eric\Documents\Guitar\Guitar Pro Tabs\Exercises\Picking", 
                               "E:\Eric\Documents\Guitar\Guitar Pro Tabs\Exercises\Legato"]):
    shuffle(dirs)
    for directory in dirs:
        exercises = listdir(directory)
        shuffle(exercises)
        directory.split('/')
        print "For %s, do %s" % (directory, exercises[0])

def main():
    print "-" * 10, "Welcome to the Guitar Practice Session Generator!", "-" * 10
    if len(argv) < 2:
        generate_practice_session()
    else:
        directories = argv[1:]
        generate_practice_session(directories)

if __name__ == '__main__':
    main()
