# Projeto SteamScouter - scrapper de informações da Steam
from tkinter import *
import customtkinter
from PIL import ImageTk, Image
from playwright.sync_api import sync_playwright


def MaisPopulares():
    #faz o scraping e tira print das informações
    with sync_playwright() as p:
        #abre o navegador (de forma oculta)
        browser = p.chromium.launch()
        page = browser.new_page()
        #navegação
        page.goto("https://store.steampowered.com/?l=portuguese")
        page.click('div[id="tab_newreleases_content_trigger"]')
        page.locator('div[class="home_leftcol home_tab_col"]').screenshot(path="SScouter_archives\screenshot.png")
        #fecha o navegador
        browser.close()
    #altera o tamanho da imagem
    imagescreenshot = Image.open("SScouter_archives\screenshot.png")
    image_new = imagescreenshot.resize((423, 557))
    img2 = ImageTk.PhotoImage(image_new)
    #faz a alteração da imagem na Label
    Label_Imagem.configure(image=img2)
    Label_Imagem.image=img2
   
def MaisVendidos():
    #faz o scraping e tira print das informações
    with sync_playwright() as p:
        #abre o navegador (de forma oculta)
        browser = p.chromium.launch()
        page = browser.new_page()
        #navegação
        page.goto("https://store.steampowered.com/?l=portuguese")
        page.click('div[id="tab_topsellers_content_trigger"]')
        page.locator('div[class="home_leftcol home_tab_col"]').screenshot(path="SScouter_archives\screenshot.png")
        #fecha o navegador
        browser.close()
    #altera o tamanho da imagem
    imagescreenshot = Image.open("SScouter_archives\screenshot.png")
    image_new = imagescreenshot.resize((423, 557))
    img2 = ImageTk.PhotoImage(image_new)
    #faz a alteração da imagem na Label
    Label_Imagem.configure(image=img2)
    Label_Imagem.image=img2
 
def MaisAntecipados():
    #faz o scraping e tira print das informações
    with sync_playwright() as p:
        #abre o navegador (de forma oculta)
        browser = p.chromium.launch()
        page = browser.new_page()
        #navegação
        page.goto("https://store.steampowered.com/?l=portuguese")
        page.click('div[id="tab_upcoming_content_trigger"]')
        page.locator('div[class="home_leftcol home_tab_col"]').screenshot(path="SScouter_archives\screenshot.png")
        #fecha o navegador
        browser.close()
    #altera o tamanho da imagem
    imagescreenshot = Image.open("SScouter_archives\screenshot.png")
    image_new = imagescreenshot.resize((423, 557))
    img2 = ImageTk.PhotoImage(image_new)
    #faz a alteração da imagem na Label
    Label_Imagem.configure(image=img2)
    Label_Imagem.image=img2

def Promocoes():
    #faz o scraping e tira print das informações
    with sync_playwright() as p:
        #abre o navegador (de forma oculta)
        browser = p.chromium.launch()
        page = browser.new_page()
        #navegação
        page.goto("https://store.steampowered.com/?l=portuguese")
        page.click('div[id="tab_specials_content_trigger"]')
        page.locator('div[class="home_leftcol home_tab_col"]').screenshot(path="SScouter_archives\screenshot.png")
        #fecha o navegador
        browser.close()
    #altera o tamanho da imagem
    imagescreenshot = Image.open("SScouter_archives\screenshot.png")
    image_new = imagescreenshot.resize((423, 557))
    img2 = ImageTk.PhotoImage(image_new)
    #faz a alteração da imagem na Label
    Label_Imagem.configure(image=img2)
    Label_Imagem.image=img2


#Propriedades da Main Window
window = Tk()
window.title("SteamScouter")
window.iconbitmap(r'SScouter_archives\Icon.ico')
window.geometry("900x600+160+50")
window.resizable(width = False ,height = False)
window.configure(bg="#0b1219")


#Atribuição do Icon e do PlaceHolder
imgLogo = PhotoImage(file="SScouter_archives\SteamScouter_Logo.png")
PlaceHolder = PhotoImage(file="SScouter_archives\placeholder.png")


#criação dos elementos da GUI
Label_Imagem = Label(window, image=PlaceHolder, background="#314e6d")
Label_Logo = Label(window, image=imgLogo, background="#0b1219")
Button_Populares = customtkinter.CTkButton(master= window,
                                           command= MaisPopulares,
                                            text= "Ver as \n Novidades Populares",
                                            text_font="none 15 bold",
                                            hover= True,
                                            hover_color= "#434343",
                                            width= 270,
                                            height=56,
                                            border_width=2,
                                            corner_radius=8,
                                            border_color= "black", 
                                            bg_color="#0b1219",
                                            fg_color= "#82a90f")
Button_MaisVendidos = customtkinter.CTkButton(master= window,
                                            command= MaisVendidos,
                                            text= "Ver os \n Mais Vendidos",
                                            text_font="none 15 bold",
                                            hover= True,
                                            hover_color= "#434343",
                                            width= 270,
                                            height=56,
                                            border_width=2,
                                            corner_radius=8,
                                            border_color= "black", 
                                            bg_color="#0b1219",
                                            fg_color= "#82a90f")
Button_MaisAntecipados = customtkinter.CTkButton(master= window,
                                            command= MaisAntecipados,
                                            text= "Ver os \n Mais Antecipados",
                                            text_font="none 15 bold",
                                            hover= True,
                                            hover_color= "#434343",
                                            width= 270,
                                            height=56,
                                            border_width=2,
                                            corner_radius=8,
                                            border_color= "black", 
                                            bg_color="#0b1219",
                                            fg_color= "#82a90f")
Button_Promocoes = customtkinter.CTkButton(master= window,
                                            command= Promocoes,
                                            text= "Ver as \n Promoções",
                                            text_font="none 15 bold",
                                            hover= True,
                                            hover_color= "#434343",
                                            width= 270,
                                            height=56,
                                            border_width=2,
                                            corner_radius=8,
                                            border_color= "black", 
                                            bg_color="#0b1219",
                                            fg_color= "#82a90f")


#Organização dos elementos da GUI
Label_Logo.place(x= 45, y= 20)
Label_Imagem.place(x= 457, y= 20)
Button_Populares.place(x= 93, y= 200)
Button_MaisVendidos.place(x= 93, y= 280)
Button_MaisAntecipados.place(x= 93, y= 360)
Button_Promocoes.place(x= 93, y= 440)


#roda o loop principal
window.mainloop()