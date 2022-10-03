# --------------- CONFIGURAÇÕES INICIAIS ---------------
# importando bibliotecas:
import pygame
from sys import exit

# definindo configurações iniciais:
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Kikinho, o gênio da tabela periódica")
icon = pygame.image.load("imagens\icon.png")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
fonte = pygame.font.Font("fontes\PixeloidSans.ttf", 30)

# definindo variáveis e importando superfícies (imagens):
fundo_sup = pygame.image.load(r"imagens\background.png")
kikinho_sup = pygame.image.load("imagens\kikinho.png")
speechBubble_sup = pygame.image.load("imagens\speechBubble.png")

# --------------- MAIN LOOP ---------------
while True:
    # mais configurações básicas:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # definindo variáveis temporárias:
    texto_sup = fonte.render("ui ui ui elemento químico", False, "Black" )

    # adicionando superfícies (imagens):
    screen.blit(fundo_sup, (0,0))
    screen.blit(kikinho_sup, (25,25))
    screen.blit(speechBubble_sup, (301, 25))
    screen.blit(texto_sup, (100,400))

    pygame.display.update()
    clock.tick(60) # fps total

''' ----- CHECKLIST: -----
    o | código base:
        x | criar uma janela
        x | terminar as configurações iniciais
        x | adicionar placeholders
        x | adicionar texto
        o | adicionar botões
    o | juntar com o algoritmo do kikinho:
        o | ligar os botões à variável de resposta
        o | atualizar a janela a cada pergunta
        o | mudar o texto da pergunta na janela
    o | adição de imagens:
        x | ícone
        x | kikinho
        o | botões
        x | fundo
        x | balão de texto
    o | se der tempo:
        o | expressões faciais
        o | música de fundo
        o | efeitos sonoros
        o | fontes diferentes
        o | letra a letra
'''