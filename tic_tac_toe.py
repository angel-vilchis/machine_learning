# Tic Tac Toe
# Angel Vilchis

from typing import List
from random import randint, choice

TIE_GAME = "njbihQSjiKkhbjig75df"
        
class Player():
    def __init__(self, name: str=None, symbol: str=None) -> None:
        self.symbol = symbol
        self.name = name


class Bot(Player):
    def __init__(self, name: str=None, symbol: str=None) -> None:
        super().__init__(name, symbol)

    def choose(self, available_positions: List[str]):
        return choice(available_positions)
        
        
class TicTacToe():
    def __init__(self) -> None:
        self.winner = None
        self.board = None
        self.reset_gameboard()
        self.get_players()

    def coinflip_for_chooser(self, heads: str, tails: str) -> (str, str):
        coinflip = randint(0, 100)
        print(f"{heads} chooses if heads, {tails} if tails.")
        if coinflip < 50:
            print("heads")
            print(f"{heads} gets to choose.")
            return heads, tails
        else:
            print("tails")
            print(f"{tails} gets to choose.")
            return tails, heads
        
    def get_available_positions(self) -> List[str]:
        available_positions = []
        possible_options = ['1', '2', '3', '4', '5', '6', '7', '8' ,'9']
        for i in range(3):
            for j in range(3):
                if self.board[i][j] in possible_options:
                    available_positions.append(self.board[i][j])
        return available_positions

    def update_board(self, turn: Player) -> None:
        option = 0
        available_positions = self.get_available_positions()
        while option not in available_positions:
            if isinstance(turn, Bot):
                option = turn.choose(available_positions)
                print(f"{turn.name}, enter an available choice: {int(option)}")
                continue
            option = input(f"{turn.name}, enter an available choice: ")
        option = int(option)
        if option <= 3:
            self.board[0][option-1] = turn.symbol
        elif option > 3 and option < 7:
            self.board[1][option-4] = turn.symbol
        else:
            self.board[2][option-7] = turn.symbol
        
    def diagonal_winner(self) -> Player:
        if self.board[0][0] == self.player_1.symbol and self.board[1][1] == self.player_1.symbol  and self.board[2][2] == self.player_1.symbol:
            return self.player_1
        if self.board[0][0] == self.player_2.symbol and self.board[1][1] == self.player_2.symbol and self.board[2][2] == self.player_2.symbol:
            return self.player_2
        if self.board[2][0] == self.player_1.symbol and self.board[1][1] == self.player_1.symbol and self.board[0][2] == self.player_1.symbol:
            return self.player_1
        if self.board[2][0] == self.player_2.symbol and self.board[1][1] == self.player_2.symbol and self.board[0][2] == self.player_2.symbol:
            return self.player_2
        return None

    def vertical_winner(self) -> Player:
        for i in range(3):
            if self.board[0][i] == self.player_1.symbol and self.board[1][i] == self.player_1.symbol and self.board[2][i] == self.player_1.symbol:
                return self.player_1
            elif self.board[0][i] == self.player_2.symbol and self.board[1][i] == self.player_2.symbol and self.board[2][i] == self.player_2.symbol:
                return self.player_2
        return None

    def horizontal_winner(self) -> Player:
        for i in range(3):
            if self.board[i] == [self.player_1.symbol, self.player_1.symbol, self.player_1.symbol]:
                return self.player_1
            elif self.board[i] == [self.player_2.symbol, self.player_2.symbol, self.player_2.symbol]:
                return self.player_2
        return None

    def game_has_ended(self) -> Player:
        if not self.get_available_positions():
            return Player("TIE_GAME", "")
        self.winner = self.horizontal_winner()
        if not self.winner:
            self.winner = self.vertical_winner()
        if not self.winner:
            self.winner = self.diagonal_winner()
        if self.winner:
            return self.winner
        return None

    def print_board(self) -> None:
        for row in self.board:
            print(row)

    def play_game(self) -> Player:
        print("When it's your turn, enter the integer position you would like to take")
        turn = self.player_1
        while not self.game_has_ended():
            self.print_board()
            self.update_board(turn)
            if turn == self.player_1:
                turn = self.player_2
            else:
                turn = self.player_1
                
        self.print_board() 
        return self.game_has_ended()

    def get_players(self) -> None:
        num_players = input("How many non-bot players? Enter 1 or 2: ")
        assert (num_players == '1' or num_players == '2'), "Must be '1' or '2' non-bot players"

        bot_name = None
        print("We will coinflip for who decides to go first.")
        if num_players == '1':
            player_name = input("Enter your player name: ")
            bot_name = input("Enter bot name: ")
            heads = input("Enter 'heads' to be heads, or anything else for tails: ") == "heads"
            if heads:
                first_name = player_name
                second_name = bot_name
            else:
                first_name = bot_name
                second_name = player_name
                
        if num_players == '2':
            first_name = input("Enter name for heads player: ")
            second_name = input("Enter name for tails player: ")

        chooser, other = self.coinflip_for_chooser(first_name, second_name)
        
        print()

        print("Player 1 makes the first move.")
        if chooser != bot_name:
            option = input(f"{chooser}, Enter 1 to be player 1 or 2 to be player 2: ")
        else:
            option = str(randint(1, 2))
            print(f"{bot_name}: I'll choose {option}")

        assert (option == '1' or option == '2'), "You can either go first '1' or second '2'"
        
        if option == '1':
            self.player_1 = Player(chooser, "X")
            self.player_2 = Player(other, "O")
        elif option == '2':
            self.player_1 = Player(other, "X")
            self.player_2 = Player(chooser, "O")
            
        if self.player_1.name == bot_name:
            self.player_1 = Bot(self.player_1.name, self.player_1.symbol)
        elif self.player_2.name == bot_name:
            self.player_2 = Bot(self.player_2.name, self.player_2.symbol)
        
    def reset_gameboard(self) -> None:
        self.board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

def main():
    tic_tac_toe = TicTacToe()
    winner = tic_tac_toe.play_game()
    if winner.name == "TIE_GAME":
        print("Tie game.")
    else:
        print(f"Congrats, {winner.name}! You win!")
    
if __name__ == "__main__":
    main()
