from abc import ABC, abstractmethod

class Jogador(ABC):
    def __init__(self, nome, cpf, saldo):
        self.nome = nome
        self.cpf = cpf
        self.saldo = saldo
        self.cartas = []

    @abstractmethod
    def fazerJogada(self):
        pass

    @abstractmethod
    def atribuirCarta(self, carta):
        pass
    
    @property
    def Nome(self):
        return self.nome

    @property
    def CPF(self):
        return self.cpf

    @property
    def Saldo(self):
        return self.saldo

    @property
    def Cartas(self):
        return self.cartas
    
    @Nome.setter
    def Nome(self, nome):
        self.nome = nome

    @CPF.setter
    def CPF(self, cpf):
        self.cpf = cpf

    @Saldo.setter
    def Saldo(self, saldo):
        self.saldo = saldo

    @Cartas.setter
    def Cartas(self, cartas):
        self.cartas = cartas


    def adicionarCarta(self, carta):
        self.cartas.append(carta)


    def __str__(self):
        return f"Nome: {self.nome}\nCPF: {self.cpf}\nSaldo: {self.saldo}\nCartas: {', '.join(self.cartas)}"

class JogadorBlackjack(Jogador):
    def fazerJogada(self):
        pass

    def atribuirCarta(self, carta):  
        pass
      
#exemplo de teste:
jogador1 = JogadorBlackjack("Alice", "1234567890", 1000)
jogador1.adicionarCarta("Ás de Espadas")
jogador1.adicionarCarta("Rei de Copas")
print(jogador1)
