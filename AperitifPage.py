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


class AperitifPage:
    """
    Classe pour la création de la fenetre de dialogue de la catégorie Apéritif et pour la géstion du choix
    du type de vin
    """
    def __init__(self, master):
        '''
        Définition de la structure de la fenetre de dialogue: frame, image, butons et texte
        '''
        self.master = master
        self.frame = Frame(self.master)
        self.master.title('DYONISO - Apéritif')
        self.master.resizable(width="false", height="false")
        self.master.geometry("900x600+180+100")
        self.frame.pack()

        backgroundApero = 'C:/Users/enricazabaino/Projet/Wine_Recommender/Prolog/apero.png'

        photoApero = PhotoImage(file=backgroundApero)
        self.canvasApero = Canvas(self.frame, width=16000, height=2000)
        self.canvasApero.imageList = []
        self.canvasApero.pack()
        self.canvasApero.create_image(0, 0, anchor="nw", image=photoApero)
        self.canvasApero.imageList.append(photoApero)
        self.closeButton = Button(self.frame, padx=38, bd=5, text="Revenir au menu principal", bg='white',
                                  command=self.close_window)
        createCloseButton = self.canvasApero.create_window(735, 500, window=self.closeButton)

        info = StringVar()
        self.label1 = Label(self.frame, textvariable=info, fg="red", font=("Helvetica", 10, "bold"),
                            height=2, width=35, relief=RAISED).place(x=595, y=50)
        info.set("Vous avez choisi la catégorie Apéritif")

        '''
        Présentation de la 1ère question et des options de choix
        '''
        question1 = StringVar()
        self.question1Display = Label(self.frame, textvariable=question1, font=("Purisa", 10, "bold"), \
                                      height=2, width=35, relief=FLAT).place(x=595, y=115)

        question1.set("Indiquer le type de vin que vous préférez")

        AperitifPage.typeVin = IntVar()
        AperitifPage.typeVin.set(-1)
        self.optionBlanc = Radiobutton(self.frame, text="Blanc", variable=AperitifPage.typeVin, value=0, indicatoron=0,
                                       command=self.new_window, width=16)
        self.optionBlanc.place(relx=0.74, rely=0.27)
        self.optionRose = Radiobutton(self.frame, text="Rosé", variable=AperitifPage.typeVin, value=1, indicatoron=0,
                                      command=self.new_window, width=16)
        self.optionRose.place(relx=0.74, rely=0.33)
        self.optionRouge = Radiobutton(self.frame, text="Rouge", variable=AperitifPage.typeVin, value=2, indicatoron=0,
                                       command=self.new_window, width=16)
        self.optionRouge.place(relx=0.74, rely=0.39)
        self.optionNoPref = Radiobutton(self.frame, text="Aucune Préférence", variable=AperitifPage.typeVin, value=3,
                                        indicatoron=0, command=self.new_window, width=16)
        self.optionNoPref.place(relx=0.74, rely=0.45)

        '''
        Intérrogation de la base de connaissance pour récupérer la liste de tous les vins conseillés pour l'apéritif
        et mise en forme du texte
        '''

        AperitifPage.typeApero = list(prolog.query("type_apero(Vin, Type)"))

        for i in range(len(AperitifPage.typeApero)):
            AperitifPage.typeApero[i]['Vin'] = AperitifPage.typeApero[i]['Vin'].replace("_", " ").capitalize()

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
        '''
        Réplique de la structure de la fenetre de dialogue définie dans la classe précédente
        '''
        self.master = master
        self.frame = Frame(self.master)
        self.master.title('DYONISO - Apéritif')
        self.master.resizable(width="false", height="false")
        self.master.geometry("900x600+180+100")
        self.frame.pack()

        backgroundApero = 'C:/Users/enricazabaino/Projet/Wine_Recommender/Prolog/apero.png'

        photoApero = PhotoImage(file=backgroundApero)
        self.canvasApero = Canvas(self.frame, width=16000, height=2000)
        self.canvasApero.imageList = []
        self.canvasApero.pack()
        self.canvasApero.create_image(0, 0, anchor="nw", image=photoApero)
        self.canvasApero.imageList.append(photoApero)

        self.closeButton = Button(self.frame, padx=38, bd=5, text="Revenir à la page précédente", bg='white',
                                  command=self.close_window)
        createCloseButton = self.canvasApero.create_window(735, 500, window=self.closeButton)

        '''
        Répartition des vins suggérés par l'apéritif en différentes listes selon le type de vin choisi 
        par l'utilisateur
        '''
        AperitifPage.vin_blanc_list = []
        AperitifPage.vin_rose_list = []
        AperitifPage.vin_rouge_list = []
        AperitifPage.tous_vin_apero = []

        if AperitifPage.typeVin.get() == 0:
            for i in range(len(AperitifPage.typeApero)):
                if AperitifPage.typeApero[i]['Type'] == 'blanc':
                    AperitifPage.vin_blanc_list.append(AperitifPage.typeApero[i]['Vin'])

        elif AperitifPage.typeVin.get() == 1:
            for i in range(len(AperitifPage.typeApero)):
                if AperitifPage.typeApero[i]['Type'] == 'rose':
                    AperitifPage.vin_rose_list.append(AperitifPage.typeApero[i]['Vin'])

        elif AperitifPage.typeVin.get() == 2:
            for i in range(len(AperitifPage.typeApero)):
                if AperitifPage.typeApero[i]['Type'] == 'rouge':
                    AperitifPage.vin_rouge_list.append(AperitifPage.typeApero[i]['Vin'])

        elif AperitifPage.typeVin.get() == 3:
            for i in range(len(AperitifPage.typeApero)):
                AperitifPage.tous_vin_apero.append(AperitifPage.typeApero[i]['Vin'])


        '''
        Affichage d'une récapitulation du choix efféctué par l'utilisateur
        '''
        infoType = StringVar()
        if AperitifPage.typeVin.get() == 0:
            self.label = Label(self.frame, textvariable=infoType, fg="red", font=("Helvetica", 10, "bold"),
                               height=4, width=35, relief=RAISED, borderwidth=5, highlightcolor="white").place(x=595, y=50)
            infoType.set("Vous avez choisi la catégorie Apéritif\n\n Vous avez indiqué Blanc")

        elif AperitifPage.typeVin.get() == 1:
            self.label = Label(self.frame, textvariable=infoType, fg="red", font=("Helvetica", 10, "bold"),
                               height=4, width=35, relief=RAISED, borderwidth=5, highlightcolor="green").place(x=595, y=50)
            infoType.set("Vous avez choisi la catégorie Apéritif\n\n Vous avez indiqué Rosé")

        elif AperitifPage.typeVin.get() == 2:
            self.label = Label(self.frame, textvariable=infoType, fg="red", font=("Helvetica", 10, "bold"),
                               height=4, width=35, relief=RAISED, borderwidth=5, highlightcolor="white").place(x=595, y=50)
            infoType.set("Vous avez choisi la catégorie Apéritif\n\n Vous avez indiqué Rouge")

        elif AperitifPage.typeVin.get() == 3:
            self.label = Label(self.frame, textvariable=infoType, fg="red", font=("Helvetica", 10, "bold"),
                               height=4, width=35, relief=RAISED, borderwidth=5, highlightcolor="white").place(x=595, y=50)
            infoType.set("Vous avez choisi la catégorie Apéritif\n\n Vous avez indiqué Aucune Préférence")

        '''
        Présentation de la question sur le prix et des options de choix
        '''
        question2 = StringVar()
        self.question2Display = Label(self.frame, textvariable=question2, font=("Helvetica", 10, "bold"),
                                      height=6, width=37, relief=FLAT, anchor="e").place(x=595, y=122)
        question2.set("Est-ce que vous souhaitez indiquer\n combien vous voulez dépénser au maximum?")

        AperitifPage.choixDuPrix = IntVar()
        AperitifPage.choixDuPrix.set(-1)
        self.oui = Radiobutton(self.frame, text="Oui", variable=AperitifPage.choixDuPrix, value=0,
                               command=self.choix_prixApero)
        self.oui.place(relx=0.75, rely=0.37)
        self.non = Radiobutton(self.frame, text="Non", variable=AperitifPage.choixDuPrix, value=1,
                               command=self.choix_prixApero)
        self.non.place(relx=0.75, rely=0.43)


    def choix_prixApero(self):
        '''
        Fonction qui gère les cas où l'utilisateur choisisse d'indiquer ou de ne pas indiquer un prix maximum
        '''
        self.e = StringVar()

        if AperitifPage.choixDuPrix.get() == 0:
            entreePrix = Entry(self.frame, textvariable=self.e, bg='bisque', fg='maroon').place(relx=0.82, rely=0.37)
            self.validerButton = Button(self.frame, text="Valider", command=self.valider).place(x=708, y=300)

        elif AperitifPage.choixDuPrix.get() == 1:
            self.newWindow = Toplevel(self.master)
            self.app = PageRecommandation(self.newWindow)

    def valider(self):
        '''
        Fonction qui récupère les vins contenus dans la base de connaissance ayant le type et le prix corrésponent aux
        choix de l'utilisateur
        return:
            un set de vins
        '''
        self.prix = int(self.e.get())

        AperitifPage.type_apero = list(prolog.query("type_apero(Vin, Type)"))
        AperitifPage.prix_vin_apero = list(prolog.query("prix_apero(Vin, Prix)"))
        AperitifPage.prix_apero_blanc = list(prolog.query("prix_apero_blanc(Vin, Prix)"))
        AperitifPage.prix_apero_rose = list(prolog.query("prix_apero_rose(Vin, Prix)"))
        AperitifPage.prix_apero_rouge = list(prolog.query("prix_apero_rouge(Vin, Prix)"))

        for i in range(len(AperitifPage.type_apero)):
            AperitifPage.type_apero[i]['Vin'] = AperitifPage.type_apero[i]['Vin'].replace("_", " ").capitalize()

        for i in range(len(AperitifPage.prix_vin_apero)):
            AperitifPage.prix_vin_apero[i]['Vin'] = AperitifPage.prix_vin_apero[i]['Vin'].replace("_", " ").capitalize()

        for i in range(len(AperitifPage.prix_apero_blanc)):
            AperitifPage.prix_apero_blanc[i]['Vin'] = AperitifPage.prix_apero_blanc[i]['Vin'].replace("_", " ").capitalize()

        for i in range(len(AperitifPage.prix_apero_rose)):
            AperitifPage.prix_apero_rose[i]['Vin'] = AperitifPage.prix_apero_rose[i]['Vin'].replace("_", " ").capitalize()

        for i in range(len(AperitifPage.prix_apero_rouge)):
            AperitifPage.prix_apero_rouge[i]['Vin'] = AperitifPage.prix_apero_rouge[i]['Vin'].replace("_", " ").capitalize()

        AperitifPage.vin_blanc = []
        AperitifPage.vin_rose = []
        AperitifPage.vin_rouge = []
        AperitifPage.tousVins = []

        if AperitifPage.typeVin.get() == 0:
            for i in range(len(AperitifPage.prix_apero_blanc)):
                if AperitifPage.prix_apero_blanc[i]['Prix'] == self.prix:
                    AperitifPage.vin_blanc.append(AperitifPage.prix_apero_blanc[i]['Vin'])

        elif AperitifPage.typeVin.get() == 1:
            for i in range(len(AperitifPage.prix_apero_rose)):
                if AperitifPage.prix_apero_rose[i]['Prix'] == self.prix:
                    AperitifPage.vin_rose.append(AperitifPage.prix_apero_rose[i]['Vin'])

        elif AperitifPage.typeVin.get() == 2:
            for i in range(len(AperitifPage.prix_apero_rouge)):
                if AperitifPage.prix_apero_rouge[i]['Prix'] == self.prix:
                    AperitifPage.vin_rouge.append(AperitifPage.prix_apero_rouge[i]['Vin'])

        elif AperitifPage.typeVin.get() == 3:
            for i in range(len(AperitifPage.prix_vin_apero)):
                if AperitifPage.prix_vin_apero[i]['Prix'] == self.prix:
                    AperitifPage.tousVins.append(AperitifPage.prix_vin_apero[i]['Vin'])

        AperitifPage.vin_blanc_set = set(AperitifPage.vin_blanc)
        AperitifPage.vin_rose_set = set(AperitifPage.vin_rose)
        AperitifPage.vin_rouge_set = set(AperitifPage.vin_rouge)
        AperitifPage.tousVins_set = set(AperitifPage.tousVins)

        self.newWindow = Toplevel(self.master)
        self.app = PageRecommandation(self.newWindow)

    def close_window(self):
        self.master.destroy()

class PageRecommandation:
    """
    Classe qui gère l'affichage de la variété de vin recommandée en fonction des choix effectués dans les étapes
    précédentes
    """
    def __init__(self, AperitifPage):
        self.master = AperitifPage
        self.frame = Frame(self.master)
        self.master.title('OINOS - Recommandation')
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
                                  command=self.conseilApero)
        createCloseButton = self.canvasRecom.create_window(750, 200, window=self.RecomButton)

        self.CaveButton = Button(self.frame, padx=38, bd=5, text="Notre cave à vin", bg='white',
                                 command=self.new_window)
        createCaveButton = self.canvasRecom.create_window(750, 500, window=self.CaveButton)

        self.closeButton = Button(self.frame, padx=38, bd=5, text="Revenir à la page précédente", bg='white',
                                  command=self.close_window)
        createCloseButton = self.canvasRecom.create_window(750, 550, window=self.closeButton)

    def conseilApero(self):
        self.RecomButton.destroy()

        var = StringVar()
        var.set("On vous conseille le cépage")
        self.label1 = Label(self.frame, textvariable=var, font=("Helvetica", 10, "bold"),
                            height=2, width=35, relief=FLAT).place(x=605, y=180)

        PageRecommandation.vin = StringVar()
        self.label3 = Label(self.frame, textvariable=PageRecommandation.vin, fg="red", font=("Helvetica", 10, "bold"),
                            height=2, width=35, relief=FLAT).place(x=605, y=210)

        var2 = StringVar()

        if AperitifPage.typeVin.get() == 0 and AperitifPage.choixDuPrix.get() == 0:
            if len(AperitifPage.vin_blanc_set) != 0:
                PageRecommandation.vin.set(random.choice(tuple(AperitifPage.vin_blanc_set)))


        elif AperitifPage.typeVin.get() == 1 and AperitifPage.choixDuPrix.get() == 0:
            if len(AperitifPage.vin_rose_set) != 0:
                PageRecommandation.vin.set(random.choice(tuple(AperitifPage.vin_rose_set)))

        elif AperitifPage.typeVin.get() == 2 and AperitifPage.choixDuPrix.get() == 0:
            if len(AperitifPage.vin_rouge_set) != 0:
                PageRecommandation.vin.set(random.choice(tuple(AperitifPage.vin_rouge_set)))

        elif AperitifPage.typeVin.get() == 3 and AperitifPage.choixDuPrix.get() == 0:
            if len(AperitifPage.tousVins_set) != 0:
                PageRecommandation.vin.set(random.choice(tuple(AperitifPage.tousVins_set)))


        elif AperitifPage.typeVin.get() == 0 and AperitifPage.choixDuPrix.get() == 1:
            PageRecommandation.vin.set(random.choice(AperitifPage.vin_blanc_list))

        elif AperitifPage.typeVin.get() == 1 and AperitifPage.choixDuPrix.get() == 1:
            PageRecommandation.vin.set(random.choice(AperitifPage.vin_rose_list))

        elif AperitifPage.typeVin.get() == 2 and AperitifPage.choixDuPrix.get() == 1:
            PageRecommandation.vin.set(random.choice(AperitifPage.vin_rouge_list))


        elif AperitifPage.typeVin.get() == 3 and AperitifPage.choixDuPrix.get() == 1:
            PageRecommandation.vin.set(random.choice(AperitifPage.typeApero)['Vin'])


        descr = list(prolog.query("description(Vin, Description)"))

        for i in range(len(descr)):
            descr[i]['Vin'] = descr[i]['Vin'].replace("_", " ").capitalize()

        var3 = StringVar()
        for i in range(len(descr)):
            if descr[i]['Vin'] == PageRecommandation.vin.get():
                var3.set(descr[i]['Description'])

        self.description = Label(self.frame, textvariable=var3, font=("Helvetica", 10, "bold"),
                                 height=12, width=37, relief=FLAT).place(x=602, y=238)

        if len(AperitifPage.vin_blanc_set) != 0 or len(AperitifPage.vin_rose_set) != 0 or len(
                AperitifPage.vin_rouge_set) != 0 or len(AperitifPage.tousVins_set) != 0:

            self.label1
            self.label3
            self.description

        elif len(AperitifPage.vin_blanc_set) == 0 or len(AperitifPage.vin_rose_set) == 0 or len(
                AperitifPage.vin_rouge_set) == 0 or \
                len(AperitifPage.tousVins_set) == 0:

            var2.set(
            "Aucune corréspondance a été trouvée\n pour le prix que vous avez indiqué.\n\nVous pouvez modifier votre "
            "recherche\n en revenant\n à la page précédente")
            self.label2 = Label(self.frame, textvariable=var2, font=("Helvetica", 10, "bold"),
                                height=16, width=35, relief=FLAT).place(x=618, y=130)

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

        self.canvas = Canvas(self.frame, background="black")
        self.viewPort = Frame(self.canvas,
                              background="black")
        self.vsb = Scrollbar(self.frame, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set, width=700,
                              height=1000)

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas_window = self.canvas.create_window((4, 4), window=self.viewPort, anchor="nw",
                                                       tags="self.viewPort")

        self.viewPort.bind("<Configure>",
                           self.onFrameConfigure)
        self.canvas.bind("<Configure>",
                         self.onCanvasConfigure)

        self.onFrameConfigure(
            None)

    def onFrameConfigure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox(
            "all"))

    def onCanvasConfigure(self, event):
        canvas_width = event.width
        self.canvas.itemconfig(self.canvas_window,
                               width=canvas_width)

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




