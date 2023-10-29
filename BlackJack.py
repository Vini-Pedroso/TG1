from Jogador import Jogador
from Cartas import Deck
class ErrorEmptyDeck(Exception):
    def __init__(self, msg="Baralho vazio"):
        self.msg = msg
        super().__init__(self.msg)
class ErrorSeed(Exception):
    def __init__(self, msg):
        self.msg = msg
class ErrorCPF(Exception):
    def __init__(self, msg):
        self.msg = msg

#Aqui começa a preparação para o jogo
def inicia_BlackJack_jogo(arquivo):
    nomeArquivo,_ = arquivo.split(".")
    _,numArquivo = nomeArquivo.split("_")
    
    arquivosaida = f"saidas/jogo_{numArquivo}.saida" 
    
    class JogadorBlackjack(Jogador):
        def __init__(self, nome, cpf, saldo, condParada):
            super().__init__(nome, cpf, saldo)
            self.condParada = int(condParada)
            if len(cpf) != 11:
                with open(f"saidas/jogo_{numArquivo}.log", 'a+') as file:
                    file.write(f"ErrorCPF!\n{nome} ESTÁ COM CPF INVALIDO")
                raise ErrorCPF(f"{nome} ESTÁ COM CPF INVALIDO")
            self.cartas = []
            self.parou = False 
        def reseta_cartas(self):
            self.cartas = []
        def reseta_parou(self):
            self.parou = False
        def __str__(self):
            return(f"Jogador: {self.nome}  CPF:{self.cpf} pontos: {self.get_somatorio()} saldo: {self.saldo}")
        #__str__ confrome o exemplo de saida

        def fazerJogada(self):
            if self.get_somatorio() < self.get_condParada():
                self.atribuirCarta()
            else:
                self.parou = True

        def atribuirCarta(self):  
            if deck.dar_carta() is  None: #aqui vamos precisar tratar o erroo 
                raise ErrorEmptyDeck
            self.cartas.append(deck.dar_carta())

        def get_condParada(self):
            return self.condParada
    
        def get_somatorio(self) ->int :  #faz o somatório das cartas do jogador 
            sum = 0
            
            for carta in self.cartas:
                value = get_deck_value(carta)
                
                if value == 11 and sum + value >21:
                    sum+=1
                else:
                    sum += value
                
            return sum 
            #SOBRECARGAS DE OPERADORES
        def __add__(self, valor):
            if isinstance(valor, (int, float)):
                self.saldo += valor
            else:
                raise TypeError("Valor incorreto. Certifique-se de que você está adicionando um número")

        def __sub__(self, valor):
            if isinstance(valor, (int, float)):
                self.saldo -= valor
            else:
                raise TypeError("Valor incorreto. Certifique-se de que você está adicionando um número")

        def __mul__(self, valor):
            if isinstance(valor, (int, float)):
                self.saldo *= valor
            else:
                raise TypeError("Valor incorreto. Certifique-se de que você está adicionando um número")
        def vitoria(self):
             self =  self + self.saldo 

        def derrota(self):
            self.saldo = 0

        def testa_blackjack(self):
            tem_as = False
            tem_dez = False
            for carta in self.cartas:
                value = get_deck_value(carta)
                if value == 11:    #Verifica se tem As
                            tem_as = True
                            
                elif value == 10:  # Verifica se a carta tem 10 pontos (Valete, Dama ou Rei)
                    tem_dez= True
                    
                    
            if len(self.cartas) == 2 and tem_as and tem_dez:
                self = self.saldo * 3
               
               
    def get_deck_value(carta) ->int : 
            result = carta['valor']
            
            if (result == "Valete") or  (result == "Dama") or (result == "Rei"):
                return 10
            elif (result == "As"):
                return 11
            else:
                return int(result) 

    


    def escreve_no_arquivo(string):

        with open(arquivosaida, 'a+') as file:
            file.write(string)
    dealer = JogadorBlackjack("Dealer", "00000000000", 1, 17) #instanciando o dealer 
    activePlayers = []


    jogadores = []
    with open(arquivo,"r") as file:
            #Aqui lemos o arquivo, e obtemos as infos sobre o jogo e sobre os jogadores que 
            #jogarão a partida 
            line = file.readline().split("--") 
            nomeJogo,NumeroJogadores,NumeroBaralhos,seed,rodadas = str(line[0]) , int(line[1]), int(line[2]), int(line[3]), int(line[4]) 
            #Nesta linha fazemos os casts
            lines = file.readlines() #ponteiro está na segunda linha já. Entao nao precisamos nos preocupar como que for lido 
            if NumeroBaralhos <=0:
                with open(f"saidas/jogo_{numArquivo}.log", 'a+') as file:
                    file.write(f"\nAtencao: Numero de baralhos é 0\n Setando numero de baralhos para o padrao (1)\n")
                #joga warning que nao tem baralho
            for line in lines:
                line = line.split("--")
                nome,cpf,saldo,condParada = str(line[0]) , str(line[1]), int(line[2]), int(line[3]) #cast 
                #Tratando erros
                if condParada <=0:
                    condParada = 16
                if saldo < 0:
                    saldo = 1

                jogador = JogadorBlackjack(nome,cpf,saldo,condParada)
                jogadores.append(jogador)
            if len(jogadores) != NumeroJogadores:
                with open(f"saidas/jogo_{numArquivo}.log", 'a+') as file:
                    file.write(f"ValueError!\n Número de jogadores não corresponde com o numero de jogadores atribuídos")
                raise ValueError("Número de jogadores não corresponde com o numero de jogadores atribuídos")



    for player in jogadores:
        activePlayers.append(player) #adiciona os jogadores 
    
    deck = Deck(NumeroBaralhos, seed)
    deck.embaralhar(seed)
    deck.save_to_file("baralho.txt") #cria, embaralha e salva o deck

    escreve_no_arquivo(f"Começando jogo {numArquivo}\n")
    #começa o jogo 
    
    condParada = False #flag para ficar tentando distribuir cartas 

    i = 1
    while(i<=rodadas): #quantidade de rodadas
        condParada = False
        dealer.reseta_cartas()
        dealer.reseta_parou()
        for player in activePlayers:
            player.reseta_cartas()   #reseta tudo 
            player.reseta_parou()
        if len(activePlayers) == 0:
            escreve_no_arquivo("Não existem mais jogadores para jogar\n Encerrando jogo.")
            break
        for player in activePlayers:
            while(condParada != True):
                condParada = True # bota a cond de Parada para True como padrao 
                for player in activePlayers:
                    if player.parou == False: # se nao parou:
                        condParada = False          #ainda quer carta
                        player.fazerJogada()              #faz a jogada, nela testa novamente se vai parar 
                dealer.fazerJogada()
            
            
        escreve_no_arquivo(f"Rodada {i}:\n")
        
        
        escreve_no_arquivo(str(dealer)+ "\n\n")
        for player in activePlayers:
            if player.get_somatorio() == 21:
                player.testa_blackjack()

            if dealer.get_somatorio()>21:
                player.vitoria()

            elif player.get_somatorio() > 21:
                player.derrota()
    
            elif player.get_somatorio() > dealer.get_somatorio():
                player.vitoria()
            
            elif player.get_somatorio() == dealer.get_somatorio():
                pass
            elif player.get_somatorio() < dealer.get_somatorio():
                player.derrota()
            escreve_no_arquivo(str(player)+ "\n\n")
        players_to_remove = []  # Crie uma lista para armazenar jogadores a serem removidos

        for player in activePlayers:
            if player.saldo <= 0:
                # Ficou sem saldo
                escreve_no_arquivo(f"Jogador {player.nome} saiu do jogo pois não tinha saldo\n\n")
                
                players_to_remove.append(player)  # Adicione o jogador à lista de jogadores a serem removidos

        for player in players_to_remove:
            activePlayers.remove(player)  # Remova os jogadores que ficaram sem saldo da lista
            
                
        i+=1