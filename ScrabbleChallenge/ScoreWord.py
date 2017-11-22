class ScoreWord:
    def __init__(self, score, word):
        self.score = score
        self.word = word

    def __str__(self):
        return "{} {}".format(self.score, self.word)
