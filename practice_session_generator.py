# TODO:
# * weight exercises to avoid repeating the same one too frequently
# * choose random song to learn
# * randomize order in which exercises are chosen
# * start up Guitar Pro or somesuch
# * add other things to incorporate into my practicing schedule

from os import listdir
from random import shuffle
from sys import argv

# take a default argument listing the directories my exercises are in
# hooray for modularity!
def generate_practice_session(dirs=
                              ["E:\Eric\Documents\Guitar\Guitar Pro Tabs\Exercises\Picking", 
                               "E:\Eric\Documents\Guitar\Guitar Pro Tabs\Exercises\Legato"]):
    shuffle(dirs)
    for i in dirs:
        exercises = listdir(i)
        shuffle(exercises)
        i.split('/')
        print "For %s, do %s" % (dirs[i], exercises[0])

def main():
    if len(argv) < 2:
        generate_practice_session()
    else:
        directories = argv[1:]
        generate_practice_session(directories)

if __name__ == '__main__':
    main()
