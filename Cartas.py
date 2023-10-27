import random
import os

class ErrorSeed(Exception):
    def __init__(self, msg):
        self.msg = msg
class ErrorDeck(Exception):
    def __init__(self, msg):
        self.msg = msg
class Deck:
    def __init__(self, num_decks=1, seed=None):
        self.num_decks = num_decks
        self.seed = seed  # Defina a semente aqui

        if num_decks > 6:
            self.num_decks = 6
            raise ErrorDeck("Número máximo de decks permitidos: 6")

        if seed is not None:
            self.seed = seed

        self.cards = self.baralhos()
        self.embaralhar()

    def baralhos(self):
        naipes = ['Paus', 'Ouros', 'Copas', 'Espadas']
        valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valete', 'Dama', 'Rei', 'As']
        baralho = [{'naipe': naipe, 'valor': valor} for naipe in naipes for valor in valores]
        if isinstance(self.num_decks, int) and self.num_decks > 0:
            return baralho * self.num_decks
        else:
            raise ValueError("Número de baralhos inválido")
        
    def carregar_baralho(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                naipe, valor = line.strip().split(" de ")
                carta = {'valor': valor, 'naipe': naipe}
                self.cards.append(carta)

    def embaralhar(self, seed=None):
        if seed is not None:
            self.seed = seed
        if self.seed is not None:
            random.seed(self.seed)
            random.shuffle(self.cards)
            self.save_to_file("baralho.txt")
        else:
            raise ErrorSeed("Seed invalida")
        
    
    def dar_carta(self):
        if self.cards:
            selected_card = self.cards.pop(0)  # Remove a primeira carta da lista
            self.save_to_file("baralho.txt")  # Salva as alterações no arquivo

            naipe, valor = selected_card['naipe'], selected_card['valor']
            carta = {'valor': valor, 'naipe': naipe}

            return carta
        else:
            print("O baralho está vazio.")
            return None

    def print_deck(self):
        for card in self.cards:
            print(f"{card['valor']} de {card['naipe']}")

    def get_deck_size(self):
        return len(self.cards)
    
    def save_to_file(self, file):
        with open(file,"w") as file:
            for card in self.cards:
                file.write(f"{card['valor']} de {card['naipe']}\n")


    def load_from_file(self,file):
        baralho = []
        with open(file,"r") as file :
            lines = file.readlines()
            for line in lines:
                naipe, valor = line.strip().split(" de ")
                baralho.append({'naipe': naipe, 'valor': valor})
        return baralho
    def get_deck_value(self, string) ->int : 
        pass
