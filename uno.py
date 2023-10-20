import random
from jogador import Jogador
from cartas import Deck
from jogadorUno import JogadorUno
class Uno:
    def __init__(self, num_players):
        self.num_players = num_players
        self.activePlayers = []
        self.current_player = 0
        self.seed= 101
        self.current_card = None
        self.deck = Deck(num_decks=1)
        self.deck.embaralhar(seed=101)
        self.load_players()

    
    def initialize_game(self):
        #Primeira carta
        self.seed += 1
        self.deck.embaralhar(seed=self.seed)
        self.current_card = random.choice(self.deck.cards)  # Alterei para escolher aleatoriamente
        self.deck.cards.remove(self.current_card)  # Remova a carta da lista

        #começando o jogo com 5 cartas para cada jogador
        for player in self.activePlayers:
            for _ in range(5):
                carta = self.deck.dar_carta()
                player.cartas_mao.append(carta)
                self.deck.cards.remove(carta)  # Remova a carta da lista do deck


    def load_players(self):
        for i in range(self.num_players):
            nome = input(f"Nome do Jogador {i + 1}: ")
            cpf = input(f"CPF do Jogador {i + 1}: ")
            saldo = 0
            player = JogadorUno(nome, cpf, saldo, self.deck)
            self.activePlayers.append(player)

        for player in self.activePlayers:
            for carta in player.cartas_mao:
                if carta in self.deck.cards:
                    self.deck.cards.remove(carta)

        for player in self.activePlayers:
            for carta in player.cartas_mao:
                if carta not in self.deck.cards:
                    print(f"Erro: Carta {carta} não encontrada no deck.")

    def start_game(self):
        while True:
            self.initialize_game()
            for player in self.activePlayers:
                print(f"Vez do Jogador {player.nome}")
                self.display_current_card()
                self.display_player_hand(player)

                if self.is_winner(player):
                    self.report_winner(player)
                    return

                self.play_turn(player)

                if len(self.deck.cards) == 0:
                    #baralho vazio, logo..
                    winner = min(self.activePlayers)
                    self.report_winner(winner)
                    return

    def display_current_card(self):
        print(f"Carta atual: {self.current_card['valor']} de {self.current_card['naipe']}")

    def display_player_hand(self, player):
        print(f"Cartas de {player.Nome}:")
        for i, card in enumerate(player.Cartas):
            print(f"{i}: {card['valor']} de {card['naipe']}")

    def is_winner(self, player):
        return len(player.Cartas) == 0

    def report_winner(self, player):
        with open("jogo_resultado.txt", "a") as file:
            file.write(f"Vencedor: Jogador: {player.nome} CPF: {player.CPF} Número cartas: {len(player.Cartas)}\n")
    
    def play_turn(self, player):
        carta_mesa = self.current_card

        while True:
            carta_mesa = player.fazerJogada(carta_mesa)

            if player.is_winner():
                self.report_winner(player)
                return carta_mesa

            if len(self.deck.cards) == 0:
                winner = min(self.activePlayers, key=len)
                self.report_winner(winner)
                return carta_mesa
