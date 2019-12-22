from tkinter import *
from tkinter.messagebox import *
from PIL import ImageTk, Image
from pyswip import *
import re
import unicodedata
import random

import warnings
warnings.filterwarnings("ignore")

prolog = Prolog()
prolog.consult("base_de_connaisances.pl")


class DessertPage:
    """
    Classe pour la création de la fenetre de dialogue de la catégorie Dessert et pour la géstion du choix
    du type de dessert
    """
    def __init__(self, master):
        '''
        Définition de la structure de la fenetre de dialogue: frame, image, butons et texte
        '''
        self.master = master
        self.frame = Frame(self.master)
        self.master.title('OINOS - Dessert')
        self.master.resizable(width="false", height="false")
        self.master.geometry("900x600+180+100")
        self.frame.pack()

        backgroundDessert = 'C:/Users/enricazabaino/Projet/Wine_Recommender/Prolog/dessert2.png'

        photoDessert = PhotoImage(file=backgroundDessert)
        self.canvasDessert = Canvas(self.frame, width=16000, height=2000)
        self.canvasDessert.imageList = []
        self.canvasDessert.pack()
        self.canvasDessert.create_image(0, 0, anchor="nw", image=photoDessert)
        self.canvasDessert.imageList.append(photoDessert)

        self.closeButton = Button(self.frame, padx=38, bd=5, text="Revenir au menu principal", bg='white',
                                  command=self.close_window)
        createCloseButton = self.canvasDessert.create_window(750, 500, window=self.closeButton)

        info = StringVar()
        self.label1 = Label(self.frame, textvariable=info, fg="red", font=("Helvetica", 10, "bold"),
                            height=2, width=35, relief=RAISED).place(x=610, y=55)
        info.set("Vous avez choisi la catégorie Dessert")

        question1 = StringVar()
        self.question1Display = Label(self.frame, textvariable=question1, font=("Purisa", 10, "bold"),
                                      height=2, width=35, relief=FLAT).place(x=610, y=135)

        '''
        Présentation de la 1ère question et des options de choix
        '''
        question1.set("Indiquer le type de dessert que\n vous allez servir")

        DessertPage.typeDessert = IntVar()
        DessertPage.typeDessert.set(-1)
        self.optionChoc = Radiobutton(self.frame, text="Dessert au Chocolat", variable=DessertPage.typeDessert, value=0,
                                      indicatoron=0, command=self.new_window, width=16)
        self.optionChoc.place(relx=0.77, rely=0.35)
        self.optionFruits = Radiobutton(self.frame, text="Dessert aux Fruits", variable=DessertPage.typeDessert,
                                        value=1, indicatoron=0, command=self.new_window, width=16)
        self.optionFruits.place(relx=0.77, rely=0.42)

        '''
        Intérrogation de la base de connaissance pour récupérer la liste de tous les vins (aisi que leurs prix)
        conseillés pour chaque type de dessert et mise en forme du texte
        '''
        DessertPage.prix_dessert_choc = list(prolog.query("prix_dessert_chocolat(Vin, Prix)"))
        DessertPage.prix_dessert_fruit = list(prolog.query("prix_dessert_fruits(Vin, Prix)"))

        for i in range(len(DessertPage.prix_dessert_choc)):
            DessertPage.prix_dessert_choc[i]['Vin'] = DessertPage.prix_dessert_choc[i]['Vin'].replace("_", " ").capitalize()
        for i in range(len(DessertPage.prix_dessert_fruit)):
            DessertPage.prix_dessert_fruit[i]['Vin'] = DessertPage.prix_dessert_fruit[i]['Vin'].replace("_", " ").capitalize()

        '''
        Intérrogation de la base de connaissance pour récupérer la liste de tous les vins 
        conseillés pour chaque type de dessert et mise en forme du texte
        '''
        DessertPage.dessertChocVin = list(prolog.query("dessert_chocolat(Vin)"))
        DessertPage.dessertFruitVin = list(prolog.query("dessert_fruits(Vin)"))

        for i in range(len(DessertPage.dessertChocVin)):
            DessertPage.dessertChocVin[i]['Vin'] = DessertPage.dessertChocVin[i]['Vin'].replace("_", " ").capitalize()
        for i in range(len(DessertPage.dessertFruitVin)):
            DessertPage.dessertFruitVin[i]['Vin'] = DessertPage.dessertFruitVin[i]['Vin'].replace("_", " ").capitalize()

    def close_window(self):
        '''
        Fonction pour fermer la fenetre alors que buton 'closeButton' est pressé
        '''
        self.master.destroy()

    def new_window(self):
        '''
        Fonction qui permet de créer une nouvelle fenetre de dialogue ayant la meme structure de la précédente
        '''
        self.newWindow = Toplevel(self.master)
        self.app = PrixPage(self.newWindow)

class PrixPage:
    """
    Classe qui permet de gérérer le choix du prix
    """
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.master.title('OINOS - Dessert')
        self.master.resizable(width="false", height="false")
        self.master.geometry("900x600+180+100")
        self.frame.pack()

        backgroundDessert = 'C:/Users/enricazabaino/Projet/Wine_Recommender/Prolog/dessert2.png'

        photoDessert = PhotoImage(file=backgroundDessert)
        self.canvasDessert = Canvas(self.frame, width=16000, height=2000)
        self.canvasDessert.imageList = []
        self.canvasDessert.pack()
        self.canvasDessert.create_image(0, 0, anchor="nw", image=photoDessert)
        self.canvasDessert.imageList.append(photoDessert)

        self.closeButton = Button(self.frame, padx=38, bd=5, text="Revenir à la page précédente", bg='white',
                                  command=self.close_window)
        createCloseButton = self.canvasDessert.create_window(750, 500, window=self.closeButton)

        '''
        Affichage d'une récapitulation du choix efféctué par l'utilisateur
        '''
        infoType = StringVar()
        if DessertPage.typeDessert.get() == 0:
            self.label = Label(self.frame, textvariable=infoType, fg="red", font=("Helvetica", 10, "bold"),
                               height=5, width=35, relief=RAISED, borderwidth=5, highlightcolor="white").place(x=605,
                                                                                                               y=46)
            infoType.set(
                "\nVous avez choisi la catégorie Dessert\n\n Vous avez choisi l'option\n 'Dessert au Chocolat'\n")

        elif DessertPage.typeDessert.get() == 1:
            self.label = Label(self.frame, textvariable=infoType, fg="red", font=("Helvetica", 10, "bold"),
                               height=5, width=35, relief=RAISED, borderwidth=5, highlightcolor="green").place(x=605,
                                                                                                               y=46)
            infoType.set(
                "\nVous avez choisi la catégorie Dessert\n\n Vous avez choisi l'option\n 'Dessert aux Fruits'\n")

        '''
        Présentation de la question sur le prix et des options de choix
        '''
        question2 = StringVar()
        self.question2Display = Label(self.frame, textvariable=question2, font=("Helvetica", 10, "bold"),
                                      height=4, width=37, relief=FLAT, anchor="e").place(x=597, y=141)
        question2.set("Est-ce que vous souhaitez indiquer\n combien vous voulez dépénser au maximum?")

        DessertPage.choixDuPrix = IntVar()
        DessertPage.choixDuPrix.set(-1)
        self.oui = Radiobutton(self.frame, text="Oui", variable=DessertPage.choixDuPrix, value=0,
                               command=self.choix_prixDessert)
        self.oui.place(relx=0.75, rely=0.37)
        self.non = Radiobutton(self.frame, text="Non", variable=DessertPage.choixDuPrix, value=1,
                               command=self.choix_prixDessert)
        self.non.place(relx=0.75, rely=0.43)

    def choix_prixDessert(self):
        '''
        Fonction qui gère les cas où l'utilisateur choisisse d'indiquer ou de ne pas indiquer un prix maximum
        '''
        self.e = StringVar()
        if DessertPage.choixDuPrix.get() == 0:
            entreePrix = Entry(self.frame, textvariable=self.e, bg='bisque', fg='maroon').place(relx=0.82, rely=0.37)
            self.validerButton = Button(self.frame, text="Valider",
                                        command=self.validerDessert).place(x=708, y=300)

        elif DessertPage.choixDuPrix.get() == 1:
            self.newWindow = Toplevel(self.master)
            self.app = PageRecommandation(self.newWindow)

    def validerDessert(self):
        '''
        Fonction qui récupère les vins contenus dans la base de connaissance dont le type de dessert
        et le prix corrésponent aux choix de l'utilisateur
        return:
            un set de vins
        '''
        PrixPage.prix = int(self.e.get())

        DessertPage.vin_choc_list = []
        DessertPage.vin_fruits_list = []

        if DessertPage.typeDessert.get() == 0:
            for i in range(len(DessertPage.prix_dessert_choc)):
                if DessertPage.prix_dessert_choc[i]['Prix'] == self.prix:
                    DessertPage.vin_choc_list.append(DessertPage.prix_dessert_choc[i]['Vin'])

        elif DessertPage.typeDessert.get() == 1:
            for i in range(len(DessertPage.prix_dessert_fruit)):
                if DessertPage.prix_dessert_fruit[i]['Prix'] == self.prix:
                    DessertPage.vin_fruits_list.append(DessertPage.prix_dessert_fruit[i]['Vin'])

        DessertPage.vin_choc_set = set(DessertPage.vin_choc_list)
        DessertPage.vin_fruits_set = set(DessertPage.vin_fruits_list)

        self.newWindow = Toplevel(self.master)
        self.app = PageRecommandation(self.newWindow)

    def close_window(self):
        self.master.destroy()

class PageRecommandation:
    """
    Classe qui gère l'affichage de la variété de vin recommandée en fonction des choix effectués dans les étapes
    précédentes
    """
    def __init__(self, DessertPage):
        self.master = DessertPage
        self.frame = Frame(self.master)
        self.master.title('DYONISO - Recommandation')
        self.master.resizable(width="false", height="false")
        self.master.geometry("900x600+180+100")
        self.frame.pack()

        backgroundRecom = 'C:/Users/enricazabaino/Projet/Wine_Recommender/Prolog/boteille.png'

        photoRecom = PhotoImage(file=backgroundRecom)
        self.canvasRecom = Canvas(self.frame, width=16000, height=2000)
        self.canvasRecom.imageList = []
        self.canvasRecom.pack()
        self.canvasRecom.create_image(0, 0, anchor="nw", image=photoRecom)
        self.canvasRecom.imageList.append(photoRecom)

        self.RecomButton = Button(self.frame, padx=38, bd=5, text="Cliquer pour découvrir nos conseils", bg='white',
                                  command=self.conseilDessert)
        createRecomeButton = self.canvasRecom.create_window(750, 200, window=self.RecomButton)

        self.CaveButton = Button(self.frame, padx=38, bd=5, text="Notre cave à vin", bg='white',
                                 command=self.new_window)
        createCaveButton = self.canvasRecom.create_window(750, 500, window=self.CaveButton)

        self.closeButton = Button(self.frame, padx=38, bd=5, text="Revenir à la page précédente", bg='white',
                                  command=self.close_window)
        createCloseButton = self.canvasRecom.create_window(750, 550, window=self.closeButton)

    def conseilDessert(self):
        self.RecomButton.destroy()

        var = StringVar()
        var.set("On vous conseille le cépage")
        self.label1 = Label(self.frame, textvariable=var, font=("Helvetica", 10, "bold"),
                            height=2, width=35, relief=FLAT).place(x=605, y=180)  # 180

        var2 = StringVar()

        PageRecommandation.vin = StringVar()
        self.label3 = Label(self.frame, textvariable=PageRecommandation.vin, fg="red", font=("Helvetica", 10, "bold"),
                            height=2, width=35, relief=FLAT).place(x=605, y=210)

        if DessertPage.typeDessert.get() == 0 and DessertPage.choixDuPrix.get() == 0:
            if len(DessertPage.vin_choc_set) != 0:
                PageRecommandation.vin.set(random.choice(tuple(DessertPage.vin_choc_set)))


        elif DessertPage.typeDessert.get() == 1 and DessertPage.choixDuPrix.get() == 0:
            if len(DessertPage.vin_fruits_set) != 0:
                PageRecommandation.vin.set(random.choice(tuple(DessertPage.vin_fruits_set)))

        elif DessertPage.typeDessert.get() == 0 and DessertPage.choixDuPrix.get() == 1:
            PageRecommandation.vin.set(random.choice(DessertPage.dessertChocVin)['Vin'])

        elif DessertPage.typeDessert.get() == 1 and DessertPage.choixDuPrix.get() == 1:
            PageRecommandation.vin.set(random.choice(DessertPage.dessertFruitVin)['Vin'])

        descr = list(prolog.query("description(Vin, Description)"))
        for i in range(len(descr)):
            descr[i]['Vin'] = descr[i]['Vin'].replace("_", " ").capitalize()

        var3 = StringVar()
        for i in range(len(descr)):
            if descr[i]['Vin'] == PageRecommandation.vin.get():
                var3.set(descr[i]['Description'])

        self.description = Label(self.frame, textvariable=var3, font=("Helvetica", 10, "bold"),
                                 height=12, width=37, relief=FLAT).place(x=602, y=238)

        if len(DessertPage.vin_choc_set) != 0 or len(DessertPage.vin_fruits_set) != 0:
            self.label1
            self.label3
            self.description


        elif len(DessertPage.vin_choc_set) == 0 or len(DessertPage.vin_fruits_set) == 0:
            var2.set(
                "Aucune corréspondance a été trouvée\n pour le prix que vous avez indiqué.\n\n"
                "Vous pouvez modifier votre recherche\n en revenant\n à la page précédente")
            self.label2 = Label(self.frame, textvariable=var2, font=("Helvetica", 10, "bold"),
                                height=26, width=35, relief=FLAT).place(x=618, y=65)

    def close_window(self):
        self.master.destroy()

    def new_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = CavePage(self.newWindow)

class CavePage:
    """
    Classe qui affiche la liste de tous les bouteilles de la variété de vin recommandée qui sont contenues dans la
    base de connaissance
    """
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.master.title('DYONISO - CAVE')
        self.master.resizable(width="false", height="false")
        self.master.geometry("900x600+180+100")
        self.frame.pack()

        self.canvas = Canvas(self.frame, background="black")  # borderwidth=0,         #place canvas on self
        self.viewPort = Frame(self.canvas,
                              background="black")  # place a frame on the canvas, this frame will hold the child widgets
        self.vsb = Scrollbar(self.frame, orient="vertical", command=self.canvas.yview)  # place a scrollbar on self
        self.canvas.configure(yscrollcommand=self.vsb.set, width=700,
                              height=1000)  # attach scrollbar action to scroll of canvas

        self.vsb.pack(side="right", fill="y")  # pack scrollbar to right of self
        self.canvas.pack(side="left", fill="both", expand=True)  # pack canvas to left of self and expand to fil
        self.canvas_window = self.canvas.create_window((4, 4), window=self.viewPort, anchor="nw",
                                                       # add view port frame to canvas
                                                       tags="self.viewPort")

        self.viewPort.bind("<Configure>",
                           self.onFrameConfigure)  # bind an event whenever the size of the viewPort frame changes.
        self.canvas.bind("<Configure>",
                         self.onCanvasConfigure)  # bind an event whenever the size of the viewPort frame changes.

        self.onFrameConfigure(
            None)  # perform an initial stretch on render, otherwise the scroll region has a tiny border until the first resize

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox(
            "all"))  # whenever the size of the frame changes, alter the scroll region respectively.

    def onCanvasConfigure(self, event):
        '''Reset the canvas window to encompass inner frame when required'''
        canvas_width = event.width
        self.canvas.itemconfig(self.canvas_window,
                               width=canvas_width)  # whenever the size of the canvas changes alter the window region respectively.

        is_in = "is_in_"
        variables = "(X,Prix,Pays)"
        vin = PageRecommandation.vin.get().lower().replace(" ", "_")
        query = is_in + vin + variables
        ag = list(prolog.query("%s" % query))
        ag = sorted(ag, key=lambda k: k['Prix'])

        for i in range(len(ag)):
            Label(self.viewPort, text="Bouteille", borderwidth="1",
                  relief="solid", pady=10, width=70, fg='yellow', bg='black').grid(row=0, column=0)

            Label(self.viewPort, text="Prix €", borderwidth="1",
                  relief="solid", pady=10, width=10, fg='yellow', bg='black').grid(row=0, column=1)

            Label(self.viewPort, text="Pays", borderwidth="1",
                  relief="solid", pady=10, width=20, fg='yellow', bg='black').grid(row=0, column=2)

            vin = ag[i]['X'].title().replace("_", " ")
            Label(self.viewPort, text=vin, borderwidth="1",
                  relief="solid", pady=10, width=70, fg='white', bg='black').grid(row=i + 1, column=0)

            prix = ag[i]['Prix']
            Label(self.viewPort, text=prix, borderwidth="1",
                  relief="solid", pady=10, width=10, fg='white', bg='black').grid(row=i + 1, column=1)

            pays = ag[i]['Pays'].title().replace("_", " ")
            Label(self.viewPort, text=pays, borderwidth="1",
                  relief="solid", pady=10, width=20, fg='white', bg='black').grid(row=i + 1, column=2)