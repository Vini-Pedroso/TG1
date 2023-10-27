import random
from jogador import Jogador
from cartas import Deck


class ErrorCPF(Exception):
    def __init__(self, msg):
        self.msg = msg

class BaralhoVazioException(Exception):
    pass

class JogadorUno(Jogador):
    def __init__(self, nome, cpf, saldo, game_number):
        super().__init__(nome, cpf, saldo)
        self.cartas_mao = []
        self.cpf = str(cpf)
        if len(cpf) != 11:
            raise ErrorCPF(f"{nome} ESTÁ COM CPF INVALIDO")
        self.game_number = game_number
        self.output_filename = f'jogo_{self.game_number}.saida'
        self.log_filename = f'jogo_{self.game_number}.log'
        self.init_output_file()  # Inicialize o arquivo de saída

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
    

    def init_output_file(self):
        with open(self.output_filename, 'w') as file:
            file.write(f'Comecando jogo {self.game_number}\n')
          
    def log_error(self, error_message):
        with open(self.log_filename, 'a') as file:
            file.write(f'ERRO: {error_message}\n')

    def report_round_start(self, round_number):
        with open(self.output_filename, 'a') as file:
            file.write(f'Comecando Rodada {round_number}\n')

    def report_winner(self, winner):
        with open(self.output_filename, 'a') as file:
            file.write(f'Vencedor: Jogador: {winner.nome} CPF: {winner.cpf} '
                       f'Numero cartas: {len(winner.cartas_mao)}\n')

    def atribuirCarta(self, carta):
        try:
            self.cartas_mao.append(carta)
        except BaralhoVazioException:
            # Tratar a exceção e encerrar o jogo, se necessário
            # Você pode definir a lógica apropriada para encerrar o jogo quando o baralho estiver vazio
            self.encerrarJogo()


    def fazerJogada(self, carta_mesa):
        jogadas_validas = [carta for carta in self.cartas_mao if carta['naipe'] == carta_mesa['naipe'] or carta['valor'] == carta_mesa['valor']]

        if len(jogadas_validas) > 0:
            # O jogador tem pelo menos uma jogada válida
            carta = jogadas_validas[0]
            self.cartas_mao.remove(carta)
            if not self.cartas_mao:
                print(f"{self.nome} ganhou o jogo")
            return carta

        else:
            # O jogador não tem jogadas válidas, então ele compra uma carta
            carta_comprada = self.comprar_carta(carta_mesa)
            print(f"{self.nome} comprou uma carta: {carta_comprada['valor']} de {carta_comprada['naipe']}")
            if not self.cartas_mao:
                print(f"{self.nome} ganhou o jogo")
            return carta_mesa


    def comprar_carta(self, carta_mesa):
        meu_deck = Deck(seed=101) 
        meu_deck.load_from_file("baralho.txt")  
        nova_carta = meu_deck.dar_carta()
        self.cartas_mao.append(nova_carta)
        return nova_carta

    def is_valid_play(self, card, carta_mesa):
        return card['naipe'] == carta_mesa['naipe'] or card['valor'] == carta_mesa['valor']
