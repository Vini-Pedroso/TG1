from JogadorUno import JogadorUno
from Uno import Uno
import os
import BlackJack
class ErrorLine(Exception):
    def __init__(self, msg):
        self.msg = msg

class ErrorJogo(Exception):
    def __init__(self, msg="Jogo inválido"):
        self.msg = msg
        super().__init__(self.msg)

def main(): 
    for game_number in range(1, 11):
        arquivo = f"entradas/jogo_{game_number}.txt"
        if os.path.exists(arquivo):
            with open(arquivo, "r") as file:
                game_info = file.readline().strip().split("--")
                game_name = game_info[0]
            try:
                if game_name == "Blackjack":
                    game = load_and_play_Blackjack_game(arquivo)
                elif game_name == "Uno":
                    game = load_and_play_uno_game(arquivo)                
                    game.start_game()
                            
            except Exception as e:
                print(f"Erro ao iniciar o jogo {game_number}: {str(e)}")
        else:
            print(f"Arquivo {arquivo} não encontrado.")

def get_winner_from_output(output_filename):
    winner = None
    with open(output_filename, "r") as file:
        lines = file.readlines()
        for line in reversed(lines):
            if line.startswith("Vencedor"):
                winner = line.strip().split(":")[1].strip()
                break
    return winner

def load_and_play_uno_game(arquivo):
    with open(arquivo, "r") as file:
        game_info = file.readline().strip().split("--")
        
        game_name = game_info[0]
        
        if game_name == 'Uno':

            num_players, num_decks, seed, rounds = game_info[1:]
            players_info = [line.strip() for line in file.readlines()[1:]]
            num_players = int(num_players)
            num_decks = int(num_decks)
            seed = int(seed)
            rounds = int(rounds)
            players = []
            _ , game_number = arquivo.split("_")
            game_number,_ = game_number.split(".")
            for player_info in players_info:
                nome, cpf = player_info.strip().split("--")
                jogador = JogadorUno( nome, cpf, 0, game_number)
                players.append(jogador)
            uno_game = Uno(arquivo,num_players, num_decks, seed, rounds, game_number)
            
            
            #uno_game.start_game()

        
            winner = uno_game.get_winner()

            return uno_game
def load_and_play_Blackjack_game(arquivo):

    with open(arquivo, "r") as file:
        game_info = file.readline().strip().split("--")
        game_name = game_info[0]
    if game_name == 'Blackjack':
        BlackJack.inicia_BlackJack_jogo(arquivo)
if __name__ == "__main__":
    main()
