from tkinter import *
from tkinter.messagebox import *
from PIL import ImageTk, Image

import warnings
warnings.filterwarnings("ignore")

from AperitifPage import AperitifPage
from DessertPage import DessertPage
from EntreePage import EntreePage
from PlatPrincipalPage import PlatPrincipalPage


class MenuPage:
    """
    Classe pour la création de la fenetre de dialogue du Menu Principal et pour la géstion du choix de la catégorie de
    plat
    """
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.master.title('DYONISO')
        self.master.resizable(width="false", height="false")
        self.master.geometry("900x600+180+100")
        self.frame.pack()

        background = 'C:/Users/enricazabaino/Projet/Wine_Recommender/Prolog/vin2.png'

        photo = PhotoImage(file=background)
        self.canvas = Canvas(self.frame, width=16000, height=2000)
        self.canvas.imageList = []
        self.canvas.pack()
        self.canvas.create_image(0, 0, anchor="nw", image=photo)
        self.canvas.imageList.append(photo)
        self.canvas.create_text(339, 60, anchor=W, font=("Purisa", 16, "bold"),
                                text="BIENVENUS chez DYONISO\n")
        self.canvas.create_text(270, 80, anchor=NW, font=("Purisa", 16, "bold"),
                                text="Vous pouvez choisir les options suivants\n")

        self.menuAperitif = Button(self.frame, padx=38, bd=5, text="Apéritif",
                                   bg='white', command=self.new_windowAperitif)
        self.menuEntree = Button(self.frame, padx=40, bd=5, text="Entrée",
                                 bg='white', command=self.new_windowEntree)
        self.menuPlatPrinc = Button(self.frame, padx=22, bd=5, text="Plat Principal",
                                    bg='white', command=self.new_windowPP)
        self.menuDessert = Button(self.frame, padx=38, bd=5, text="Dessert",
                                  bg='white', command=self.new_windowDessert)
        self.closeButton = Button(self.frame, padx=40, bd=5, text="Fermer",
                                  bg='white', command=self.close_window)

        createMenuAperitif = self.canvas.create_window(270, 140, window=self.menuAperitif)
        createMenuEntree = self.canvas.create_window(270, 180, window=self.menuEntree)
        createMenuPlatPrinc = self.canvas.create_window(270, 220, window=self.menuPlatPrinc)
        createMenuDessert = self.canvas.create_window(270, 260, window=self.menuDessert)
        createCloseButton = self.canvas.create_window(270, 300, window=self.closeButton)

    def close_window(self):
        '''
        Fonction pour fermer la fenetre alors que buton 'closeButton' est pressé
        '''
        self.master.destroy()

    def new_windowAperitif(self):
        '''
        Fonction qui permet d'ouvrir une fenetre de dialogue de la classe AperitifPage
        '''
        self.newWindow = Toplevel(self.master)
        self.app = AperitifPage(self.newWindow)

    def new_windowEntree(self):
        '''
        Fonction qui permet d'ouvrir une fenetre de dialogue de la classe EntreePage
        '''
        self.newWindow = Toplevel(self.master)
        self.app = EntreePage(self.newWindow)

    def new_windowPP(self):
        '''
        Fonction qui permet d'ouvrir une fenetre de dialogue de la classe PlatPrincipalPage
        '''
        self.newWindow = Toplevel(self.master)
        self.app = PlatPrincipalPage(self.newWindow)

    def new_windowDessert(self):
        '''
        Fonction qui permet d'ouvrir une fenetre de dialogue de la classe DessertPage
        '''
        self.newWindow = Toplevel(self.master)
        self.app = DessertPage(self.newWindow)