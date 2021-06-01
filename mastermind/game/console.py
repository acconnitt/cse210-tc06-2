# The console class outputs and prints various things that the director class tells it to do.
class Console:

    def print_blank_line(self):
        # Print blank line
        print("--------------------")

    def print_players(self, roster):
        # Print player's name and the start guess and hint string
        for player in roster.players:
            print(
                f"Player {player.get_name()}: {player.get_guess()}, {player.get_hint()}")

    def print_turn(self, player):
        # Prints player's turn
        print(f"{player.get_name()}'s turn: ")

    def print_win(self, player):
        # Prints player's name when wins
        print(f"{player.get_name()} won!")