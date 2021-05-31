# The guess class gets and stores the last guess of each player.
class Guess:

    def __init__(self, code, guess="____"):
        """The class constructor.
        """
        self.guess = str(guess)
        self.hint = "****"
        self.code = str(code)

    def check_guess(self):
        index = 0
        self.hint = "****"
        x = list(self.hint)
        for letter in str(self.code):
            if letter == self.guess[index]:
                x[index] = "X"
            elif self.guess[index] in self.code:
                x[index] = "O"
            index += 1
        self.hint = "".join(x)

    def set_guess(self, guess):
        self.guess = guess

    def get_guess(self):
        return self.guess

    def check_win(self):
        win = False
        for letter in self.hint:
            if letter == "X":
                win = True
            else:
                win = False
                break
        return win
