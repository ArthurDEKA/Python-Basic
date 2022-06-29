# Projeto CountryGuess
from tkinter import *
import customtkinter
import random

#Listas que armazenam as perguntas, respostas e verificação
BancoPerguntas = [
    'O Japão é considerado o\nprincipal rival da Coreia do Sul',
    'O Brasil é considerado o\nprincipal rival da Argentina',
    'A Turquia é considerada a\nprincipal rival da Grécia',
    'O Brasil faz fronteira com\num membro da União Europeia',
    'Porto Rico é um país',
    'República da China é o\nnome oficial de Taiwan',
    'A Índia tem uma população\nmaior que a da Europa',
    'Sidney é a capital\nda Australia',
    'Toronto é a capital\ndo Canadá',
    'Ottawa é a capital\ndo Canadá',
    'Barbados é o nome\nde um país',
    'A Guiné Equatorial é o único país\nafricano que tem como seu\nidioma oficial o espanhol',
    'El Salvador é o único país\nlatino americano que\nfala holandês',
    'O Brasil é o único país\nque nunca deixou de participar\nde uma Copa do Mundo',
    'O México é a maior economia\nda América Latina',
    'O País com a maior população\ndo mundo é Taiwan',
    'A décima maior economia\ndo mundo é a do Qatar',
    'A Rússia é um país com\nterritório na Ásia e na Europa',
    'Ilhas Marshall não é o\nnome de um país independente',
    'A Bolívia é o país\nmais plano do mundo',
    'San Marino é o Estado/País\nmais antigo do mundo',
    'O menor país do mundo\né o Vaticano, que possui\napenas 800 habitantes oficiais',
    'A cidade de Tóquio,\nno Japão, é a mais\npopulosa do mundo',
    'A China é a única economia\nno rank das 10 maiores\nque não foi pro espaço',
    'Timor-Leste é um país\nafricano que fala português',
    'A China não permite\nque grande empresas estrangeiras\natuem em seu território',
    'O país com o maior\nnúmero de startups\nno mundo é a India',
    'Oymyakon, na Rússia,\né o local habitado mais frio do mundo',
    'É possível cruzar Liechtenstein\nem menos de um dia',
    'A Mongólia é o país\nmenos povoado do mundo',
    ]
BancoRespostas = [
    False,
    True,
    True,
    True,
    False,
    True,
    True,
    False,
    False,
    True,
    True,
    False,
    True,
    True,
    False,
    False,
    False,
    True,
    False,
    True,
    True,
    True,
    True,
    False,
    False,
    True,
    False,
    True,
    True,
    True,
    ]
BancoVerificacao = [
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    ]

#classe dos dados
class Dados:
    def __init__(self, ListaPerguntas, ListaRespostas, ListaVerificacao):
        self.ListaPerguntas = ListaPerguntas
        self.ListaRespostas = ListaRespostas
        self.ListaVerificacao = ListaVerificacao

PacoteDados = Dados(ListaPerguntas= BancoPerguntas, ListaRespostas= BancoRespostas, ListaVerificacao= BancoVerificacao)

#Variáveis do projeto
i = 0
Acertos = 0
Erros = 0

#Funções do programa
#Função para definir a frase inicial do programa
def FraseInicial():
    #é sorteada uma pergunta com um range do mesmo tamanho da lista de perguntas
    global i
    global PacoteDados
    TamanhoLista = (len(PacoteDados.ListaPerguntas))
    i = random.randint(0,TamanhoLista-1)  
    TextoInicial = PacoteDados.ListaPerguntas[i]
    #a frase sorteada é marcada como já usada
    PacoteDados.ListaVerificacao[i] = 0
    return TextoInicial
    
#Função para dar o raise no frame
def FrameRaise(frame):
    frame.tkraise()

#Função para quando o botão VERDADEIRO for clicado
def clickVerdadeiro():
    global i
    global PacoteDados
    global Acertos
    global Erros
    #faz a verificação se o usuário acertou ou não e faz a contagem
    if PacoteDados.ListaRespostas[i] == True:
        Acertos = Acertos + 1
        label_Acertos.configure(text= ("Acertos: " + str(Acertos)))
    else:
        Erros = Erros + 1
        label_Erros.configure(text= ("Erros: " + str(Erros)))
    #checagem se ainda existem frases disponíveis
    ListaAcabou = True
    for verificacao in PacoteDados.ListaVerificacao:
        if verificacao == 1:
            ListaAcabou = False
            break
    if ListaAcabou == True:
        Label_TextoPergunta.configure(text= "Acabaram as perguntas!\nObrigado por jogar!")
        Button_Falso.configure(state="disabled")
        Button_Verdadeiro.configure(state="disabled")
    #caso ainda existam, é sorteada uma nova frase
    else:
        TamanhoLista = (len(PacoteDados.ListaPerguntas))
        #o loop while serve para a nova frase sorteada serem apenas as que ainda não foram usadas
        while PacoteDados.ListaVerificacao[i] != 1:
            i = random.randint(0,TamanhoLista-1)
        #após a nova frase ser sorteada, ela é marcada como já utilizada
        PacoteDados.ListaVerificacao[i] = 0
        Label_TextoPergunta.configure(text= (PacoteDados.ListaPerguntas[i]))
 
#Função para quando o botão FALSO for clicado
def clickFalso():
    global i
    global PacoteDados
    global Acertos
    global Erros
    #faz a verificação se o usuário acertou ou não e faz a contagem
    if PacoteDados.ListaRespostas[i] == False:
        Acertos = Acertos + 1
        label_Acertos.configure(text= ("Acertos: " + str(Acertos)))
    else:
        Erros = Erros + 1
        label_Erros.configure(text= ("Erros: " + str(Erros)))
    #checagem se ainda existem frases disponíveis
    ListaAcabou = True
    for verificacao in PacoteDados.ListaVerificacao:
        if verificacao == 1:
            ListaAcabou = False
            break
    if ListaAcabou == True:
        Label_TextoPergunta.configure(text= "Acabaram as perguntas!\nObrigado por jogar :)")
        Button_Falso.configure(state="disabled")
        Button_Verdadeiro.configure(state="disabled")
    #caso ainda existam, é sorteada uma nova frase
    else:
        TamanhoLista = (len(PacoteDados.ListaPerguntas))
        #o loop while serve para a nova frase sorteada serem apenas as que ainda não foram usadas
        while PacoteDados.ListaVerificacao[i] != 1:
            i = random.randint(0,TamanhoLista-1)
        #após a nova frase ser sorteada, ela é marcada como já utilizada
        PacoteDados.ListaVerificacao[i] = 0
        Label_TextoPergunta.configure(text= (PacoteDados.ListaPerguntas[i]))


#Propriedades da Main Window
window = Tk()
window.title("CountryGuess")
window.geometry("700x400")
window.resizable(width = False ,height = False)
window.configure(bg="#2F0061")


#definição das imagens usadas
#definição da tela de menu usada no Frame_Menu
ImgMenu = PhotoImage(file= "archives/TelaMenu.png")
#definição do background usado no frame_quiz
background = PhotoImage(file="archives/background.png")


#criação dos elementos da GUI
#FRAME MENU
Frame_Menu = Frame(window, width= 702, height= 400)
Label_ImgMenu = Label(Frame_Menu, image= ImgMenu)
Button_Jogar = customtkinter.CTkButton(
    master= Frame_Menu,
    command= lambda:FrameRaise(Frame_Quiz),
    text= "JOGAR",
    text_font="none 17 bold",
    text_color= "black",
    hover= True,
    hover_color= "#ff6123",
    height=50,
    width= 200,
    border_width=2,
    corner_radius=8,
    border_color= "black", 
    bg_color="#994900",
    fg_color= "#ff4800")
#FRAME QUIZ
Frame_Quiz = Frame(window, width= 702, height= 400)
Label_background = Label(Frame_Quiz, image= background)
Label_TextoPergunta = Label(Frame_Quiz, text=FraseInicial(), bg="#f68500", fg="black", font="none 25 bold")
label_Acertos = customtkinter.CTkLabel(Frame_Quiz, text="Acertos: 0", text_font="none 20 bold", text_color="#78ff00", bg_color="black")
label_Erros = customtkinter.CTkLabel(Frame_Quiz, text="Erros: 0", text_font="none 15 bold", text_color="#ff0000", bg_color="black")
Button_Verdadeiro = customtkinter.CTkButton(
    master= Frame_Quiz,
    command= clickVerdadeiro,
    text= "VERDADEIRO",
    text_font="none 17 bold",
    text_color= "black",
    hover= True,
    hover_color= "#ff6123",
    height=50,
    width= 250,
    border_width=2,
    corner_radius=8,
    border_color= "black", 
    bg_color="#da7700",
    fg_color= "#ff4800",)
Button_Falso = customtkinter.CTkButton(
    master= Frame_Quiz,
    command=clickFalso, 
    text= "FALSO",
    text_font="none 17 bold",
    text_color= "black",
    hover= True,
    hover_color= "#ff6123",
    height=50,
    width= 250,
    border_width=2,
    corner_radius=8,
    border_color= "black", 
    bg_color="#da7700",
    fg_color= "#ff4800")


#Organização do programa (uso do .place)
#organização no Frame_Menu
Frame_Menu.place(x= -2, y= 0)
Label_ImgMenu.place(x= 0, y= 0)
Button_Jogar.place(x= 350, y= 340, anchor=CENTER)
#organização no Frame_Quiz
Frame_Quiz.place(x= -2, y= 0)
Label_background.place(x= 0, y= 0)
Label_TextoPergunta.place(x= 350, y= 100, anchor=CENTER)
Button_Verdadeiro.place(x= 78,y= 254)
Button_Falso.place(x= 370,y= 254)
label_Acertos.place(x= 350,y= 348, anchor=CENTER)
label_Erros.place(x= 350,y= 375, anchor=CENTER)


#execução do programa
#definindo que o Frame_Menu será o que aparecerá primeiro
FrameRaise(Frame_Menu)
#definindo a frase inicial


#roda o loop principal
window.mainloop()