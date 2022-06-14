# Projeto GotchaTube - downloader de video do youtube
from pytube import YouTube
from tkinter import *
import customtkinter

#função de baixar o vídeo
def clickBaixar():
    url = customtkinter.CTkEntry.get(EntradaURL)
    dir_saida = customtkinter.CTkEntry.get(EntradaDiretorio)
    video = YouTube(url)
    stream = video.streams.get_highest_resolution()
    stream.download(output_path = dir_saida)

#Propriedades da Main Window
window = Tk()
window.title("GotchaTube!")
window.geometry("600x200")
window.resizable(width = False ,height = False)
window.configure(bg="#ededed")

#atribuição da logo do GotchaTube
img = PhotoImage(file="GotchaTube_logo.png")

#criação dos elementos da GUI
Label_Logo = Label(window, image=img)
EntradaURL = customtkinter.CTkEntry(master=window, placeholder_text="Coloque aqui a URL do vídeo", width= 345, height= 35, )
EntradaDiretorio = customtkinter.CTkEntry(master=window, placeholder_text="Coloque aqui o diretório de destino do vídeo", width= 345, height= 35, )
Button_Baixar = customtkinter.CTkButton(master= window,
                                            command= clickBaixar,
                                            text= "Baixar Vídeo",
                                            text_font="none 15 bold",
                                            hover= True,
                                            hover_color= "#434343",
                                            width= 133,
                                            height=30,
                                            border_width=2,
                                            corner_radius=8,
                                            border_color= "black", 
                                            bg_color="#ededed",
                                            fg_color= "#202020")

#Organização dos elementos da GUI
EntradaURL.place(x= 235, y= 35)
EntradaDiretorio.place(x=235, y= 80)
Button_Baixar.place(x=235, y=136)
Label_Logo.place(x= 15, y= 30)

#roda o loop principal
window.mainloop()