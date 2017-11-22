import random
from sys import argv
import os


def read_flashcard_file(filename):
    """Get the questions from a fixed flash card file"""
    filepath = "cardrepository/" + filename
    if not os.path.isfile(filepath):
        print("Not a valid file name!!")
        exit()

    flash_card_dict = {}
    with open(filepath) as file:
        while True:
            line = file.readline().replace("\n", "")
            if 0 == len(line):
                break
            keyvalue = line.split(",")
            flash_card_dict[keyvalue[0]] = keyvalue[1]
    return flash_card_dict


def select_questions_randomly(flash_car_dict):
    while True:
        flash_card_key = random.choice(list(flash_card_dict.keys()))
        answer = input("{}? ".format(flash_card_key))
        if "exit" == answer.lower():
            print("Goodbye")
            exit()
        elif answer.lower() == flash_card_dict[flash_card_key].lower():
            print("Correct! Nice job.")
        else:
            print("Incorrect. The correct answer is {}.".format(flash_card_dict[flash_card_key]))


def get_filename():
    if 2 != len(argv):
        print("Please input a quiz questions file name!")
        exit()
    return argv[1]


# Run the script
filename = get_filename()
flash_card_dict = read_flashcard_file(filename)
select_questions_randomly(flash_card_dict)
