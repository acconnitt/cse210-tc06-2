# The player class gets the names of each player and stores them.
class Player:
    """
    """

    def __init__(self, name, guess, code):
        """
        """
        self._name = name
        self.guess = guess
        self.code = code

    def get_name(self):
        """
        """
        return self._name

    def get_guess(self):
        return self.guess.get_guess()

    def get_hint(self):
        return self.guess.hint