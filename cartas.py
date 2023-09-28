import random
import os

class ErrorSeed(Exception):
    def __init__(self, msg):
        self.msg = msg

class Deck:
    def __init__(self, num_decks=1):
        self.num_decks = num_decks
        self.cards = self.baralhos()
        
    def baralhos(self):
        naipes = ['Paus', 'Ouros', 'Copas', 'Espadas']
        valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valete', 'Dama', 'Rei', 'Ás']
        baralho = [{'naipe': naipe, 'valor': valor} for naipe in naipes for valor in valores]
        return baralho * self.num_decks
    
    def shuffle(self, seed=101):
        if seed == 101:
            random.seed(101)
            random.shuffle(self.cards)
        else:
            raise ErrorSeed("Seed invalida")
            
    def print_deck(self):
        for card in self.cards:
            print(f"{card['valor']} de {card['naipe']}")

    def get_deck_size(self):
        return len(self.cards)
# Exemplo de uso:
if __name__ == "__main__":
    deck = Deck(num_decks=4)  # Criar um deck com dois baralhos
    deck.shuffle(seed=101)     # Embaralhar o deck com semente 42
    deck.save_to_file("baralho.txt")  # Salvar o deck em um arquivo

    # Carregar o deck de um arquivo
    deck.load_from_file("baralho.txt")

    # Imprimir o deck carregado
    deck.print_deck()
    tamanho_decks = deck.get_deck_size()
    print("tamanho do baralho é: ", tamanho_decks)
