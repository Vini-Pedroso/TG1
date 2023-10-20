from cartas import Deck
from jogadorUno import JogadorUno
from uno import Uno
import os

class ErrorLine(Exception):
    def __init__(self, msg):
        self.msg = msg

def main():
    # Defina aqui o nome do arquivo que você deseja ler
    arquivo = "jogo_6.txt"

    if os.path.exists(arquivo):
        try:
            game = load_game(arquivo)
            if game is not None:
                game.start_game()
            else:
                print("Jogo não suportado.")
        except Exception as e:
            print(f"Erro ao iniciar o jogo: {str(e)}")
    else:
        print(f"Arquivo {arquivo} não encontrado.")

def load_game(file_name):
    with open(file_name, "r") as file:
        game_info = file.readline().strip().split("--")
        game_name = game_info[0]
        
        if game_name == 'Uno':
            return load_uno(game_info)

        if len(game_info) != 5:
            raise ErrorLine(f"Arquivo {file_name} não possui informações suficientes.")

        nomeJogo, NumeroJogadores, NumeroBaralhos, seed, rodadas = game_info
        NumeroJogadores = int(NumeroJogadores)
        NumeroBaralhos = int(NumeroBaralhos)
        seed = int(seed)
        rodadas = int(rodadas)

        jogadores = []

        for line in file:
            line = line.strip().split("--")
            if len(line) < 2:
                raise ErrorLine(f"Arquivo {file_name} contém informações de jogador inválidas.")
            nome, cpf = line[0], line[1]
            saldo = int(line[2]) if len(line) > 2 else 0
            condParada = int(line[3]) if len(line) > 3 else 0
            jogador = JogadorUno(nome, cpf, saldo, condParada)
            jogadores.append(jogador)

        activePlayers = [player for player in jogadores if player.saldo > 0]

        return Uno(NumeroJogadores, activePlayers, NumeroBaralhos, seed, rodadas)
    
def load_uno(lines):
    game_info = lines[0].strip().split("--")
    num_players = int(game_info[1])
    num_decks = int(game_info[2])
    seed = int(game_info[3])
    rounds = int(game_info[4])

    players = []

    for i in range(1, num_players + 1):
        player_info = lines[i].strip().split("--")
        nome = player_info[0]
        cpf = player_info[1]
        condParada = int(player_info[2])
        players.append((nome, cpf, condParada))

    return Uno(num_players, players, num_decks, seed, rounds)

if __name__ == "__main__":
    main()
