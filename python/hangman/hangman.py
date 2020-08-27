# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman:
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.word = word
        self.masked_word = ['_' for l in range(len(word))]

    def guess(self, char):
        if self.status != STATUS_ONGOING:
            raise ValueError('The game has already finished.')
        else:
            rightPos = [k for k, v in enumerate(self.word) if char == v and char not in self.masked_word]
            if len(rightPos) == 0:
                self.remaining_guesses -= 1
                if self.remaining_guesses == -1:
                    self.status = STATUS_LOSE
            else:
                for p in rightPos:
                    self.masked_word[p] = char
                if '_' not in self.masked_word:
                    self.status = STATUS_WIN
            
    def get_masked_word(self):
        return ''.join(self.masked_word)

    def get_status(self):
        return self.status
