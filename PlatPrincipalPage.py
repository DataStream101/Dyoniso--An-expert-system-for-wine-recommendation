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

class PlatPrincipalPage:
    """
    Classe pour la création de la fenetre de dialogue de la catégorie Plat Principal et pour la géstion du choix
    du type de plat
    """
    def __init__(self, master):
        '''
        Définition de la structure de la fenetre de dialogue: frame, image, butons et texte
        '''
        self.master = master
        self.frame = Frame(self.master)
        self.master.title('DYONISO - Plat Principal')
        self.master.resizable(width="false", height="false")
        self.master.geometry("900x600+180+100")
        self.frame.pack()

        backgroundPP = 'C:/Users/enricazabaino/Projet/Wine_Recommender/Prolog/plat_principal.png'


        photoPP = PhotoImage(file= backgroundPP)
        self.canvasPP = Canvas(self.frame, width=16000, height=2000)
        self.canvasPP.imageList = []
        self.canvasPP.pack()
        self.canvasPP.create_image(0, 0, anchor="nw", image=photoPP)
        self.canvasPP.imageList.append(photoPP)

        self.closeButton = Button(self.frame, padx = 38, bd = 5, text = "Revenir au menu principal", bg ='white', \
                                  command = self.close_window)
        createCloseButton = self.canvasPP.create_window(737, 500, window=self.closeButton)

        info = StringVar()
        self.label1 = Label(self.frame, textvariable = info, fg = "red", font = ("Helvetica" ,10, "bold"), \
                            height = 2, width = 35, relief = RAISED).place(x= 595 ,y = 50)
        info.set("Vous avez choisi la catégorie Plat Principal")

        '''
        Présentation de la 1ère question et des options de choix
        '''
        question1 = StringVar()
        self.question1Display = Label(self.frame, textvariable = question1, font = ("Purisa" ,10, "bold"), \
                                      height = 2, width = 35, relief = FLAT).place(x= 595 ,y = 115)

        question1.set("Sélectionner une catégorie de plat")

        PlatPrincipalPage.typePP = IntVar()
        PlatPrincipalPage.typePP.set(-1)
        self.optionViande = Radiobutton(self.frame, text="Viande", variable=PlatPrincipalPage.typePP, value=0, indicatoron =0, \
                                        height =1, width =20, command = self.new_window)
        self.optionViande.place(relx = 0.75, rely = 0.30)
        self.optionPoisson = Radiobutton(self.frame, text="Poisson", variable=PlatPrincipalPage.typePP, value=1, indicatoron =0, \
                                         height =1, width =20, command = self.new_window)
        self.optionPoisson.place(relx = 0.75, rely = 0.36)
        self.optionPates = Radiobutton(self.frame, text="Pâtes ou Riz", variable=PlatPrincipalPage.typePP, value=2, indicatoron =0, \
                                       height =1, width =20, command = self.new_window)
        self.optionPates.place(relx = 0.75, rely = 0.42)
        self.optionExotique = Radiobutton(self.frame, text="Exotiques ou Épicés", variable=PlatPrincipalPage.typePP, value=3, indicatoron =0, \
                                          height =1, width =20, command = self.new_window)
        self.optionExotique.place(relx = 0.75, rely = 0.48)
        self.optionVeg = Radiobutton(self.frame, text="Végétariens", variable=PlatPrincipalPage.typePP, value=4, indicatoron =0, \
                                     height =1, width =20, command = self.new_window)
        self.optionVeg.place(relx = 0.75, rely = 0.54)

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
        self.app = Recette(self.newWindow)

class Recette:
    """
    Classe qui permet de gérérer la saisie du nom du plat que l'utilisateur va serivres
    """
    def __init__(self, master):
        '''
        Réplique de la structure de la fenetre de dialogue définie dans la classe précédente
        '''
        self.master = master
        self.frame = Frame(self.master)
        self.master.title('DYONISO - Plat Principal')
        self.master.resizable(width="false", height="false")
        self.master.geometry("900x600+180+100")
        self.frame.pack()

        backgroundPP = 'C:/Users/enricazabaino/Projet/Wine_Recommender/Prolog/plat_principal.png'


        photoPP = PhotoImage(file= backgroundPP)
        self.canvasPP = Canvas(self.frame, width=16000, height=2000)
        self.canvasPP.imageList = []
        self.canvasPP.pack()
        self.canvasPP.create_image(0, 0, anchor="nw", image=photoPP)
        self.canvasPP.imageList.append(photoPP)

        self.closeButton = Button(self.frame, padx = 38, bd = 5, text = "Revenir à la page précédente", bg ='white',
                                  command = self.close_window)
        createCloseButton = self.canvasPP.create_window(737, 500, window=self.closeButton)

        infoType = StringVar()
        '''
        Affichage d'une récapitulation du choix efféctué par l'utilisateur
        '''
        if PlatPrincipalPage.typePP.get() == 0:
            self.label = Label(self.frame, textvariable=infoType, fg="red", font=("Helvetica", 10, "bold"), \
                               height=4, width=35, relief=RAISED, borderwidth=5, highlightcolor="white").place(x=595,
                                                                                                               y=50)
            infoType.set("Vous avez choisi la catégorie Plat Principal\n\n Vous avez choisi l'option 'Viande'")

        elif PlatPrincipalPage.typePP.get() == 1:
            self.label = Label(self.frame, textvariable=infoType, fg="red", font=("Helvetica", 10, "bold"), \
                               height=4, width=35, relief=RAISED, borderwidth=5, highlightcolor="green").place(x=595,
                                                                                                               y=50)
            infoType.set("Vous avez choisi la catégorie Plat Principal\n\n Vous avez choisi l'option 'Poisson'")

        elif PlatPrincipalPage.typePP.get() == 2:
            self.label = Label(self.frame, textvariable=infoType, fg="red", font=("Helvetica", 10, "bold"), \
                               height=4, width=35, relief=RAISED, borderwidth=5, highlightcolor="green").place(x=595,
                                                                                                               y=50)
            infoType.set("Vous avez choisi la catégorie Plat Principal\n\n Vous avez choisi l'option 'Pâtes ou Riz'")

        elif PlatPrincipalPage.typePP.get() == 3:
            self.label = Label(self.frame, textvariable=infoType, fg="red", font=("Helvetica", 10, "bold"), \
                               height=4, width=35, relief=RAISED, borderwidth=5, highlightcolor="green").place(x=595,
                                                                                                               y=50)
            infoType.set(
                "Vous avez choisi la catégorie Plat Principal\n\n Vous avez choisi l'option 'Exotiques\nou Épicés'")

        elif PlatPrincipalPage.typePP.get() == 4:
            self.label = Label(self.frame, textvariable=infoType, fg="red", font=("Helvetica", 10, "bold"), \
                               height=4, width=35, relief=RAISED, borderwidth=5, highlightcolor="green").place(x=595,
                                                                                                               y=50)
            infoType.set("Vous avez choisi la catégorie Plat Principal\n\n Vous avez choisi l'option 'Végétariens'")

        '''
        Question sur le nom de la recette.
        '''
        questionIngredient = StringVar()
        self.questionIngredientDisplay = Label(self.frame, textvariable=questionIngredient,
                                               font=("Helvetica", 10, "bold"), \
                                               height=8, width=37, relief=FLAT).place(x=585, y=122)
        questionIngredient.set("Indiquer le nom de votre recette")

        self.e = StringVar()
        choixRecette = Entry(self.frame, textvariable=self.e, bg='bisque', fg='maroon').place(relx=0.67, rely=0.37, \
                                                                                              width=265, height=130)
        self.validerButton = Button(self.frame, padx=38, bd=5, text="Valider", bg='white', \
                                    command=self.validerRecette).place(x=675, y=410)


        '''
        Intérrogation de la base de connaissance pour récupérer la liste de tous les vins conseillés pour chaque 
        ingrédient du plat principal et mise en forme du texte
        '''
        PlatPrincipalPage.v_rouge = list(prolog.query("is_in_v_rouge(X, Vin)"))
        PlatPrincipalPage.v_blanche = list(prolog.query("is_in_v_blanche(X, Vin)"))
        PlatPrincipalPage.gibier = list(prolog.query("is_in_gibier(X, Vin)"))
        PlatPrincipalPage.p_mer = list(prolog.query("is_in_p_mer(X, Vin)"))
        PlatPrincipalPage.p_douce = list(prolog.query("is_in_p_douce(X, Vin)"))
        PlatPrincipalPage.coquillages = list(prolog.query("is_in_coquillages(X, Vin)"))
        PlatPrincipalPage.crustaces = list(prolog.query("is_in_crustaces(X, Vin)"))
        PlatPrincipalPage.f_dur = list(prolog.query("is_in_f_dur(X, Vin)"))
        PlatPrincipalPage.f_mol = list(prolog.query("is_in_f_mol(X, Vin)"))
        PlatPrincipalPage.veg = list(prolog.query("is_in_vegetarien(X, Vin)"))
        PlatPrincipalPage.charc = list(prolog.query("is_in_charcuteries(X, Vin)"))
        PlatPrincipalPage.exo = list(prolog.query("prix_exotique(Vin,Prix)"))

        for i in range(len(PlatPrincipalPage.v_rouge)):
            PlatPrincipalPage.v_rouge[i]['Vin'] = PlatPrincipalPage.v_rouge[i]['Vin'].replace("_", " ").capitalize()
        for i in range(len(PlatPrincipalPage.v_blanche)):
            PlatPrincipalPage.v_blanche[i]['Vin'] = PlatPrincipalPage.v_blanche[i]['Vin'].replace("_", " ").capitalize()
        for i in range(len(PlatPrincipalPage.gibier)):
            PlatPrincipalPage.gibier[i]['Vin'] = PlatPrincipalPage.gibier[i]['Vin'].replace("_", " ").capitalize()
        for i in range(len(PlatPrincipalPage.p_mer)):
            PlatPrincipalPage.p_mer[i]['Vin'] = PlatPrincipalPage.p_mer[i]['Vin'].replace("_", " ").capitalize()
        for i in range(len(PlatPrincipalPage.p_douce)):
            PlatPrincipalPage.p_douce[i]['Vin'] = PlatPrincipalPage.p_douce[i]['Vin'].replace("_", " ").capitalize()
        for i in range(len(PlatPrincipalPage.coquillages)):
            PlatPrincipalPage.coquillages[i]['Vin'] = PlatPrincipalPage.coquillages[i]['Vin'].replace("_",                                                                                         " ").capitalize()
        for i in range(len(PlatPrincipalPage.crustaces)):
            PlatPrincipalPage.crustaces[i]['Vin'] = PlatPrincipalPage.crustaces[i]['Vin'].replace("_", " ").capitalize()
        for i in range(len(PlatPrincipalPage.f_dur)):
            PlatPrincipalPage.f_dur[i]['Vin'] = PlatPrincipalPage.f_dur[i]['Vin'].replace("_", " ").capitalize()
        for i in range(len(PlatPrincipalPage.f_mol)):
            PlatPrincipalPage.f_mol[i]['Vin'] = PlatPrincipalPage.f_mol[i]['Vin'].replace("_", " ").capitalize()
        for i in range(len(PlatPrincipalPage.veg)):
            PlatPrincipalPage.veg[i]['Vin'] = PlatPrincipalPage.veg[i]['Vin'].replace("_", " ").capitalize()
        for i in range(len(PlatPrincipalPage.p_douce)):
            PlatPrincipalPage.charc[i]['Vin'] = PlatPrincipalPage.charc[i]['Vin'].replace("_", " ").capitalize()
        for i in range(len(PlatPrincipalPage.exo)):
            PlatPrincipalPage.exo[i]['Vin'] = PlatPrincipalPage.exo[i]['Vin'].replace("_", " ").capitalize()

    def validerRecette(self):
        '''
        Fonction qui récupère les vins contenus dans la base de connaissance suggérés pour le type d'ingrédient contenu
        dans la recette saisie par l'utilisateur
        '''
        def text_split(text):
            '''
            Fonction qui récupère le texte saisi par l'utilisateur et le met en forme de façon de le rendre compatible
            avec la syntaxe utilisée pour l'implémentation de la base des connaissances
            '''
            text = unicodedata.normalize('NFD', text)
            text = text.encode('ascii', 'ignore')
            text = text.decode("utf-8")
            text = text.lower().split()
            return text

        recette = self.e.get()
        recette = text_split(recette)

        PlatPrincipalPage.viande_rouge = []
        PlatPrincipalPage.viande_blanche = []
        PlatPrincipalPage.gibier = []
        PlatPrincipalPage.poisson_mer = []
        PlatPrincipalPage.poisson_douce = []
        PlatPrincipalPage.coquillages = []
        PlatPrincipalPage.crustaces = []
        PlatPrincipalPage.pates = []
        PlatPrincipalPage.vegetarien = []
        PlatPrincipalPage.exotique = []

        if PlatPrincipalPage.typePP.get() == 0:

            for k in range(len(recette)):
                for i in range(len(PlatPrincipalPage.v_rouge)):
                    if recette[k] == PlatPrincipalPage.v_rouge[i]['X']:
                        PlatPrincipalPage.viande_rouge.append(PlatPrincipalPage.v_rouge[i]['Vin'])

            for k in range(len(recette)):
                for i in range(len(PlatPrincipalPage.v_blanche)):
                    if recette[k] == PlatPrincipalPage.v_blanche[i]['X']:
                        PlatPrincipalPage.viande_blanche.append(PlatPrincipalPage.v_blanche[i]['Vin'])

            for k in range(len(recette)):
                for i in range(len(PlatPrincipalPage.gibier)):
                    if recette[k] == PlatPrincipalPage.gibier[i]['X']:
                        PlatPrincipalPage.gibier.append(PlatPrincipalPage.gibier[i]['Vin'])

        elif PlatPrincipalPage.typePP.get() == 1:
            for k in range(len(recette)):
                for i in range(len(PlatPrincipalPage.p_mer)):
                    if recette[k] == PlatPrincipalPage.p_mer[i]['X']:
                        PlatPrincipalPage.poisson_mer.append(PlatPrincipalPage.p_mer[i]['Vin'])

            for k in range(len(recette)):
                for i in range(len(PlatPrincipalPage.p_douce)):
                    if recette[k] == PlatPrincipalPage.p_douce[i]['X']:
                        PlatPrincipalPage.poisson_douce.append(PlatPrincipalPage.p_douce[i]['Vin'])

            for k in range(len(recette)):
                for i in range(len(PlatPrincipalPage.coquillages)):
                    if recette[k] == PlatPrincipalPage.coquillages[i]['X']:
                        PlatPrincipalPage.coquillages.append(PlatPrincipalPage.coquillages[i]['Vin'])

            for k in range(len(recette)):
                for i in range(len(PlatPrincipalPage.crustaces)):
                    if recette[k] == PlatPrincipalPage.crustaces[i]['X']:
                        PlatPrincipalPage.crustaces.append(PlatPrincipalPage.crustaces[i]['Vin'])

        elif PlatPrincipalPage.typePP.get() == 2:

            for k in range(len(recette)):
                for i in range(len(PlatPrincipalPage.p_mer)):
                    if recette[k] == PlatPrincipalPage.p_mer[i]['X']:
                        PlatPrincipalPage.pates.append(PlatPrincipalPage.p_mer[i]['Vin'])

            for k in range(len(recette)):
                for i in range(len(PlatPrincipalPage.p_douce)):
                    if recette[k] == PlatPrincipalPage.p_douce[i]['X']:
                        PlatPrincipalPage.pates.append(PlatPrincipalPage.p_douce[i]['Vin'])

            for k in range(len(recette)):
                for i in range(len(PlatPrincipalPage.coquillages)):
                    if recette[k] == PlatPrincipalPage.coquillages[i]['X']:
                        PlatPrincipalPage.pates.append(PlatPrincipalPage.coquillages[i]['Vin'])

            for k in range(len(recette)):
                for i in range(len(PlatPrincipalPage.crustaces)):
                    if recette[k] == PlatPrincipalPage.crustaces[i]['X']:
                        PlatPrincipalPage.pates.append(PlatPrincipalPage.crustaces[i]['Vin'])

            for k in range(len(recette)):
                for i in range(len(PlatPrincipalPage.v_rouge)):
                    if recette[k] == PlatPrincipalPage.v_rouge[i]['X']:
                        PlatPrincipalPage.pates.append(PlatPrincipalPage.v_rouge[i]['Vin'])

            for k in range(len(recette)):
                for i in range(len(PlatPrincipalPage.v_blanche)):
                    if recette[k] == PlatPrincipalPage.v_blanche[i]['X']:
                        PlatPrincipalPage.pates.append(PlatPrincipalPage.v_blanche[i]['Vin'])

            for k in range(len(recette)):
                for i in range(len(PlatPrincipalPage.gibier)):
                    if recette[k] == PlatPrincipalPage.gibier[i]['X']:
                        PlatPrincipalPage.pates.append(PlatPrincipalPage.gibier[i]['Vin'])

            for k in range(len(recette)):
                for i in range(len(PlatPrincipalPage.f_dur)):
                    if recette[k] == PlatPrincipalPage.f_dur[i]['X']:
                        PlatPrincipalPage.pates.append(PlatPrincipalPage.f_dur[i]['Vin'])

            for k in range(len(recette)):
                for i in range(len(PlatPrincipalPage.f_mol)):
                    if recette[k] == PlatPrincipalPage.f_mol[i]['X']:
                        PlatPrincipalPage.pates.append(PlatPrincipalPage.f_mol[i]['Vin'])

            for k in range(len(recette)):
                for i in range(len(PlatPrincipalPage.veg)):
                    if recette[k] == PlatPrincipalPage.veg[i]['X']:
                        PlatPrincipalPage.pates.append(PlatPrincipalPage.veg[i]['Vin'])

            for k in range(len(recette)):
                for i in range(len(PlatPrincipalPage.charc)):
                    if recette[k] == PlatPrincipalPage.charc[i]['X']:
                        PlatPrincipalPage.pates.append(PlatPrincipalPage.charc[i]['Vin'])

        elif PlatPrincipalPage.typePP.get() == 3:
            for i in range(len(PlatPrincipalPage.exo)):
                PlatPrincipalPage.exotique.append(PlatPrincipalPage.exo[i]['Vin'])


        elif PlatPrincipalPage.typePP.get() == 4:

            for k in range(len(recette)):
                for i in range(len(PlatPrincipalPage.veg)):
                    if recette[k] == PlatPrincipalPage.veg[i]['X']:
                        PlatPrincipalPage.vegetarien.append(PlatPrincipalPage.veg[i]['Vin'])

        self.newWindow = Toplevel(self.master)
        self.app = PagePrix(self.newWindow)


    def close_window(self):
        self.master.destroy()


class PagePrix:
    """
    Classe qui permet de gérérer le choix du prix
    """
    def __init__(self, PlatPrincipalPage):
        self.master = PlatPrincipalPage
        self.frame = Frame(self.master)
        self.master.title('DYONISO - Plat Principal')
        self.master.resizable(width="false", height="false")
        self.master.geometry("900x600+180+100")
        self.frame.pack()

        backgroundPP = 'C:/Users/enricazabaino/Projet/Wine_Recommender/Prolog/plat_principal.png'

        photoPP = PhotoImage(file=backgroundPP)
        self.canvasPP = Canvas(self.frame, width=16000, height=2000)
        self.canvasPP.imageList = []
        self.canvasPP.pack()
        self.canvasPP.create_image(0, 0, anchor="nw", image=photoPP)
        self.canvasPP.imageList.append(photoPP)

        self.closeButton = Button(self.frame, padx=38, bd=5, text="Revenir à la page précedente", bg='white', \
                                  command=self.close_window)
        createCloseButton = self.canvasPP.create_window(737, 500, window=self.closeButton)

        question = StringVar()
        self.questionDisplay = Label(self.frame, textvariable=question, font=("Helvetica", 10, "bold"), \
                                     height=6, width=37, relief=FLAT, anchor="e").place(x=595, y=122)
        question.set("Est-ce que vous souhaitez indiquer\n combien vous voulez dépénser au maximum?")

        PagePrix.choixDuPrix = IntVar()
        PagePrix.choixDuPrix.set(-1)
        self.oui = Radiobutton(self.frame, text="Oui", variable=PagePrix.choixDuPrix, value=0, \
                               command=self.choix_prix)
        self.oui.place(relx=0.75, rely=0.37)
        self.non = Radiobutton(self.frame, text="Non", variable=PagePrix.choixDuPrix, value=1, \
                               command=self.choix_prix)
        self.non.place(relx=0.75, rely=0.43)

    def choix_prix(self):
        '''
        Fonction qui gère les cas où l'utilisateur choisisse d'indiquer ou de ne pas indiquer un prix maximum
        '''
        self.e = StringVar()
        if PagePrix.choixDuPrix.get() == 0:
            entreePrix = Entry(self.frame, textvariable=self.e, bg='bisque', fg='maroon').place(relx=0.82, rely=0.37)
            self.validerButton = Button(self.frame, text="Valider", \
                                        command=self.validerPrix).place(x=708, y=300)

        elif PagePrix.choixDuPrix.get() == 1:
            self.newWindow = Toplevel(self.master)
            self.app = PageRecommandation(self.newWindow)

    def validerPrix(self):
        '''
        Fonction qui récupère les vins contenus dans la base de connaissance par ingrédient et dont le prix corréspond
        au choix de l'utilisateur
        return:
            un set de vins
        '''
        PagePrix.prixVin_coquillages = list(prolog.query("pp_coquillages_prix(Vin, Prix)"))
        PagePrix.prixVin_crustaces = list(prolog.query("pp_crustaces_prix(Vin, Prix)"))
        PagePrix.prixVin_poissonMer = list(prolog.query("pp_p_mer_prix(Vin, Prix)"))
        PagePrix.prixVin_poissonEauDouce = list(prolog.query("pp_p_douce_prix(Vin, Prix)"))
        PagePrix.prixVin_vegetarien = list(prolog.query("pp_vegetarien_prix(Vin, Prix)"))
        PagePrix.prixVin_viandeBlanche = list(prolog.query("pp_v_blanche_prix(Vin, Prix)"))
        PagePrix.prixVin_viandeRouge = list(prolog.query("pp_v_rouge_prix(Vin, Prix)"))
        PagePrix.prixVin_gibier = list(prolog.query("pp_gibier_prix(Vin, Prix)"))
        PagePrix.prixVin_charcuterie = list(prolog.query("pp_charcuterie_prix(Vin, Prix)"))
        PagePrix.prixVin_fromDur = list(prolog.query("pp_f_dur_prix(Vin, Prix)"))
        PagePrix.prixVin_fromMol = list(prolog.query("pp_f_mol_prix(Vin, Prix)"))

        for i in range(len(PagePrix.prixVin_coquillages)):
            PagePrix.prixVin_coquillages[i]['Vin'] = PagePrix.prixVin_coquillages[i]['Vin'].replace("_",
                                                                                                    " ").capitalize()
        for i in range(len(PagePrix.prixVin_crustaces)):
            PagePrix.prixVin_crustaces[i]['Vin'] = PagePrix.prixVin_crustaces[i]['Vin'].replace("_", " ").capitalize()
        for i in range(len(PagePrix.prixVin_poissonMer)):
            PagePrix.prixVin_poissonMer[i]['Vin'] = PagePrix.prixVin_poissonMer[i]['Vin'].replace("_", " ").capitalize()
        for i in range(len(PagePrix.prixVin_poissonEauDouce)):
            PagePrix.prixVin_poissonEauDouce[i]['Vin'] = PagePrix.prixVin_poissonEauDouce[i]['Vin'].replace("_",
                                                                                                            " ").capitalize()
        for i in range(len(PagePrix.prixVin_vegetarien)):
            PagePrix.prixVin_vegetarien[i]['Vin'] = PagePrix.prixVin_vegetarien[i]['Vin'].replace("_", " ").capitalize()
        for i in range(len(PagePrix.prixVin_viandeBlanche)):
            PagePrix.prixVin_viandeBlanche[i]['Vin'] = PagePrix.prixVin_viandeBlanche[i]['Vin'].replace("_",
                                                                                                        " ").capitalize()
        for i in range(len(PagePrix.prixVin_viandeRouge)):
            PagePrix.prixVin_viandeRouge[i]['Vin'] = PagePrix.prixVin_viandeRouge[i]['Vin'].replace("_",
                                                                                                    " ").capitalize()
        for i in range(len(PagePrix.prixVin_gibier)):
            PagePrix.prixVin_gibier[i]['Vin'] = PagePrix.prixVin_gibier[i]['Vin'].replace("_", " ").capitalize()
        for i in range(len(PagePrix.prixVin_charcuterie)):
            PagePrix.prixVin_charcuterie[i]['Vin'] = PagePrix.prixVin_charcuterie[i]['Vin'].replace("_",
                                                                                                    " ").capitalize()
        for i in range(len(PagePrix.prixVin_fromDur)):
            PagePrix.prixVin_fromDur[i]['Vin'] = PagePrix.prixVin_fromDur[i]['Vin'].replace("_", " ").capitalize()
        for i in range(len(PagePrix.prixVin_fromMol)):
            PagePrix.prixVin_fromMol[i]['Vin'] = PagePrix.prixVin_fromMol[i]['Vin'].replace("_", " ").capitalize()

        self.prix = int(self.e.get())

        PagePrix.vin_viande = []
        PagePrix.vin_poisson = []
        PagePrix.vin_pates = []
        PagePrix.vin_exotique = PlatPrincipalPage.exotique
        PagePrix.vin_vegetarien = []

        if PlatPrincipalPage.typePP.get() == 0:
            for i in range(len(PagePrix.prixVin_viandeBlanche)):
                if PagePrix.prixVin_viandeBlanche[i]['Prix'] == self.prix:
                    PagePrix.vin_viande.append(PagePrix.prixVin_viandeBlanche[i]['Vin'])

            for i in range(len(PagePrix.prixVin_viandeRouge)):
                if PagePrix.prixVin_viandeRouge[i]['Prix'] == self.prix:
                    PagePrix.vin_viande.append(PagePrix.prixVin_viandeRouge[i]['Vin'])

            for i in range(len(PagePrix.prixVin_gibier)):
                if PagePrix.prixVin_gibier[i]['Prix'] == self.prix:
                    PagePrix.vin_viande.append(PagePrix.prixVin_gibier[i]['Vin'])

        elif PlatPrincipalPage.typePP.get() == 1:
            for i in range(len(PagePrix.prixVin_coquillages)):
                if PagePrix.prixVin_coquillages[i]['Prix'] == self.prix:
                    PagePrix.vin_poisson.append(PagePrix.prixVin_coquillages[i]['Vin'])

            for i in range(len(PagePrix.prixVin_crustaces)):
                if PagePrix.prixVin_crustaces[i]['Prix'] == self.prix:
                    PagePrix.vin_poisson.append(PagePrix.prixVin_crustaces[i]['Vin'])

            for i in range(len(PagePrix.prixVin_poissonMer)):
                if PagePrix.prixVin_poissonMer[i]['Prix'] == self.prix:
                    PagePrix.vin_poisson.append(PagePrix.prixVin_poissonMer[i]['Vin'])

            for i in range(len(PagePrix.prixVin_poissonEauDouce)):
                if PagePrix.prixVin_poissonEauDouce[i]['Prix'] == self.prix:
                    PagePrix.vin_poisson.append(PagePrix.prixVin_poissonEauDouce[i]['Vin'])

        elif PlatPrincipalPage.typePP.get() == 2:
            for i in range(len(PagePrix.prixVin_coquillages)):
                if PagePrix.prixVin_coquillages[i]['Prix'] == self.prix:
                    PagePrix.vin_pates.append(PagePrix.prixVin_coquillages[i]['Vin'])

            for i in range(len(PagePrix.prixVin_crustaces)):
                if PagePrix.prixVin_crustaces[i]['Prix'] == self.prix:
                    PagePrix.vin_pates.append(PagePrix.prixVin_crustaces[i]['Vin'])

            for i in range(len(PagePrix.prixVin_poissonMer)):
                if PagePrix.prixVin_poissonMer[i]['Prix'] == self.prix:
                    PagePrix.vin_pates.append(PagePrix.prixVin_poissonMer[i]['Vin'])

            for i in range(len(PagePrix.prixVin_poissonEauDouce)):
                if PagePrix.prixVin_poissonEauDouce[i]['Prix'] == self.prix:
                    PagePrix.vin_pates.append(PagePrix.prixVin_poissonEauDouce[i]['Vin'])

            for i in range(len(PagePrix.prixVin_viandeBlanche)):
                if PagePrix.prixVin_viandeBlanche[i]['Prix'] == self.prix:
                    PagePrix.vin_pates.append(PagePrix.prixVin_viandeBlanche[i]['Vin'])

            for i in range(len(PagePrix.prixVin_viandeRouge)):
                if PagePrix.prixVin_viandeRouge[i]['Prix'] == self.prix:
                    PagePrix.vin_pates.append(PagePrix.prixVin_viandeRouge[i]['Vin'])

            for i in range(len(PagePrix.prixVin_gibier)):
                if PagePrix.prixVin_gibier[i]['Prix'] == self.prix:
                    PagePrix.vin_pates.append(PagePrix.prixVin_gibier[i]['Vin'])

            for i in range(len(PagePrix.prixVin_charcuterie)):
                if PagePrix.prixVin_charcuterie[i]['Prix'] == self.prix:
                    PagePrix.vin_pates.append(PagePrix.prixVin_charcuterie[i]['Vin'])

            for i in range(len(PagePrix.prixVin_vegetarien)):
                if PagePrix.prixVin_vegetarien[i]['Prix'] == self.prix:
                    PagePrix.vin_pates.append(PagePrix.prixVin_vegetarien[i]['Vin'])

            for i in range(len(PagePrix.prixVin_fromDur)):
                if PagePrix.prixVin_fromDur[i]['Prix'] == self.prix:
                    PagePrix.vin_pates.append(PagePrix.prixVin_fromDur[i]['Vin'])

            for i in range(len(PagePrix.prixVin_fromMol)):
                if PagePrix.prixVin_fromMol[i]['Prix'] == self.prix:
                    PagePrix.vin_pates.append(PagePrix.prixVin_fromMol[i]['Vin'])

        elif PlatPrincipalPage.typePP.get() == 4:
            for i in range(len(PagePrix.prixVin_vegetarien)):
                if PagePrix.prixVin_vegetarien[i]['Prix'] == self.prix:
                    PagePrix.vin_vegetarien.append(PagePrix.prixVin_vegetarien[i]['Vin'])

        PagePrix.vin_viande_set = set(PagePrix.vin_viande)
        PagePrix.vin_poisson_set = set(PagePrix.vin_poisson)
        PagePrix.vin_pates_set = set(PagePrix.vin_pates)
        PagePrix.vin_exotique_set = set(PagePrix.vin_exotique)
        PagePrix.vin_vegetarien_set = set(PagePrix.vin_vegetarien)

        self.newWindow = Toplevel(self.master)
        self.app = PageRecommandation(self.newWindow)

    def close_window(self):
        self.master.destroy()

class PageRecommandation:
    """
    Classe qui gère l'affichage de la variété de vin recommandée en fonction des choix effectués dans les étapes
    précédentes
    """
    def __init__(self, PagePrix):
        self.master = PagePrix
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
                                  command=self.conseil)
        createCloseButton = self.canvasRecom.create_window(750, 200, window=self.RecomButton)

        self.CaveButton = Button(self.frame, padx=38, bd=5, text="Notre cave à vin", bg='white',
                                 command=self.new_window)
        createCaveButton = self.canvasRecom.create_window(750, 500, window=self.CaveButton)

        self.closeButton = Button(self.frame, padx=38, bd=5, text="Revenir à la page précédente", bg='white',
                                  command=self.close_window)
        createCloseButton = self.canvasRecom.create_window(750, 550, window=self.closeButton)

    def conseil(self):
        self.RecomButton.destroy()

        var = StringVar()
        var.set("On vous conseille le cépage")
        self.label1 = Label(self.frame, textvariable=var, font=("Helvetica", 10, "bold"),
                            height=2, width=35, relief=FLAT).place(x=605, y=180)  # 180

        var2 = StringVar()

        PageRecommandation.vin = StringVar()
        self.label3 = Label(self.frame, textvariable=PageRecommandation.vin, fg="red", font=("Helvetica", 10, "bold"),
                            height=2, width=35, relief=FLAT).place(x=605, y=210)

        if PlatPrincipalPage.typePP.get() == 0 and PagePrix.choixDuPrix.get() == 0:
            if len(PagePrix.vin_viande_set) != 0:
                PageRecommandation.vin.set(random.choice(tuple(PagePrix.vin_viande_set)))

        elif PlatPrincipalPage.typePP.get() == 1 and PagePrix.choixDuPrix.get() == 0:
            if len(PagePrix.vin_poisson_set) != 0:
                PageRecommandation.vin.set(random.choice(tuple(PagePrix.vin_poisson_set)))

        elif PlatPrincipalPage.typePP.get() == 2 and PagePrix.choixDuPrix.get() == 0:
            if len(PagePrix.vin_pates_set) != 0:
                PageRecommandation.vin.set(random.choice(tuple(PagePrix.vin_pates_set)))

        elif PlatPrincipalPage.typePP.get() == 3 and PagePrix.choixDuPrix.get() == 0:
            if len(PagePrix.vin_exotique_set) != 0:
                PageRecommandation.vin.set(random.choice(tuple(PagePrix.vin_exotique_set)))


        elif PlatPrincipalPage.typePP.get() == 4 and PagePrix.choixDuPrix.get() == 0:
            if len(PagePrix.vin_vegetarien_set) != 0:
                PageRecommandation.vin.set(random.choice(tuple(PagePrix.vin_vegetarien_set)))

        elif PlatPrincipalPage.typePP.get() == 0 and PagePrix.choixDuPrix.get() == 1:
            PageRecommandation.vin.set(random.choice(PlatPrincipalPage.viande_rouge))

        elif PlatPrincipalPage.typePP.get() == 1 and PagePrix.choixDuPrix.get() == 1:
            PageRecommandation.vin.set(random.choice(PlatPrincipalPage.poisson_mer))

        elif PlatPrincipalPage.typePP.get() == 2 and PagePrix.choixDuPrix.get() == 1:
            PageRecommandation.vin.set(random.choice(PlatPrincipalPage.v_rouge)['Vin'])

        elif PlatPrincipalPage.typePP.get() == 3 and PagePrix.choixDuPrix.get() == 1:
            PageRecommandation.vin.set(random.choice(PlatPrincipalPage.exotique))

        elif PlatPrincipalPage.typePP.get() == 4 and PagePrix.choixDuPrix.get() == 1:
            PageRecommandation.vin.set(random.choice(PlatPrincipalPage.vegetarien))

        descr = list(prolog.query("description(Vin, Description)"))

        for i in range(len(descr)):
            descr[i]['Vin'] = descr[i]['Vin'].replace("_", " ").capitalize()

        var3 = StringVar()
        for i in range(len(descr)):
            if descr[i]['Vin'] == PageRecommandation.vin.get():
                var3.set(descr[i]['Description'])

        self.description = Label(self.frame, textvariable=var3, font=("Helvetica", 10, "bold"),
                                 height=12, width=37, relief=FLAT).place(x=602, y=238)

        if len(PagePrix.vin_viande_set) != 0 or len(PagePrix.vin_poisson_set) != 0 or \
                len(PagePrix.vin_pates_set) != 0 or len(PagePrix.vin_exotique_set) != 0 or \
                len(PagePrix.vin_vegetarien_set) != 0:
            self.label1
            self.label3
            self.description


        elif len(PagePrix.vin_viande_set) == 0 or len(PagePrix.vin_poisson_set) == 0 or \
                len(PagePrix.vin_pates_set) == 0 or len(PagePrix.vin_exotique_set) == 0 or \
                len(PagePrix.vin_vegetarien_set) == 0:

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
