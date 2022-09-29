# importando bibliotecas:
import pygame
from sys import exit

# definindo configurações iniciais:
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Kikinho, o gênio da tabela periódica")
icon = pygame.image.load("imagens\placeholder.bmp")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
fonte = pygame.font.Font("fontes\PixeloidSans.ttf", 30)

# definindo variáveis e importando superfícies (imagens):
fundo_sup = pygame.image.load(r"imagens\bg_placeholder.png")
kikinho_sup = pygame.image.load("imagens\placeholder.png")


# main loop:
while True:
    # mais configurações básicas:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # adicionando superfícies (imagens):
    screen.blit(fundo_sup, (0,0))
    screen.blit(kikinho_sup, (300,75))
    texto_sup = fonte.render("ui ui ui elemento químico", False, "Black" )
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
        o | ícone
        o | kikinho
        o | botões
        o | fundo
        o | balão de texto
    o | se der tempo:
        o | expressões faciais
        o | música de fundo
        o | efeitos sonoros
        o | fontes diferentes
'''