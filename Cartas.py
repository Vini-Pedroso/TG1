import random
import os

class ErrorSeed(Exception):
    def __init__(self, msg):
        self.msg = msg
class Deck:
    def __init__(self, num_decks=1):
        self.num_decks = num_decks
        self.seed = None
        self.cards = self.baralhos()
        if num_decks > 6:
            self.num_decks = 6
            raise ErrorSeed("Número máximo de decks permitidos: 6\n Setando automáticamente o número de decks para 6")
        self.cards = self.baralhos()
        with open("baralho.txt","w") as file:
            for card in self.cards:
                file.write(f"{card['valor']} de {card['naipe']}\n")
        

    def baralhos(self):
        naipes = ['Paus', 'Ouros', 'Copas', 'Espadas']
        valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valete', 'Dama', 'Rei', 'As']
        baralho = [{'naipe': naipe, 'valor': valor} for naipe in naipes for valor in valores]
        return baralho * self.num_decks
    

    def embaralhar(self, seed=None):
        if seed is not None:
            self.seed = seed
        if self.seed is not None:
            random.seed(seed)
            random.shuffle(self.cards)
        else:
            raise ErrorSeed("Seed invalida")
    
    def dar_carta(self):
        with open("baralho.txt" , "r+") as file:
            lines = file.readlines()
            selected_card = lines[0]
            lines.pop(0) # remove a carta que foi pega 
            file.seek(0) #aponta para o primeiro espaço do arquivo
            file.truncate() #tira tudo que tem no arquivo (precisa do seek antes)
            file.writelines(lines) #reescreve sem a carta removida
        naipe, valor = selected_card.strip().split(" de ")
        return {'valor': valor, 'naipe': naipe}
        

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
    def get_deck_value(self, string) ->int : 
        pass
