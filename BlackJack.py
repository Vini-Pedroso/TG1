from Jogador import Jogador
import cartas 


class ErrorSeed(Exception):
    def __init__(self, msg):
        self.msg = msg


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
jogadores = []
with open("jogo.txt","r") as file:
        #Aqui lemos o arquivo, e obtemos as infos sobre o jogo e sobre os jogadores que 
        #jogarão a partida 
        line = file.readline().split("--") 
        nomeJogo,NumeroJogadores,NumerosBaralhos,seed,rodadas = str(line[0]) , int(line[1]), int(line[2]), int(line[3]), int(line[4]) 
        #Nesta linha fazemos os casts
        if nomeJogo != "Blackjack":
            raise ErrorSeed("Não é este o jogo")
        lines = file.readlines() #ponteiro está na segunda linha já. Entao nao precisamos nos preocupar como que for lido 
    

        for line in lines:
            line = line.split("--")
            nome,cpf,saldo,condParada = str(line[0]) , str(line[1]), int(line[2]), int(line[3]) #cast 
            jogador = JogadorBlackjack(nome,cpf,saldo,condParada)
            jogadores.append(jogador)



for player in jogadores:
     if (player.saldo > 0): # teste se tem saldo para jogar
        activePlayers.append(player)
for player in activePlayers:
    print(player)

