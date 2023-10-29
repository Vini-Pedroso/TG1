# ViniciusGabriel

# Sistema de Jogos de Cartas em Python

Este é um sistema de jogos de cartas em Python que oferece a funcionalidade de jogar dois jogos populares de cartas: Blackjack e Uno. Você pode usar este sistema para jogar os jogos ou como base para desenvolver seus próprios jogos de cartas.

## Requisitos de Sistema

- Python 3.6 ou superior.
- Bibliotecas Python: Nenhuma biblioteca externa é necessária.

## Instalação

1. Clone ou faça o download deste repositório para o seu computador.

2. Navegue até o diretório raiz do projeto.

3. Execute o aplicativo com o seguinte comando:

   ```bash
   python APP.py jogo_1.txt


Agora você está pronto para jogar Blackjack e Uno no sistema de jogos de cartas!

#Como Jogar o Blackjack
O Blackjack é um jogo de cartas em que o objetivo é somar cartas para chegar o mais próximo possível de 21, sem ultrapassar esse valor.

Inicie um jogo de Blackjack com o comando apropriado (consulte a seção de instalação).

Siga as instruções no terminal para adicionar jogadores ao jogo.

Após a configuração, siga as instruções para fazer jogadas e tomar decisões durante o jogo.

O jogo continuará até que um vencedor seja determinado com base nas regras do Blackjack.

#Como Jogar o Uno
O Uno é um jogo de cartas em que os jogadores tentam descartar todas as suas cartas, seguindo as regras do jogo.

Inicie um jogo de Uno com o comando apropriado (consulte a seção de instalação).

Siga as instruções no terminal para adicionar jogadores ao jogo.

Após a configuração, siga as instruções para fazer jogadas e tomar decisões durante o jogo.

O jogo continuará até que um vencedor seja determinado com base nas regras do Uno.

##Classes
Classe Jogador
A classe base Jogador representa um jogador genérico de jogos de cartas.
Classe JogadorUno
A classe JogadorUno é específica para o jogo Uno, com métodos para fazer jogadas e atribuir cartas.
Classe Uno
A classe Uno é responsável por gerenciar o jogo Uno, incluindo a inicialização e as regras do jogo.
Classe Blackjack
A classe Blackjack lida com o jogo de Blackjack, incluindo as regras e a lógica do jogo.
Exemplos de Uso
Aqui estão alguns exemplos de código para iniciar jogos e adicionar jogadores:


# Iniciar um jogo Uno
game_number = 1
uno_game = Uno(num_players=4, num_decks=2, seed=12345, rounds=5, game_number=game_number)

# Adicionar jogadores ao jogo Uno
player1 = JogadorUno(nome="Alice", cpf="12345678901", saldo=100)
player2 = JogadorUno(nome="Bob", cpf="98765432109", saldo=50)
uno_game.adicionar_jogador(player1)
uno_game.adicionar_jogador(player2)

# Iniciar um jogo de Blackjack a partir de um arquivo
arquivo = "jogo_3.txt"
Blackjack.inicia_BlackJack_jogo(arquivo)

# Leitura do Blackjack
Na leitura dos outputs do jogo, devemos nos atentar que o saldo exibido está relacionado já com a rodada impressa, ou seja. Se na rodada o jogador perde, no seu print seu saldo já será 0, pois ele já perdeu.
As escritas estão formatados com frases a mais que tem como objetivo tentar esclarecer o que acontece em cada jogada.  
