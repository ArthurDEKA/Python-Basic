# Projeto SinôniMEU - Buscador de sinônimos com a biblioteca Pysinonimos
import tkinter
from pysinonimos.sinonimos import Search, historic
from tkinter import *
import customtkinter

def PesquisaSinonimos():
    #faz a pesquisa dos sinônimos
    pesquisa = customtkinter.CTkEntry.get(Entry_Pesquisa)
    palavra = Search(str(pesquisa))
    sinonimos_palavra = palavra.synonyms()
    #insere os sinônimos na listbox
    for item in sinonimos_palavra:
        Listbox_Lista.insert(0, item)

#Propriedades da Main Window
window = Tk()
window.title("SinôniMEU")
window.geometry("340x544+160+50")
window.resizable(width = False ,height = False)
window.configure(bg="#b18f5e")

#atribuição da Logo
logo = PhotoImage(file="SinoniMEU_archives\Logo_SinoniMEU.png")

#criação dos elementos da GUI
Label_Logo = Label(window, image = logo, background="#b18f5e")
Entry_Pesquisa = customtkinter.CTkEntry(master=window, placeholder_text="Descubra um sinônimo!", width= 275, height= 35, justify='center')
Button_Pesquisar = customtkinter.CTkButton(master= window,
                                            command= PesquisaSinonimos,
                                            text= "Pesquisar",
                                            text_font="none 10 bold",
                                            hover= True,
                                            hover_color= "#434343",
                                            width= 133,
                                            height=20,
                                            border_width=2,
                                            corner_radius=8,
                                            border_color= "black", 
                                            bg_color="#b18f5e",
                                            fg_color= "#202020")
Listbox_Lista = tkinter.Listbox(master=window,
                                width= 25,
                                height=12,
                                background="#6a573b",
                                foreground="white",
                                font=('none 15 bold'),
                                selectbackground="#343434",
                                justify='center')

#Organização dos elementos da GUI
Label_Logo.place(x= -2, y = 0)
Entry_Pesquisa.place(x = 33, y = 115)
Button_Pesquisar.place(x = 104, y = 155)
Listbox_Lista.place(x= 30, y= 210)

#roda o loop principal
window.mainloop()