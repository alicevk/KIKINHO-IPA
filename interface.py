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
fonte = pygame.font.Font("fontes\PixeloidSans.ttf", 26)

# definindo variáveis e importando superfícies, retângulos e classes de sprites:
fundo_surf = pygame.image.load(r"imagens\background.png")
kikinho_surf = pygame.image.load("imagens\kikinho.png")
speechBubble_surf = pygame.image.load("imagens\speechBubble.png")
caixa_surf = pygame.image.load("imagens\caixa.png")

text_rect = pygame.Rect(355,45,400,159)

class Button(pygame.sprite.Sprite): 
    def __init__(self, resposta):
        super().__init__()
        
        if resposta == "SIM":
            self.fotinha = "imagens\SIM.png"
            self.ponto = (455,269)

        elif resposta == "NÃO_SEI":
            self.fotinha = r"imagens\NÃO_SEI.png"
            self.ponto = (455,371)

        elif resposta == "NÃO":
            self.fotinha = r"imagens\NÃO.png"
            self.ponto = (455,473)

        self.image = pygame.image.load(self.fotinha)
        self.rect = self.image.get_rect(topleft = self.ponto)

ButtonGroup = pygame.sprite.Group()
ButtonGroup.add(Button("SIM"))
ButtonGroup.add(Button("NÃO_SEI"))
ButtonGroup.add(Button("NÃO"))

# --------------- DEFININDO FUNÇÕES ---------------
# função para o texto: (https://www.pygame.org/wiki/TextWrap)
def drawText(text, color="Black", surface=screen, rect=text_rect, font=fonte, aa=False, bkg=None):
    rect = pygame.Rect(rect)
    y = rect.top
    lineSpacing = -1

    # get the height of the font
    fontHeight = font.size("Tg")[1]

    while text:
        i = 1

        # determine if the row of text will be outside our area
        if y + fontHeight > rect.bottom:
            break

        # determine maximum width of line
        while font.size(text[:i])[0] < rect.width and i < len(text):
            i += 1

        # if we've wrapped the text, then adjust the wrap to the last word      
        if i < len(text): 
            i = text.rfind(" ", 0, i) + 1

        # render the line and blit it to the surface
        if bkg:
            image = font.render(text[:i], 1, color, bkg)
            image.set_colorkey(bkg)
        else:
            image = font.render(text[:i], aa, color)

        surface.blit(image, (rect.left, y))
        y += fontHeight + lineSpacing

        # remove the text we just blitted
        text = text[i:]

    return text

# --------------- MAIN LOOP ---------------
while True:
    # mais configurações básicas:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # definindo variáveis temporárias:
    perguntaAtual = "O seu elemento faz ligação covalente?"
   
    # exibindo superfícies (imagens):
    screen.blit(fundo_surf, (0,0))
    screen.blit(kikinho_surf, (25,25))
    screen.blit(speechBubble_surf, (301, 25))
    screen.blit(caixa_surf, (435, 249))

    ButtonGroup.draw(screen)

    drawText(perguntaAtual)

    # exibindo sprites:


    pygame.display.update()
    clock.tick(60) # fps total

''' --------------- CHECKLIST: ---------------
    o | código base:
        x | criar uma janela
        x | terminar as configurações iniciais
        x | adicionar placeholders
        x | adicionar texto
        x | adicionar botões
        o | fazer os botões funcionarem ;-;
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
        o | fontes/cores diferentes
        o | texto que aparece letra a letra
        o | botão que muda de cor enquanto pressionado
        o | loop inicial de apresentação :)
             fraseInicial = "Olá, sou o Kikinho, gênio da tabela periódica da Ilum Escola de Ciência." 
             fraseInicial = "Pense em um elemento da tabela periódica, e eu vou tentar adivinhá-lo através de perguntas de SIM ou NÃO!"

'''