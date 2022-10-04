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
indexFrase = 0

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
            SIM1 = pygame.image.load("imagens\SIM.png")
            SIM2 = pygame.image.load("imagens\SIM2.png")
            self.frames = [SIM1, SIM2]
            self.ponto = (455,269)
            self.valor = "s"

        elif resposta == "NÃO_SEI":
            NÃO_SEI1 = pygame.image.load(r"imagens\NÃO_SEI.png")
            NÃO_SEI2 = pygame.image.load(r"imagens\NÃO_SEI2.png")
            self.frames = [NÃO_SEI1, NÃO_SEI2]
            self.ponto = (455,371)
            self.valor = ""

        elif resposta == "NÃO":
            NÃO1 = pygame.image.load(r"imagens\NÃO.png")
            NÃO2 = pygame.image.load(r"imagens\NÃO2.png")
            self.frames = [NÃO1,NÃO2]
            self.ponto = (455,473)
            self.valor = "n"

        elif resposta == "CONTINUAR":
            CONTINUAR1 = pygame.image.load("imagens\CONTINUAR.png")
            CONTINUAR2 = pygame.image.load("imagens\CONTINUAR2.png")
            self.frames = [CONTINUAR1, CONTINUAR2]
            self.ponto = (455,371)
            self.valor = "vai"

        self.animation_index = 0
        self.apertando = False
        self.image = self.frames[int(self.animation_index)]
        self.rect = self.image.get_rect(topleft = self.ponto)

    def button_input(self):
        clique = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()
        if clique[0] and self.rect.collidepoint(pos[0], pos[1]):
            self.apertando = True
            return self.valor
        else:
            self.apertando = False

    def animation(self):
        if self.apertando == True:
            self.animation_index = 1
        else:
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.button_input()
        self.animation()
            
ButtonGroup = pygame.sprite.Group()
ButtonGroup.add(Button("SIM"))
ButtonGroup.add(Button("NÃO_SEI"))
ButtonGroup.add(Button("NÃO"))

CONTINUAR = pygame.sprite.GroupSingle()
CONTINUAR.add(Button("CONTINUAR"))

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

# --------------- LOOP INICIAL ---------------
while True:
    # mais configurações básicas:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit
    
    # definindo as frases de apresentação:
    fraseInicial = ["Olá, sou o Kikinho, gênio da tabela periódica da Ilum Escola de Ciência.", "Pense em um elemento da tabela periódica, e eu vou tentar adivinhá-lo através de perguntas de SIM ou NÃO!"]

    # exibindo superfícies (imagens) e sprites:
    screen.blit(fundo_surf, (0,0))
    screen.blit(kikinho_surf, (25,25))
    screen.blit(speechBubble_surf, (301, 25))

    drawText(fraseInicial[indexFrase])

    CONTINUAR.draw(screen)
    CONTINUAR.update()

    if Button("CONTINUAR").button_input() == "vai":
        indexFrase += 1

    if indexFrase >= 2:
        break

    pygame.display.update()
    clock.tick(15) # fps total

# --------------- MAIN LOOP ---------------
while True:
    # mais configurações básicas:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # definindo variáveis temporárias:
    perguntaAtual = "O seu elemento faz ligação covalente?"
   
    # exibindo superfícies (imagens) e sprites:
    screen.blit(fundo_surf, (0,0))
    screen.blit(kikinho_surf, (25,25))
    screen.blit(speechBubble_surf, (301, 25))
    screen.blit(caixa_surf, (435, 249))
    
    drawText(perguntaAtual)

    ButtonGroup.draw(screen)
    ButtonGroup.update()

    pygame.display.update()
    clock.tick(15) # fps total

''' --------------- CHECKLIST: ---------------
    o | código base:
        x | criar uma janela
        x | terminar as configurações iniciais
        x | adicionar placeholders
        x | adicionar texto
        x | adicionar botões
        x | fazer os botões funcionarem
        o | limitar eventos para botões apertarem só uma vez :,)
    o | juntar com o algoritmo do kikinho:
        o | ligar os botões à variável de resposta
        o | atualizar a janela a cada pergunta
        o | mudar o texto da pergunta na janela
    x | adição de imagens:
        x | ícone
        x | kikinho
        x | botões
        x | fundo
        x | balão de texto
    o | se der tempo:
        o | expressões faciais
        o | música de fundo
        o | efeitos sonoros
        o | fontes/cores diferentes
        o | texto que aparece letra a letra
        x | botão que muda de cor enquanto pressionado
        x | loop inicial de apresentação :)

'''