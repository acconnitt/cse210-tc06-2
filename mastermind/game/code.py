# The code class generates the secret code at the start of the game.
import random


class Code:

    def __init__(self):
        # Variable that stores the code
        self.code = 0

    def generate_code(self):
        # This generates a code using the random module
        self.code = random.randint(1000, 9999)

    def get_code(self):
        # Calls the generate code method and returns that code
        self.generate_code()
        return self.code

