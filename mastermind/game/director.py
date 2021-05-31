# The director handles the playing of the game and calls the other classes together.
from game.code import Code
from game.player import Player
from game.roster import Roster
from game.guess import Guess
from game.console import Console


class Director:

    def __init__(self):
        self.roster = Roster()
        self.console = Console()
        self.keep_playing = True
        self.win = False

    def start_game(self):
        self.prepare_game()
        self.roster.next_player()
        while self.keep_playing:
            print()
            self._get_inputs()
            self._do_updates()
            self.roster.next_player()

    def _get_inputs(self):
        player = self.roster.get_current()
        self.console.print_blank_line()
        self.console.print_players(self.roster)
        self.console.print_blank_line()
        self.console.print_turn(player)

        valid_guess = False

        while not valid_guess:
            guess = input("What is your guess? ")
            for i in guess:
                if i.isalpha():
                    print("Your guess was invalid because it contained letters, please try again. ")
                    break
            if len(guess) != 4:
                print("Your guess was invalid because it wasn't 4 characters long, please try again.")
            else:
                valid_guess = True

        player.guess.set_guess(guess)
        player.guess.check_guess()
        self.win = player.guess.check_win()

    def _do_updates(self):
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
        code = Code()
        the_code = code.get_code()
        for n in range(2):
            name = input(f"Enter a name for player {n + 1}: ")
            guess = Guess(the_code)
            player = Player(name, guess, code)
            self.roster.add_player(player)
