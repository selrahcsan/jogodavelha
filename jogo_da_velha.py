import os

# Tabuleiro do Jogo da Velha
tabuleiro = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]

# Códigos de cor ANSI
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"

# Função para Limpar a Tela 
def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função que, dado um tabuleiro, exibe esse tabuleiro de Jogo da Velha no console.
def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)

# Função que, dado um tabuleiro e jogador, verifica se esse jogador venceu o jogo.
def verificar_vencedor(tabuleiro, jogador):
    # Verificar linhas
    for linha in tabuleiro:
        if all([posicao == jogador for posicao in linha]):
            return True

    # Verificar colunas
    for coluna in range(3):
        if all([tabuleiro[linha][coluna] == jogador for linha in range(3)]):
            return True

    # Verificar diagonais
    if all([tabuleiro[i][i] == jogador for i in range(3)]) or \
       all([tabuleiro[i][2 - i] == jogador for i in range(3)]):
        return True

    return False

# Função que, dado um tabuleiro, verifica se o jogo terminou em empate.
def verificar_empate(tabuleiro):
    for linha in tabuleiro:
        if any([posicao.isdigit() for posicao in linha]):
            return False
    return True

# Função principal que implementa o jogo da velha.
def jogo_da_velha():
    tabuleiro = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"]
    ]
    jogador_atual = "X"

    while True:
        exibir_tabuleiro(tabuleiro)

        # Solicitar a jogada do jogador
        try:
            jogada = int(input(f"Jogador {jogador_atual}, escolha uma posição (1-9): ")) - 1
            limpa_tela()
        except ValueError:
            input("\033[31mEntrada inválida\033[0m.\nPor favor, insira um número entre 1 e 9.\nAperte qualquer tecla para continuar...")
            limpa_tela()
            continue

        # Verificar se a jogada é válida
        if jogada < 0 or jogada > 8:
            input("\033[31mPosição inválida.\033[0m\nEscolha um número entre 1 e 9.\nAperte qualquer tecla para continuar...")
            limpa_tela()
            continue

        linha = jogada // 3
        coluna = jogada % 3

        if tabuleiro[linha][coluna] in ["X", "O"]:
            input("\033[31mPosição já ocupada.\033[0m\nEscolha outra posição.\nAperte qualquer tecla para continuar...")
            limpa_tela()
            continue

        # Fazer a jogada
        tabuleiro[linha][coluna] = jogador_atual

        # Verificar se o jogador atual venceu
        if verificar_vencedor(tabuleiro, jogador_atual):
            exibir_tabuleiro(tabuleiro)
            print(f"Parabéns! O jogador {jogador_atual} venceu!")
            break

        # Verificar se o jogo terminou em empate
        if verificar_empate(tabuleiro):
            exibir_tabuleiro(tabuleiro)
            print("O jogo terminou em empate!")
            break

        # Alternar entre os jogadores
        jogador_atual = "O" if jogador_atual == "X" else "X"

# Iniciar o jogo
if __name__ == "__main__":
    limpa_tela()
    jogo_da_velha()