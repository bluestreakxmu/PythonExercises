from sys import argv
from ScrabbleChallenge.ScoreWord import ScoreWord

sowpodlist = []
valid_words = []

scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
          "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
          "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
          "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
          "x": 8, "z": 10}


def construct_word_list():
    """construct a word list from 'sowpods.txt'"""
    with open("sowpods.txt") as file:
        while True:
            line = file.readline().replace("\n", "")
            if 0 == len(line):
                return
            sowpodlist.append(line)


def get_the_rack():
    """get the Scrabble rack (the letters available to make words) from the command line argument"""
    if len(argv) != 2:
        print("Usage: scrabble.py [RACK]")
        return
    key_word = argv[1].lower()
    # sort the keyword's letters for purpose of reducing comparison to sowpod list
    return sorted(key_word)


def find_valid_words(key_word):
    """find all words from the word list that are made of letters that are a subset of the rack letters"""
    for word in sowpodlist:  # loop sowpod list
        keyword_copy = key_word.copy()
        match_word_flag = True
        for letter in list(word):  # loop word's letters
            match_letter_flag = False
            for keyword_letter in keyword_copy:  # loop keyword's letters
                if letter < keyword_letter:  # Note: the keyword letter is sorted from 'a' to 'z'
                    break
                elif letter == keyword_letter:
                    keyword_copy.remove(keyword_letter)
                    match_letter_flag = True
                    break

            if not match_letter_flag:
                match_word_flag = False
                break
        if match_word_flag:
            valid_words.append(word)


def scoring():
    """determine the Scrabble scores for each valid word, using the scores dictionary"""
    # calculate score for every word
    score_words = []
    for word in valid_words:
        word_score = 0
        for letter in list(word):
            word_score += scores[letter]
        score_words.append(ScoreWord(word_score, word))

    # sort the words by score
    score_words.sort(key=lambda item: item.score, reverse=True)
    # print the words by score
    for score_word in score_words:
        print(score_word)


# Run this script
keyword = get_the_rack()
if keyword:
    construct_word_list()
    find_valid_words(keyword)
    scoring()
