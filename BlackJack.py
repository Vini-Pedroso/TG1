from TG1.Jogador import Jogador


class JogadorBlackjack(Jogador):
    def __init__(self, nome, cpf, saldo, condParada):
        super().__init__(nome, cpf, saldo)
        self.condParada = condParada
    def fazerJogada(self):
        #if self.saldo == 0:
        pass
    def atribuirCarta(self, carta):  
        pass
 

activePlayers = []
with open ("jogo.txt, r") as file:
        for count in enumerate(file): #descobre quantas linhas tem
            pass
        filelen = count #precisariamos usar +1, mas estamos descontando a primeira linha
        partes = file.strip("--")
        for i in range(1,filelen):
            jogador = JogadorBlackjack(partes[0],partes[1],partes[2])

            
jogador1 = JogadorBlackjack("Alice", "1234567890", 1000)
jogador1.adicionarCarta("Ás de Espadas")
jogador1.adicionarCarta("Rei de Copas")
print(jogador1)
