# First draft: just choose random numbers for each exercise to do.

# TODO: 
# * weight exercises to avoid repeating the same one too frequenrly
# * choose random song to learn
# * randomize order in which exercises are chosen
# * start up Guitar Pro or somesuch
# * add other things to incorporate into my practicing schedule

from os import listdir
from random import shuffle
 
def main():
    picking_dir = "E:\Eric\Documents\Guitar\Guitar Pro Tabs\Exercises\Picking"
    legato_dir = "E:\Eric\Documents\Guitar\Guitar Pro Tabs\Exercises\Legato"
    picking_exercises = listdir(picking_dir)
    legato_exercises = listdir(legato_dir)
    shuffle(picking_exercises)
    shuffle(legato_exercises)
    print("Here's your practice session!")
    print("For your picking warmup, do exercise", picking_exercises[1])
    print("For your legato warmup, do exercise", legato_exercises[0])

if __name__ == '__main__':
    main()
