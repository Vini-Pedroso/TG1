import random
import os

class ErrorSeed(Exception):
    def __init__(self, msg):
        self.msg = msg

class Deck:
    def __init__(self, num_decks=1):
        self.num_decks = num_decks
        if num_decks > 6:
            self.num_decks = 6
            raise ErrorSeed("Número máximo de decks permitidos: 6\n Setando automáticamente o número de decks para 6")
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
    
    def dar_carta(self):
        with open("baralho.txt" , "r+") as file:
            lines = file.readlines()
            selected_card = lines[0]
            lines.remove(selected_card) # remove a carta que foi pega 
            file.seek(0) #escreve no primeiro espaço o baralho sem a carta selecionada
            file.writelines(lines) 
            return selected_card
        

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
                line = line .split("de")
                naipe, valor = line
                baralho.append({'naipe': naipe, 'valor': valor})
        print(baralho)
        return baralho
            

        
# Exemplo de uso:
if __name__ == "__main__":
    deck = Deck(num_decks=1)  # Criar um deck com dois baralhos
    deck.shuffle(seed=101)     # Embaralhar o deck com semente 42
    deck.save_to_file("baralho.txt")  # Salvar o deck em um arquivo

    # Carregar o deck de um arquivo
    #deck.load_from_file("baralho.txt")

    # Imprimir o deck carregado
    deck.print_deck()
    tamanho_decks = deck.get_deck_size()
    print("tamanho do baralho é: ", tamanho_decks)
    print();print() ;print() 
    deck.dar_carta() ;deck.dar_carta()
    deck.load_from_file("baralho.txt")
    #deck.print_deck()

