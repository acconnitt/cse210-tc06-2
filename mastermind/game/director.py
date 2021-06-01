# The director handles the playing of the game and calls the other classes together.
from game.code import Code
from game.player import Player
from game.roster import Roster
from game.guess import Guess
from game.console import Console


class Director:

    def __init__(self):
        """ Constructor method. 
            Object is initialized
        """
        self.roster = Roster()  # Calls Roster class
        self.console = Console()  # Calls Console class
        self.keep_playing = True  # Keep playing while true
        self.win = False  # Starts as false while player hasn't won

    def start_game(self):
        self.prepare_game()  # Calls prepare_game method
        self.roster.next_player()  # Calls next_player method from Roster class
        while self.keep_playing:  # keep_playing "looping" while is true
            print()
            self._get_inputs()  # Calls get_inputs method
            self._do_updates()  # Calls do_updates
            self.roster.next_player()  # Calls next_player method from Roster class

    def _get_inputs(self):
        """Ask for player guess 
            Checks if the player input is valid
        """
        player = self.roster.get_current()  # Calls get.current to get object
        self.console.print_blank_line()
        # Calls print_player method from Cosole class
        self.console.print_players(self.roster)
        self.console.print_blank_line()
        # Calls print_turn method from Cosole class
        self.console.print_turn(player)

        valid_guess = False  # Validation of guess
        while not valid_guess:
            # Ask for player guess and checks if player imput is valid
            guess = input("What is your guess? ")
            for i in guess:
                if i.isalpha():
                    print(
                        "Your guess was invalid because it contained letters, please try again. ")
                    break
            if len(guess) != 4:  # Check guess len is not diferent than 4 digits
                print(
                    "Your guess was invalid because it wasn't 4 characters long, please try again.")
            else:
                valid_guess = True  # Guess is valid

        player.guess.set_guess(guess)  # Call check_guess to update guess
        player.guess.check_guess()  # Call check_guess to check if player guess is == to code
        self.win = player.guess.check_win()  # Calls guess_

    def _do_updates(self):
        """Check if game is player won the game

        Args:
            self (Director): An instance of Director.
        """
        if self.win:
            self.console.print_win(self.roster.get_current())
            self.keep_playing = False
        elif not self.win:
            pass

    def prepare_game(self):
        """Prepares the game before it begins. In this case, that means getting the player names and adding them to the roster.
            Args:
                self (Director): An instance of Director.
        """
        code = Code()  # Calls the Code class
        new_code = code.get_code()  # Calls the get_code method from Code class
        for n in range(2):
            # Loop twice to get player name, guess, code
            # Players name input
            name = input(f"Enter a name for player {n + 1}: ")
            guess = Guess(new_code)
            player = Player(name, guess, code)
            # Calls add_player method with player as parameter
            self.roster.add_player(player)
