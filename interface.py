# --------------- CONFIGURAÇÕES INICIAIS ---------------
# importando bibliotecas:
import pygame
from sys import exit
import time
import kikinho
import random
from mendeleev import element

# definindo configurações iniciais:
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Kikinho, o gênio da tabela periódica")
icon = pygame.image.load("imagens\icon.png")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
fonte = pygame.font.Font("fontes\PixeloidSans.ttf", 26)
indexFrase = 0
perguntaAtual = "O seu elemento é um ametal?" # Define a primeira pergunta como a pergunta atual
listaExcluída = set()
answer = ""
pausado = False

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
            self.valor = "nsei"

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
        if clique[0] and self.rect.collidepoint(pos[0], pos[1]) and not self.apertando:
            time.sleep(0.1)
            self.apertando = True
            global answer
            answer = self.valor
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

ButtonGroupFinal = pygame.sprite.Group()
ButtonGroupFinal.add(Button("SIM"))
ButtonGroupFinal.add(Button("NÃO"))

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

    if answer == "vai":
        answer = ""
        indexFrase += 1

    if indexFrase >= 2:
        break

    pygame.display.update()
    clock.tick(15) # fps total

# --------------- MAIN LOOP ---------------
while kikinho.perguntasPossíveis != set(): # Enquanto ainda houver perguntas possíveis:

    # mais configurações básicas:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # checando a resposta:
    if answer == "":
        pausado = True
    if answer == "s": # Se a resposta for sim:
        for elemento in kikinho.elementosPossíveis: # Para cada elemento possível,
            if elemento not in kikinho.perguntas[perguntaAtual]: # Se este elemento não corresponde à pergunta:
                listaExcluída.add(elemento) # Adiciona o elemento à lista para exclusão
        pausado = False
    
    kikinho.elementosPossíveis = kikinho.elementosPossíveis - listaExcluída # Retira a lista de exclusão da lista de elementos possíveis

    if answer == "n": # Se a resposta for não:
        kikinho.elementosPossíveis = kikinho.elementosPossíveis - kikinho.perguntas[perguntaAtual] # Retira os elementos correspondentes à pergunta da lista de elementos possíveis
        pausado = False

    if answer == "nsei":
        pausado = False

    if not pausado:
    # partindo para a próxima pergunta:
        kikinho.perguntasPossíveis.remove(perguntaAtual) # Remove a pergunta atual da lista de perguntas possíveis, impedindo que as perguntas se repitam

        for chave in kikinho.perguntas: # Para cada pergunta no dicionário perguntas:
            if kikinho.elementosPossíveis.intersection(kikinho.perguntas[chave]) == set() and chave in kikinho.perguntasPossíveis: # Se não houver nenhuma pergunta em comum com elementos possíveis:
                kikinho.perguntasPossíveis.remove(chave) # Remove pergunta de perguntas possíveis
        
        if kikinho.perguntasPossíveis == set(): # Se não houver mais perguntas possíveis:
            for chave, valor in kikinho.perguntasEspecíficas.items(): # Para cada par chave-valor no dicionário de perguntas específicas:
                if list(valor)[0] in kikinho.elementosPossíveis: # Se o elemento correspondente (valor) estiver entre os elementos possíveis:
                    kikinho.perguntas[chave] = valor # Adiciona o par chave-valor (pergunta e elemento) ao dicionário de perguntas normais
                    kikinho.perguntasPossíveis.add(chave) # Adiciona a pergunta (chave) à lista de perguntas possíveis

        listaTemporária = list(kikinho.perguntasPossíveis) # Uma lista temporária que é uma cópia do conjunto de perguntas possíveis
        
        if listaTemporária != [] and len(kikinho.elementosPossíveis) >= 2: # Se houver alguma pergunta na lista temporária e ainda houver algum elemento possível:
            perguntaAtual = random.choice(listaTemporária) # Define uma pergunta aleatória das restantes como pergunta atual
    
        if len(kikinho.elementosPossíveis) <= 2: # Se houver apenas 2 ou menos elementos:
            break # Sai do loop while, para adivinhar seu elemento

        # resetando variáveis temporárias:
        listaExcluída = set() # Limpa a lista de elementos a serem excluídos a cada iteração (usada posteriormente)
        answer = "" # Limpa a variável que contém a resposta para a pergunta atual

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

if len(kikinho.elementosPossíveis) == 0:
    Fala = "Baixo astral, cara. Não consegui adivinhar o seu elemento. Você me venceu. :'(" # :(

resultadoTemporário = list(kikinho.elementosPossíveis) # Cria uma lista para o resultado temporário
answer = ""
elementoAdivinhado = resultadoTemporário[0] # Define o primeiro item da lista como aquele a ser adivinhado
finished = False

# --------------- LOOP FINAL ---------------
while True:
    # mais configurações básicas:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if not finished:
        if answer == "":
            Fala = "O seu elemento é o " + element(elementoAdivinhado).name + "?"
            # Note acima o uso da biblioteca mendeleev para obtenção do nome do elemento a partir de seu número atômico! :)
        if answer == "s": # Se a resposta final for sim:
            Fala = "Isso! Consegui acertar! De primeira hein? ;)" # :D
            finished = True
        if len(resultadoTemporário) == 1 and answer == 'n': # Se a lista de elementos estiver vazia e a resposta final for não:
            Fala = "Baixo astral, cara. Não consegui adivinhar o seu elemento. Você me venceu. :'(" # :(
            finished = True
        if len(resultadoTemporário) != 1 and answer == "n":
            resultadoTemporário.remove(elementoAdivinhado)
            elementoAdivinhado = resultadoTemporário[0]
            answer = ""

    screen.blit(fundo_surf, (0,0))
    screen.blit(kikinho_surf, (25,25))
    screen.blit(speechBubble_surf, (301, 25))
    screen.blit(caixa_surf, (435, 249))

    drawText(Fala)

    ButtonGroupFinal.draw(screen)
    ButtonGroupFinal.update()

    pygame.display.update()
    clock.tick(15)

''' --------------- CHECKLIST: ---------------
    x | código base:
        x | criar uma janela
        x | terminar as configurações iniciais
        x | adicionar placeholders
        x | adicionar texto
        x | adicionar botões
        x | fazer os botões funcionarem
        x | limitar eventos para botões apertarem só uma vez :,)
    x | juntar com o algoritmo do kikinho:
        x | importar as variáveis do kikinho
        x | passar o código do kikinho pra cá
        x | ligar os botões à variável de resposta
        x | atualizar a janela a cada pergunta
        x | mudar o texto da pergunta na janela
        x | testar se funciona depois de atualizar o kikinho
        x | arrumar frase final
        x | implementar botão de NÃO SEI
    x | atualizar o algoritmo do kikinho:
        x | tirar as perguntas questionáveis
        x | colocar novas perguntas gerais
        x | colocar novas perguntas específicas
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

KIKINHO OFICIALMENTE TERMINADO!!!!

'''