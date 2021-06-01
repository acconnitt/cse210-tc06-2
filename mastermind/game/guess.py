class Guess:

    """ The guess class gets and stores the last guess of each player.
    """

    def __init__(self, code, guess="____"):
        """The class constructor.
        """
        self.guess = str(guess)  # Player
        self.hint = "****"  # Hints
        self.code = str(code)  # Code

    def check_guess(self):
        """Check if user guess is same as system generated code
        """
        index = 0
        self.hint = "****"
        x = list(self.hint)
        # Loop through guess to compare code
        for letter in str(self.code):
            # If guess is == to code, hint index = X
            if letter == self.guess[index]:
                x[index] = "X"

            # If guess is != to code, hint index = O
            elif self.guess[index] in self.code:
                x[index] = "O"
            index += 1  # Next index
        self.hint = "".join(x)  # Uodate hint with x

    def set_guess(self, guess):
        """ Set guess to update """
        self.guess = guess

    def get_guess(self):
        """ Return guess"""
        return self.guess

    def check_win(self):
        """Check if player won
        """
        win = False
        for letter in self.hint:
            if letter == "X":
                win = True
            else:
                win = False
                break
        return win
