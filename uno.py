# Classe Uno atualizada
import random
from Jogador import Jogador
from Cartas import Deck
from JogadorUno import JogadorUno

class ErrorCPF(Exception):
    def __init__(self, msg):
        self.msg = msg

class ErrorExitCondition(Exception):
    def __init__(self, msg="Condição de Parada Inválida"):
        self.msg = msg
        super().__init__(self.msg)

class ErrorInvalidBalance(Exception):
    def __init__(self, msg="Saldo Inválido"):
        self.msg = msg
        super().__init__(self.msg)

class ErrorEmptyDeck(Exception):
    def __init__(self, msg="Baralho vazio"):
        self.msg = msg
        super().__init__(self.msg)

class Uno:
    def __init__(self, arquivo,num_players, num_decks, seed, rounds, game_number):
        self.arquivo = arquivo
        
        self.num_players = num_players
        self.activePlayers = self.load_players(arquivo)
        print(self.activePlayers)
        print("AQUIIIIII")
        self.current_player = 0
        self.seed = seed
        self.current_card = None
        self.rounds = rounds
        self.game_number = game_number
        self.output_filename = f'saidas/jogo_{game_number}.saida'
        self.log_filename = f'saidas/jogo_{game_number}.log'
        self.init_output_file()

        if isinstance(num_decks, int) and num_decks > 0:
            self.num_decks = num_decks
        else:
            raise ValueError("Número de baralhos inválido")

        self.deck = Deck(num_decks, seed)
        self.deck.load_from_file("baralho.txt")
        self.cards = self.deck.cards

    def initialize_game(self):
        self.current_card = random.choice(self.deck.cards)
        self.deck.cards.remove(self.current_card)

        for player in self.activePlayers:
            player.init_output_file()
            for _ in range(5):
                if self.deck.cards:
                    carta = self.deck.dar_carta()
                    if carta in self.deck.cards:
                        self.deck.cards.remove(carta)
                    else:
                        self.log_error("Carta não encontrada no deck.")
                    player.cartas_mao.append(carta)
                    player.deck = self.deck
                else:
                    self.log_error("Baralho vazio - Encerrando jogo atual")
                    break  

    def load_players(self, arquivo):
        players = []
        player_info = []
        
        with open(arquivo, 'r') as file:
            lines = file.read().splitlines()
            #for line in lines[1:]:
            #    # Separe a linha em nome e cpf
            #    parts = line.split('--')
            #    nome, cpf = parts[0], parts[1]
            #    # Defina o saldo como None por padrão
            #    saldo = None
            #    if len(parts) > 2:
            #        saldo = int(parts[2])  # Se houver um terceiro valor, use-o como saldo
            game_info = file.readline().strip().split("--")

            #print(game_info)
            players_info = [line.strip() for line in lines[1:]]
            _ , game_number = arquivo.split("_")
            game_number,_ = game_number.split(".")
            print(game_number)
            print(f"ESTAMOS AQUI{players_info}")
            for player_info in players_info:
                print(player_info)
                nome, cpf = player_info.strip().split("--")
                jogador = JogadorUno( nome, cpf, 0, game_number)
                players.append(jogador)
                print("AQUIKKKKKKK")
                print(jogador)    
            

        return players

    def start_game(self):
        self.initialize_game()
        winner = None

        with open(self.output_filename, 'a+') as file:
            file.write(f"Começando jogo {self.game_number}\n")

        for round_number in range(self.rounds):
            self.report_round_start(round_number + 1)
            self.seed += 1
            self.deck.embaralhar(self.seed)
            try:
                print(self.activePlayers)
                for player in self.activePlayers:
                    self.display_current_card()
                    self.display_player_hand(player)
                    if self.is_winner(player):
                        winner = player
                        break
                    self.current_card = self.play_turn(player, self.current_card)
                if winner:
                    self.report_winner(winner)

            except ErrorExitCondition as e:
                self.log_error(str(e))
                break
            except ErrorInvalidBalance as e:
                self.log_error(str(e))
            except Exception as e:
                self.log_error(f"Erro não tratado: {str(e)}")

        if not winner:
            # Encontre o jogador com menos cartas na mão
            winner = min(self.activePlayers, key=lambda player: len(player.cartas_mao))
            self.report_winner(winner)


    def report_winner(self, player):
        with open(self.output_filename, "a+") as file:
            file.write(f"Vencedor: Jogador: {player.nome} CPF: {player.cpf} Número cartas: {len(player.cartas_mao)}\n")

    def report_draw(self):
        with open(self.output_filename, 'a+') as file:
            file.write("Empate! Nenhum jogador possui mais cartas.\n")


    def display_current_card(self):
        print("ESTAMOS AQUIKKKKKKKK")
        with open(self.output_filename, 'a+') as file:
            file.write(f"Carta atual: {self.current_card['valor']} de {self.current_card['naipe']}\n")
        print(f"Carta atual: {self.current_card['valor']} de {self.current_card['naipe']}")

    def carta_mesa_atual(self, card):
        print(f"Carta atual na mesa: {card['valor']} de {card['naipe']}")

    def play_turn(self, player, current_card):
        carta_mesa = current_card
        try:
            self.carta_mesa_atual(carta_mesa)
            jogou = False
            carta_um = player.fazerJogada(carta_mesa)

            if carta_um is not carta_mesa:
                jogou = True
                return carta_um

            if not jogou:
                
                carta_comprada = self.deck.dar_carta()
                player.cartas_mao.append(carta_comprada)
                if carta_comprada in self.deck.cards:
                    self.deck.cards.remove(carta_comprada)
                else:
                    raise ErrorEmptyDeck("Baralho vazio - Encerrando jogo atual")
        except ErrorExitCondition as e:
            self.log_error(str(e))
            # Atribua 16 ou realize a ação apropriada

        except ErrorInvalidBalance as e:
            self.log_error(str(e))
            # Atribua 1 ou realize a ação apropriada

        except Exception as e:
            # Outra exceção não tratada - registre o erro e continue
            self.log_error(f"Erro não tratado: {str(e)}")

        return carta_mesa

    def init_output_file(self):
        pass

    def log_error(self, error_message):
        with open(self.log_filename, 'a+') as file:
            file.write(f'ERRO: {error_message}\n')

    def get_winner(self):
        winner = min(self.activePlayers, key=lambda player: len(player.cartas_mao))
        return winner

    def is_winner(self, player):
        len(player.cartas_mao) == 0

    def report_round_start(self, round_number):
        with open(self.output_filename, 'a+') as file:
            file.write(f'Começando Rodada {round_number}\n')


    def display_player_hand(self, player):
        with open(self.output_filename, 'a+') as file:
            file.write(f"Cartas de {player.nome}:\n")
            for i, card in enumerate(player.cartas_mao):
                file.write(f"{i}: {card['valor']} de {card['naipe']}\n")
                print(f"{i}: {card['valor']} de {card['naipe']}")
