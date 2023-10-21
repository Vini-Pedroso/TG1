import random
from jogador import Jogador  # Certifique-se de importar a classe Jogador do pacote correto.
from cartas import Deck
class ErrorCPF(Exception):
    def __init__(self, msg):
        self.msg = msg
class JogadorUno(Jogador):
    def __init__(self, nome, cpf, condParada, deck):
        super().__init__(nome, cpf, saldo=0)
        self.cartas_mao = []
        self.cpf = str(cpf)
        self.condParada = condParada
        if len(cpf) != 11:
            raise ErrorCPF(f" {nome} ESTÁ COM CPF INVALIDO")
        self.deck = deck
    
    def fazerJogada(self, carta_mesa):
        jogadas_validas = [carta for carta in self.cartas_mao if carta['naipe'] == carta_mesa['naipe'] or carta['valor'] == carta_mesa['valor']]
        valid_play = False

        while not valid_play:
            self.display_player_hand()
            if self.is_winner():
                self.report_winner()
                return None  # Adicione um retorno aqui para indicar que o jogador não jogou uma carta válida

            card_index = int(input(f"Vez do Jogador {self.nome}. Escolha uma carta para jogar (0 a {len(self.cartas_mao) - 1}): "))

            if card_index >= 0 and card_index < len(self.cartas_mao):
                selected_card = self.cartas_mao[card_index]

                if self.is_valid_play(selected_card, carta_mesa):
                    self.cartas_mao.remove(selected_card)
                    carta_mesa = selected_card
                    valid_play = True
                else:
                    print("Jogada inválida. Tente novamente.")
            else:
                print("Índice de carta inválido. Tente novamente.")
        
        return carta_mesa  # Retorne a carta jogada

    def is_valid_play(self, card, carta_mesa):
        if card['naipe'] == carta_mesa['naipe'] or card['valor'] == carta_mesa['valor']:
            return True
        return False

    def display_player_hand(self):
        print(f"Cartas de {self.nome}:")
        for i, card in enumerate(self.cartas_mao):
            print(f"{i}: {card['valor']} de {card['naipe']}")

    def is_winner(self):
        return len(self.cartas_mao) == 0

    def report_winner(self):
        with open("jogo_resultado.txt", "a") as file:
            file.write(f"Vencedor: Jogador: {self.nome} CPF: {self.cpf} Número cartas: {len(self.cartas_mao)}\n")


    # SOBRECARGA DE OPERADORES:
    def __gt__(self, other):
        return len(self.cartas_mao) > len(other.cartas_mao)

    def __lt__(self, other):
        return len(self.cartas_mao) < len(other.cartas_mao)

    def __ge__(self, other):
        return len(self.cartas_mao) >= len(other.cartas_mao)

    def __le__(self, other):
        return len(self.cartas_mao) <= len(other.cartas_mao)

    def __eq__(self, other):
        return len(self.cartas_mao) == len(other.cartas_mao)

    def __ne__(self, other):
        return len(self.cartas_mao) != len(other.cartas_mao)
    
    def comprar_carta(self):
        carta_comprada = self.deck.dar_carta()

        if self.is_valid_play(carta_comprada, self.current_card):
            self.cartas_mao.append(carta_comprada)
            self.deck.cards.remove(carta_comprada)
        else:
            self.deck.descartar_carta(carta_comprada)

    def atribuirCarta(self, carta):
        self.cartas_mao.append(carta)
