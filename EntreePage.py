from tkinter import *
from tkinter.messagebox import *
from PIL import ImageTk, Image
from pyswip import *
import re
import unicodedata
import random

prolog = Prolog()
prolog.consult("base_de_connaisances.pl")

import warnings
warnings.filterwarnings("ignore")


class EntreePage:
    """
    Classe pour la création de la fenetre de dialogue de la catégorie Entrée et pour la géstion du choix
    du type d'entrée
    """
    def __init__(self, master):
        '''
        Définition de la structure de la fenetre de dialogue: frame, image, butons et texte
        '''
        self.master = master
        self.frame = Frame(self.master)
        self.master.title('DYONISO - Entrée')
        self.master.resizable(width="false", height="false")
        self.master.geometry("900x600+180+100")
        self.frame.pack()

        backgroundEntree = 'C:/Users/enricazabaino/Projet/Wine_Recommender/Prolog/entree.png'

        photoEntree = PhotoImage(file=backgroundEntree)
        self.canvasEntree = Canvas(self.frame, width=16000, height=2000)
        self.canvasEntree.imageList = []
        self.canvasEntree.pack()
        self.canvasEntree.create_image(0, 0, anchor="nw", image=photoEntree)
        self.canvasEntree.imageList.append(photoEntree)

        self.closeButton = Button(self.frame, padx=38, bd=5, text="Revenir au menu principal", bg='white',
                                  command=self.close_window)
        createCloseButton = self.canvasEntree.create_window(737, 500, window=self.closeButton)

        info = StringVar()
        self.label1 = Label(self.frame, textvariable=info, fg="red", font=("Helvetica", 10, "bold"),
                            height=2, width=35, relief=RAISED).place(x=595, y=50)
        info.set("Vous avez choisi la catégorie Entrée")

        '''
        Présentation de la 1ère question et des options de choix
        '''
        question1 = StringVar()
        self.question1Display = Label(self.frame, textvariable=question1, font=("Purisa", 10, "bold"),
                                      height=2, width=35, relief=FLAT).place(x=595, y=115)

        question1.set("Indiquer le type d'entrée que vous allez\n servire")

        EntreePage.typeEntree = IntVar()
        EntreePage.typeEntree.set(-1)
        self.optionCharcuterie = Radiobutton(self.frame, text="Charcuteries", variable=EntreePage.typeEntree, value=0,
                                             indicatoron=0,
                                             height=1, width=16, command=self.new_window)
        self.optionCharcuterie.place(relx=0.75, rely=0.30)
        self.optionCoquil = Radiobutton(self.frame, text="Coquillages", variable=EntreePage.typeEntree, value=1, indicatoron=0,
                                        height=1, width=16, command=self.new_window)
        self.optionCoquil.place(relx=0.75, rely=0.36)
        self.optionFromage = Radiobutton(self.frame, text="Fromages", variable=EntreePage.typeEntree, value=2, indicatoron=0,
                                         height=1, width=16, command=self.new_window)
        self.optionFromage.place(relx=0.75, rely=0.42)
        self.optionQuiche = Radiobutton(self.frame, text="Quiche", variable=EntreePage.typeEntree, value=3, indicatoron=0,
                                        height=1, width=16, command=self.new_window)
        self.optionQuiche.place(relx=0.75, rely=0.48)
        self.optionSalade = Radiobutton(self.frame, text="Salade", variable=EntreePage.typeEntree, value=4, indicatoron=0,
                                        height=1, width=16, command=self.new_window)
        self.optionSalade.place(relx=0.75, rely=0.54)
        self.optionSoupe = Radiobutton(self.frame, text="Soupe", variable=EntreePage.typeEntree, value=5, indicatoron=0,
                                       height=1, width=16, command=self.new_window)
        self.optionSoupe.place(relx=0.75, rely=0.60)

        '''
        Intérrogation de la base de connaissance pour récupérer la liste de tous les vins conseillés pour chaque 
        catégorie d'entrée ou d'ingrédient et mise en forme du texte
        '''
        EntreePage.charcuteriesVin = list(prolog.query("charcuterie(Vin)"))
        EntreePage.coquillagesVin = list(prolog.query("coquillages(Vin)"))
        EntreePage.crustacesVin = list(prolog.query("crustaces(Vin)"))
        EntreePage.poissonMerVin = list(prolog.query("poisson_mer(Vin)"))
        EntreePage.poissonEauDouceVin = list(prolog.query("poisson_eau_douce(Vin)"))
        EntreePage.fromagesAffinésVin = list(prolog.query("fromagedur(Vin)"))
        EntreePage.fromagesDouxVin = list(prolog.query("fromagemol(Vin)"))
        EntreePage.fromagesChevreVin = list(prolog.query("fromagechevre(Vin)"))
        EntreePage.viandeBlancheVin = list(prolog.query("viande_blanche_volaille(Vin)"))
        EntreePage.viandeRougeVin = list(prolog.query("viande_rouge(Vin)"))
        EntreePage.gibierVin = list(prolog.query("gibier(Vin)"))
        EntreePage.legumesVin = list(prolog.query("vegetarien(Vin)"))

        for i in range(len(EntreePage.charcuteriesVin)):
            EntreePage.charcuteriesVin[i]['Vin'] = EntreePage.charcuteriesVin[i]['Vin'].replace("_", " ").capitalize()
        for i in range(len(EntreePage.coquillagesVin)):
            EntreePage.coquillagesVin[i]['Vin'] = EntreePage.coquillagesVin[i]['Vin'].replace("_", " ").capitalize()
        for i in range(len(EntreePage.crustacesVin)):
            EntreePage.crustacesVin[i]['Vin'] = EntreePage.crustacesVin[i]['Vin'].replace("_", " ").capitalize()
        for i in range(len(EntreePage.poissonMerVin)):
            EntreePage.poissonMerVin[i]['Vin'] = EntreePage.poissonMerVin[i]['Vin'].replace("_", " ").capitalize()
        for i in range(len(EntreePage.poissonEauDouceVin)):
            EntreePage.poissonEauDouceVin[i]['Vin'] = EntreePage.poissonEauDouceVin[i]['Vin'].replace("_", " ").capitalize()
        for i in range(len(EntreePage.fromagesAffinésVin)):
            EntreePage.fromagesAffinésVin[i]['Vin'] = EntreePage.fromagesAffinésVin[i]['Vin'].replace("_", " ").capitalize()
        for i in range(len(EntreePage.fromagesDouxVin)):
            EntreePage.fromagesDouxVin[i]['Vin'] = EntreePage.fromagesDouxVin[i]['Vin'].replace("_", " ").capitalize()
        for i in range(len(EntreePage.fromagesChevreVin)):
            EntreePage.fromagesChevreVin[i]['Vin'] = EntreePage.fromagesChevreVin[i]['Vin'].replace("_", " ").capitalize()
        for i in range(len(EntreePage.viandeBlancheVin)):
            EntreePage.viandeBlancheVin[i]['Vin'] = EntreePage.viandeBlancheVin[i]['Vin'].replace("_", " ").capitalize()
        for i in range(len(EntreePage.viandeRougeVin)):
            EntreePage.viandeRougeVin[i]['Vin'] = EntreePage.viandeRougeVin[i]['Vin'].replace("_", " ").capitalize()
        for i in range(len(EntreePage.gibierVin)):
            EntreePage.gibierVin[i]['Vin'] = EntreePage.gibierVin[i]['Vin'].replace("_", " ").capitalize()
        for i in range(len(EntreePage.legumesVin)):
            EntreePage.legumesVin[i]['Vin'] = EntreePage.legumesVin[i]['Vin'].replace("_", " ").capitalize()


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
        self.app = Choix(self.newWindow)

class Choix:
    """
    Classe qui permet de gérérer les sous-options au sien de chaque catégorie d'entrée
    """
    def __init__(self, master):
        '''
        Réplique de la structure de la fenetre de dialogue définie dans la classe précédente
        '''
        self.master = master
        self.frame = Frame(self.master)
        self.master.title('DYONISO - Entrée')
        self.master.resizable(width="false", height="false")
        self.master.geometry("900x600+180+100")
        self.frame.pack()

        backgroundEntree = 'C:/Users/enricazabaino/Projet/Wine_Recommender/Prolog/entree.png'

        photoEntree = PhotoImage(file=backgroundEntree)
        self.canvasEntree = Canvas(self.frame, width=16000, height=2000)
        self.canvasEntree.imageList = []
        self.canvasEntree.pack()
        self.canvasEntree.create_image(0, 0, anchor="nw", image=photoEntree)
        self.canvasEntree.imageList.append(photoEntree)

        self.closeButton = Button(self.frame, padx=38, bd=5, text="Revenir à la page précédente", bg='white',
                                  command=self.close_window)
        createCloseButton = self.canvasEntree.create_window(737, 500, window=self.closeButton)

        infoType = StringVar()

        '''
        Affichage d'une récapitulation du choix efféctué par l'utilisateur
        '''
        if EntreePage.typeEntree.get() == 0:
            self.label = Label(self.frame, textvariable=infoType, fg="red", font=("Helvetica", 10, "bold"),
                               height=4, width=35, relief=RAISED, borderwidth=5, highlightcolor="white").place(x=595,
                                                                                                               y=50)
            infoType.set("Vous avez choisi la catégorie Entrée\n\n Vous avez choisi l'option 'Charcuteries'")

        elif EntreePage.typeEntree.get() == 1:
            self.label = Label(self.frame, textvariable=infoType, fg="red", font=("Helvetica", 10, "bold"),
                               height=4, width=35, relief=RAISED, borderwidth=5, highlightcolor="green").place(x=595,
                                                                                                               y=50)
            infoType.set("Vous avez choisi la catégorie Entrée\n\n Vous avez choisi l'option 'Coquillages'")

        elif EntreePage.typeEntree.get() == 2:
            self.label = Label(self.frame, textvariable=infoType, fg="red", font=("Helvetica", 10, "bold"),
                               height=4, width=35, relief=RAISED, borderwidth=5, highlightcolor="green").place(x=595,
                                                                                                               y=50)
            infoType.set("Vous avez choisi la catégorie Entrée\n\n Vous avez choisi l'option 'Fromages'")

        elif EntreePage.typeEntree.get() == 3:
            self.label = Label(self.frame, textvariable=infoType, fg="red", font=("Helvetica", 10, "bold"),
                               height=4, width=35, relief=RAISED, borderwidth=5, highlightcolor="green").place(x=595,
                                                                                                               y=50)
            infoType.set("Vous avez choisi la catégorie Entrée\n\n Vous avez choisi l'option 'Quiche'")

        elif EntreePage.typeEntree.get() == 4:
            self.label = Label(self.frame, textvariable=infoType, fg="red", font=("Helvetica", 10, "bold"),
                               height=4, width=35, relief=RAISED, borderwidth=5, highlightcolor="green").place(x=595,
                                                                                                               y=50)
            infoType.set("Vous avez choisi la catégorie Entrée\n\n Vous avez choisi l'option 'Salade'")

        elif EntreePage.typeEntree.get() == 5:
            self.label = Label(self.frame, textvariable=infoType, fg="red", font=("Helvetica", 10, "bold"),
                               height=4, width=35, relief=RAISED, borderwidth=5, highlightcolor="green").place(x=595,
                                                                                                               y=50)
            infoType.set("Vous avez choisi la catégorie Entrée\n\n Vous avez choisi l'option 'Soupe'")

        '''
        Présentation de la question relative au choix de prix si la catégorie d'entrée choisie par l'utilisateur
        est 'charcuterie' ou 'coquillages'.
        Présentation de la question relative à l'ingrédient si la catégorie d'entrée choisie par l'utilisateur
        est 'fromages', 'quiche', 'salade' ou 'soupe' .
        '''
        if EntreePage.typeEntree.get() == 0 or EntreePage.typeEntree.get() == 1:
            question2 = StringVar()
            self.question2Display = Label(self.frame, textvariable=question2, font=("Helvetica", 10, "bold"),
                                          height=6, width=37, relief=FLAT, anchor="e").place(x=595, y=122)
            question2.set("Est-ce que vous souhaitez indiquer\n combien vous voulez dépénser au maximum?")

            EntreePage.choixDuPrixEntree = IntVar()
            EntreePage.choixDuPrixEntree.set(-1)
            self.oui = Radiobutton(self.frame, text="Oui", variable=EntreePage.choixDuPrixEntree, value=0,
                                   command=self.choix_prixEntree)
            self.oui.place(relx=0.75, rely=0.37)
            self.non = Radiobutton(self.frame, text="Non", variable=EntreePage.choixDuPrixEntree, value=1,
                                   command=self.choix_prixEntree)
            self.non.place(relx=0.75, rely=0.43)

        if EntreePage.typeEntree.get() == 2:
            questionTypeFrom = StringVar()
            self.questionTypeFromDisplay = Label(self.frame, textvariable=questionTypeFrom,
                                                 font=("Helvetica", 10, "bold"),
                                                 height=8, width=37, relief=FLAT).place(x=585, y=122)
            questionTypeFrom.set("Indiquer le type de fromage que\n vous allez servir")

            EntreePage.choixFromage = IntVar()
            EntreePage.choixFromage.set(-1)
            self.affinés = Radiobutton(self.frame, text="Fromages Affinés", variable=EntreePage.choixFromage, value=0,
                                       command=self.choix_fromage)
            self.affinés.place(relx=0.70, rely=0.37)
            self.doux = Radiobutton(self.frame, text="Fromages Doux", variable=EntreePage.choixFromage, value=1,
                                    command=self.choix_fromage)
            self.doux.place(relx=0.70, rely=0.43)
            self.chevre = Radiobutton(self.frame, text="Fromages de Chèvre ou Brebis", variable=EntreePage.choixFromage,
                                      value=2, command=self.choix_fromage)
            self.chevre.place(relx=0.70, rely=0.48)

        elif EntreePage.typeEntree.get() == 3 or EntreePage.typeEntree.get() == 4 or EntreePage.typeEntree.get() == 5:
            questionIngredient = StringVar()
            self.questionIngredientDisplay = Label(self.frame, textvariable=questionIngredient,
                                                   font=("Helvetica", 10, "bold"),
                                                   height=8, width=37, relief=FLAT).place(x=585, y=122)
            questionIngredient.set("Indiquer quel est l'ingrédient principal")

            EntreePage.choixIngredient = IntVar()
            EntreePage.choixIngredient.set(-1)
            self.fromage = Radiobutton(self.frame, text="Fromage", variable=EntreePage.choixIngredient, value=0,
                                       command=self.choix_IngrFromage)
            self.fromage.place(relx=0.70, rely=0.37)
            self.poisson = Radiobutton(self.frame, text="Fruits de mer ou Poisson", variable=EntreePage.choixIngredient,
                                       value=1, command=self.choix_IngrPoisson)
            self.poisson.place(relx=0.70, rely=0.42)
            self.viande = Radiobutton(self.frame, text="Viande", variable=EntreePage.choixIngredient,
                                      value=2, command=self.choix_IngrViande)
            self.viande.place(relx=0.70, rely=0.47)
            self.legumes = Radiobutton(self.frame, text="Légumes", variable=EntreePage.choixIngredient,
                                       value=3, command=self.choix_legumes)
            self.legumes.place(relx=0.70, rely=0.52)

    def choix_IngrFromage(self):
        '''
         Fonction qui gère les sous-options dans le cas où l'utilisateur choisisse l'ingrédient 'fromage'
         '''
        self.fromage.place_forget()
        self.poisson.place_forget()
        self.viande.place_forget()
        self.legumes.place_forget()

        questionTypeFrom = StringVar()
        self.questionTypeFromDisplay = Label(self.frame, textvariable=questionTypeFrom, font=("Helvetica", 10, "bold"),
                                             height=8, width=37, relief=FLAT).place(x=585, y=122)
        questionTypeFrom.set("Indiquer le type de fromage que\n vous allez utiliser")

        EntreePage.choixIngredientFromage = IntVar()
        EntreePage.choixIngredientFromage.set(-1)
        self.affinés = Radiobutton(self.frame, text="Fromages Affinés", variable=EntreePage.choixIngredientFromage,
                                   value=0, command=self.choix_fromage)
        self.affinés.place(relx=0.70, rely=0.37)
        self.doux = Radiobutton(self.frame, text="Fromages Doux", variable=EntreePage.choixIngredientFromage, value=1,
                                command=self.choix_fromage)
        self.doux.place(relx=0.70, rely=0.43)
        self.chevre = Radiobutton(self.frame, text="Fromages de Chèvre ou Brebis",
                                  variable=EntreePage.choixIngredientFromage,
                                  value=2, command=self.choix_fromage)
        self.chevre.place(relx=0.70, rely=0.48)

    def choix_fromage(self):
        '''
        Fonction qui gère la question sur le prix et des options de choix lorsque l'ingrédient choisi est 'fromage'
        '''
        self.affinés.place_forget()
        self.doux.place_forget()
        self.chevre.place_forget()

        question2 = StringVar()
        self.question2Display = Label(self.frame, textvariable=question2, font=("Helvetica", 10, "bold"),
                                      height=6, width=37, relief=FLAT, anchor="e").place(x=595, y=122)
        question2.set("Est-ce que vous souhaitez indiquer\n combien vous voulez dépénser au maximum?")

        EntreePage.choixDuPrixEntree = IntVar()
        EntreePage.choixDuPrixEntree.set(-1)
        self.oui = Radiobutton(self.frame, text="Oui", variable=EntreePage.choixDuPrixEntree, value=0,
                               command=self.choix_prixEntree)
        self.oui.place(relx=0.75, rely=0.37)
        self.non = Radiobutton(self.frame, text="Non", variable=EntreePage.choixDuPrixEntree, value=1,
                               command=self.choix_prixEntree)
        self.non.place(relx=0.75, rely=0.43)

    def choix_IngrPoisson(self):
        '''
        Fonction qui gère les sous-options dans le cas où l'utilisateur choisisse l'ingrédient 'poisson'
        '''
        self.fromage.place_forget()
        self.poisson.place_forget()
        self.viande.place_forget()
        self.legumes.place_forget()

        questionTypePoisson = StringVar()
        self.questionTypePoissonDisplay = Label(self.frame, textvariable=questionTypePoisson,
                                                font=("Helvetica", 10, "bold"),
                                                height=8, width=36, relief=FLAT).place(x=580, y=122)
        questionTypePoisson.set("Indiquer si vous allez utiliser")

        EntreePage.choixIngredientPoisson = IntVar()
        EntreePage.choixIngredientPoisson.set(-1)
        self.mer = Radiobutton(self.frame, text="Poisson de mer/Crustaces", variable=EntreePage.choixIngredientPoisson,
                               value=0, command=self.choix_poisson)
        self.mer.place(relx=0.68, rely=0.37)
        self.buttonDescription1 = Button(self.frame, padx=38, bd=0, height=1, width=25,
                                         text="[Ex. sardine,thon,poulpe,crevettes,crabe, etc.]")
        createbuttonDescription1 = self.canvasEntree.create_window(740, 260, window=self.buttonDescription1)

        self.eauDouce = Radiobutton(self.frame, text="Poisson d'eau douce", variable=EntreePage.choixIngredientPoisson,
                                    value=1, command=self.choix_poisson)
        self.eauDouce.place(relx=0.68, rely=0.50)
        self.buttonDescription2 = Button(self.frame, padx=38, bd=0, height=1, width=12, text="[Ex. saumone,truit, etc.]")
        createbuttonDescription2 = self.canvasEntree.create_window(685, 335, window=self.buttonDescription2)

    def choix_poisson(self):
        '''
        Fonction qui gère la question sur le prix et des options de choix lorsque l'ingrédient choisi est 'poisson'
        '''
        self.mer.place_forget()
        self.eauDouce.place_forget()
        self.buttonDescription1.destroy()
        self.buttonDescription2.destroy()

        question2 = StringVar()
        self.question2Display = Label(self.frame, textvariable=question2, font=("Helvetica", 10, "bold"),
                                      height=6, width=37, relief=FLAT, anchor="e").place(x=595, y=122)
        question2.set("Est-ce que vous souhaitez indiquer\n combien vous voulez dépénser au maximum?")

        EntreePage.choixDuPrixEntree = IntVar()
        EntreePage.choixDuPrixEntree.set(-1)
        self.oui = Radiobutton(self.frame, text="Oui", variable=EntreePage.choixDuPrixEntree, value=0,
                               command=self.choix_prixEntree)
        self.oui.place(relx=0.75, rely=0.37)
        self.non = Radiobutton(self.frame, text="Non", variable=EntreePage.choixDuPrixEntree, value=1,
                               command=self.choix_prixEntree)
        self.non.place(relx=0.75, rely=0.43)

    def choix_IngrViande(self):
        '''
        Fonction qui gère les sous-options dans le cas où l'utilisateur choisisse l'ingrédient 'viande'
        '''
        self.fromage.place_forget()
        self.poisson.place_forget()
        self.viande.place_forget()
        self.legumes.place_forget()

        questionTypeViande = StringVar()
        self.questionTypeViandeDisplay = Label(self.frame, textvariable=questionTypeViande,
                                               font=("Helvetica", 10, "bold"),
                                               height=8, width=36, relief=FLAT).place(x=580, y=122)
        questionTypeViande.set("Indiquer si vous allez utiliser")

        EntreePage.choixIngredientViande = IntVar()
        EntreePage.choixIngredientViande.set(-1)
        self.blanche = Radiobutton(self.frame, text="Viande Blanche ou Volaille",
                                   variable=EntreePage.choixIngredientViande, value=0,
                                   command=self.choix_viande)
        self.blanche.place(relx=0.68, rely=0.37)
        self.buttonDescription1 = Button(self.frame, padx=38, bd=0, height=1, width=25,
                                         text="[Ex. cochon,poulet,dinde,canard, etc.]")
        createbuttonDescription1 = self.canvasEntree.create_window(733, 260, window=self.buttonDescription1)

        self.rouge = Radiobutton(self.frame, text="Viande Rouge", variable=EntreePage.choixIngredientViande, value=1,
                                 command=self.choix_viande)
        self.rouge.place(relx=0.68, rely=0.48)
        self.buttonDescription2 = Button(self.frame, padx=38, bd=0, height=1, width=12,
                                         text="[Ex. boeuf, veau,agneau, etc.]")
        createbuttonDescription2 = self.canvasEntree.create_window(713, 325, window=self.buttonDescription2)

        self.gibier = Radiobutton(self.frame, text="Gibier", variable=EntreePage.choixIngredientViande, value=2,
                                  command=self.choix_viande)
        self.gibier.place(relx=0.68, rely=0.59)
        self.buttonDescription3 = Button(self.frame, padx=38, bd=0, height=1, width=12,
                                         text="[Ex. sanglier,cerf, etc.]")
        createbuttonDescription3 = self.canvasEntree.create_window(691, 385, window=self.buttonDescription3)

    def choix_viande(self):
        '''
        Fonction qui gère la question sur le prix et des options de choix lorsque l'ingrédient choisi est 'viande'
        '''
        self.blanche.place_forget()
        self.rouge.place_forget()
        self.gibier.place_forget()
        self.buttonDescription1.destroy()
        self.buttonDescription2.destroy()
        self.buttonDescription3.destroy()

        question2 = StringVar()
        self.question2Display = Label(self.frame, textvariable=question2, font=("Helvetica", 10, "bold"),
                                      height=6, width=37, relief=FLAT, anchor="e").place(x=595, y=122)
        question2.set("Est-ce que vous souhaitez indiquer\n combien vous voulez dépénser au maximum?")

        EntreePage.choixDuPrixEntree = IntVar()
        EntreePage.choixDuPrixEntree.set(-1)
        self.oui = Radiobutton(self.frame, text="Oui", variable=EntreePage.choixDuPrixEntree, value=0,
                               command=self.choix_prixEntree)
        self.oui.place(relx=0.75, rely=0.37)
        self.non = Radiobutton(self.frame, text="Non", variable=EntreePage.choixDuPrixEntree, value=1,
                               command=self.choix_prixEntree)
        self.non.place(relx=0.75, rely=0.43)

    def choix_legumes(self):
        '''
        Fonction qui gère la question sur le prix et des options de choix lorsque l'ingrédient choisi est 'légumes'
        '''
        self.fromage.place_forget()
        self.poisson.place_forget()
        self.viande.place_forget()
        self.legumes.place_forget()

        question2 = StringVar()
        self.question2Display = Label(self.frame, textvariable=question2, font=("Helvetica", 10, "bold"),
                                      height=6, width=37, relief=FLAT, anchor="e").place(x=595, y=122)
        question2.set("Est-ce que vous souhaitez indiquer\n combien vous voulez dépénser au maximum?")

        EntreePage.choixDuPrixEntree = IntVar()
        EntreePage.choixDuPrixEntree.set(-1)
        self.oui = Radiobutton(self.frame, text="Oui", variable=EntreePage.choixDuPrixEntree, value=0,
                               command=self.choix_prixEntree)
        self.oui.place(relx=0.75, rely=0.37)
        self.non = Radiobutton(self.frame, text="Non", variable=EntreePage.choixDuPrixEntree, value=1,
                               command=self.choix_prixEntree)
        self.non.place(relx=0.75, rely=0.43)

    def choix_prixEntree(self):
        '''
        Fonction qui gère les cas où l'utilisateur choisisse d'indiquer ou de ne pas indiquer un prix maximum
        '''
        self.e = StringVar()
        if EntreePage.choixDuPrixEntree.get() == 0:
            entreePrix = Entry(self.frame, textvariable=self.e, bg='bisque', fg='maroon').place(relx=0.82, rely=0.37)
            self.validerButton = Button(self.frame, text="Valider",
                                        command=self.validerEntree).place(x=708, y=300)

        elif EntreePage.choixDuPrixEntree.get() == 1:
            self.newWindow = Toplevel(self.master)
            self.app = PageRecommandation(self.newWindow)

    def validerEntree(self):
        '''
        Fonction qui récupère les vins contenus dans la base de connaissance dont le prix corréspond au
        choix de l'utilisateur
        return:
            un set de vins
        '''
        EntreePage.prixVin_charcuteries = list(prolog.query("prix_charcuterie(Vin, Prix)"))
        EntreePage.prixVin_coquillages = list(prolog.query("prix_coquillages(Vin, Prix)"))
        EntreePage.prixVin_poissonMer = list(prolog.query("prix_poisson_mer(Vin, Prix)"))
        EntreePage.prixVin_poissonEauDouce = list(prolog.query("prix_poisson_eau_douce(Vin, Prix)"))
        EntreePage.prixVin_fromagesAffinés = list(prolog.query("prix_fromages_affines(Vin, Prix)"))
        EntreePage.prixVin_fromagesDoux = list(prolog.query("prix_fromages_doux(Vin, Prix)"))
        EntreePage.prixVin_fromagesChevre = list(prolog.query("prix_fromages_chevre(Vin, Prix)"))
        EntreePage.prixVin_viandeBlanche = list(prolog.query("prix_viande_blanche(Vin, Prix)"))
        EntreePage.prixVin_viandeRouge = list(prolog.query("prix_viande_rouge(Vin, Prix)"))
        EntreePage.prixVin_gibier = list(prolog.query("prix_gibier(Vin, Prix)"))
        EntreePage.prixVin_legumes = list(prolog.query("prix_vegetarien(Vin, Prix)"))

        for i in range(len(EntreePage.prixVin_charcuteries)):
            EntreePage.prixVin_charcuteries[i]['Vin'] = EntreePage.prixVin_charcuteries[i]['Vin'].replace("_",
                                                                                                          " ").capitalize()
        for i in range(len(EntreePage.prixVin_coquillages)):
            EntreePage.prixVin_coquillages[i]['Vin'] = EntreePage.prixVin_coquillages[i]['Vin'].replace("_",
                                                                                                        " ").capitalize()
        for i in range(len(EntreePage.prixVin_poissonMer)):
            EntreePage.prixVin_poissonMer[i]['Vin'] = EntreePage.prixVin_poissonMer[i]['Vin'].replace("_",
                                                                                                      " ").capitalize()
        for i in range(len(EntreePage.prixVin_poissonEauDouce)):
            EntreePage.prixVin_poissonEauDouce[i]['Vin'] = EntreePage.prixVin_poissonEauDouce[i]['Vin'].replace("_",
                                                                                                                " ").capitalize()
        for i in range(len(EntreePage.prixVin_fromagesAffinés)):
            EntreePage.prixVin_fromagesAffinés[i]['Vin'] = EntreePage.prixVin_fromagesAffinés[i]['Vin'].replace("_",
                                                                                                                " ").capitalize()
        for i in range(len(EntreePage.prixVin_fromagesDoux)):
            EntreePage.prixVin_fromagesDoux[i]['Vin'] = EntreePage.prixVin_fromagesDoux[i]['Vin'].replace("_",
                                                                                                          " ").capitalize()
        for i in range(len(EntreePage.prixVin_fromagesChevre)):
            EntreePage.prixVin_fromagesChevre[i]['Vin'] = EntreePage.prixVin_fromagesChevre[i]['Vin'].replace("_",
                                                                                                              " ").capitalize()
        for i in range(len(EntreePage.prixVin_viandeBlanche)):
            EntreePage.prixVin_viandeBlanche[i]['Vin'] = EntreePage.prixVin_viandeBlanche[i]['Vin'].replace("_",
                                                                                                            " ").capitalize()
        for i in range(len(EntreePage.prixVin_viandeRouge)):
            EntreePage.prixVin_viandeRouge[i]['Vin'] = EntreePage.prixVin_viandeRouge[i]['Vin'].replace("_",
                                                                                                        " ").capitalize()
        for i in range(len(EntreePage.prixVin_gibier)):
            EntreePage.prixVin_gibier[i]['Vin'] = EntreePage.prixVin_gibier[i]['Vin'].replace("_", " ").capitalize()
        for i in range(len(EntreePage.prixVin_legumes)):
            EntreePage.prixVin_legumes[i]['Vin'] = EntreePage.prixVin_legumes[i]['Vin'].replace("_", " ").capitalize()

        self.prix = int(self.e.get())

        EntreePage.vin_charcuteries = []
        EntreePage.vin_coquillages = []
        EntreePage.vin_fromagesAffinés = []
        EntreePage.vin_fromagesDoux = []
        EntreePage.vin_fromagesChevre = []
        EntreePage.vin_poissonMer = []
        EntreePage.vin_poissonEauDouce = []
        EntreePage.vin_viandeBlanche = []
        EntreePage.vin_viandeRouge = []
        EntreePage.vin_gibier = []
        EntreePage.vin_legumes = []

        if EntreePage.typeEntree.get() == 0:
            for i in range(len(EntreePage.prixVin_charcuteries)):
                if EntreePage.prixVin_charcuteries[i]['Prix'] == self.prix:
                    EntreePage.vin_charcuteries.append(EntreePage.prixVin_charcuteries[i]['Vin'])

        elif EntreePage.typeEntree.get() == 1:
            for i in range(len(EntreePage.prixVin_coquillages)):
                if EntreePage.prixVin_coquillages[i]['Prix'] == self.prix:
                    EntreePage.vin_coquillages.append(EntreePage.prixVin_coquillages[i]['Vin'])

        elif EntreePage.typeEntree.get() == 2 and EntreePage.choixFromage.get() == 0:
            for i in range(len(EntreePage.prixVin_fromagesAffinés)):
                if EntreePage.prixVin_fromagesAffinés[i]['Prix'] == self.prix:
                    EntreePage.vin_fromagesAffinés.append(EntreePage.prixVin_fromagesAffinés[i]['Vin'])

        elif EntreePage.typeEntree.get() == 2 and EntreePage.choixFromage.get() == 1:
            for i in range(len(EntreePage.prixVin_fromagesDoux)):
                if EntreePage.prixVin_fromagesDoux[i]['Prix'] == self.prix:
                    EntreePage.vin_fromagesDoux.append(EntreePage.prixVin_fromagesDoux[i]['Vin'])

        elif EntreePage.typeEntree.get() == 2 and EntreePage.choixFromage.get() == 2:
            for i in range(len(EntreePage.prixVin_fromagesChevre)):
                if EntreePage.prixVin_fromagesChevre[i]['Prix'] == self.prix:
                    EntreePage.vin_fromagesChevre.append(EntreePage.prixVin_fromagesChevre[i]['Vin'])


        elif (
                EntreePage.typeEntree.get() == 3 or EntreePage.typeEntree.get() == 4 or EntreePage.typeEntree.get() == 5) and \
                EntreePage.choixIngredient.get() == 0 and EntreePage.choixIngredientFromage.get() == 0:
            for i in range(len(EntreePage.prixVin_fromagesAffinés)):
                if EntreePage.prixVin_fromagesAffinés[i]['Prix'] == self.prix:
                    EntreePage.vin_fromagesAffinés.append(EntreePage.prixVin_fromagesAffinés[i]['Vin'])


        elif (
                EntreePage.typeEntree.get() == 3 or EntreePage.typeEntree.get() == 4 or EntreePage.typeEntree.get() == 5) and \
                EntreePage.choixIngredient.get() == 0 and EntreePage.choixIngredientFromage.get() == 1:
            for i in range(len(EntreePage.prixVin_fromagesDoux)):
                if EntreePage.prixVin_fromagesDoux[i]['Prix'] == self.prix:
                    EntreePage.vin_fromagesDoux.append(EntreePage.prixVin_fromagesDoux[i]['Vin'])

        elif (
                EntreePage.typeEntree.get() == 3 or EntreePage.typeEntree.get() == 4 or EntreePage.typeEntree.get() == 5) and \
                EntreePage.choixIngredient.get() == 0 and EntreePage.choixIngredientFromage.get() == 2:
            for i in range(len(EntreePage.prixVin_fromagesChevre)):
                if EntreePage.prixVin_fromagesChevre[i]['Prix'] == self.prix:
                    EntreePage.vin_fromagesChevre.append(EntreePage.prixVin_fromagesChevre[i]['Vin'])


        elif (
                EntreePage.typeEntree.get() == 3 or EntreePage.typeEntree.get() == 4 or EntreePage.typeEntree.get() == 5) and \
                EntreePage.choixIngredient.get() == 1 and EntreePage.choixIngredientPoisson.get() == 0:
            for i in range(len(EntreePage.prixVin_poissonMer)):
                if EntreePage.prixVin_poissonMer[i]['Prix'] == self.prix:
                    EntreePage.vin_poissonMer.append(EntreePage.prixVin_poissonMer[i]['Vin'])

        elif (
                EntreePage.typeEntree.get() == 3 or EntreePage.typeEntree.get() == 4 or EntreePage.typeEntree.get() == 5) and \
                EntreePage.choixIngredient.get() == 1 and EntreePage.choixIngredientPoisson.get() == 1:
            for i in range(len(EntreePage.prixVin_poissonEauDouce)):
                if EntreePage.prixVin_poissonEauDouce[i]['Prix'] == self.prix:
                    EntreePage.vin_poissonEauDouce.append(EntreePage.prixVin_poissonEauDouce[i]['Vin'])

        elif (
                EntreePage.typeEntree.get() == 3 or EntreePage.typeEntree.get() == 4 or EntreePage.typeEntree.get() == 5) and \
                EntreePage.choixIngredient.get() == 2 and EntreePage.choixIngredientViande.get() == 0:
            for i in range(len(EntreePage.prixVin_viandeBlanche)):
                if EntreePage.prixVin_viandeBlanche[i]['Prix'] == self.prix:
                    EntreePage.vin_viandeBlanche.append(EntreePage.prixVin_viandeBlanche[i]['Vin'])

        elif (
                EntreePage.typeEntree.get() == 3 or EntreePage.typeEntree.get() == 4 or EntreePage.typeEntree.get() == 5) and \
                EntreePage.choixIngredient.get() == 2 and EntreePage.choixIngredientViande.get() == 1:
            for i in range(len(EntreePage.prixVin_viandeRouge)):
                if EntreePage.prixVin_viandeRouge[i]['Prix'] == self.prix:
                    EntreePage.vin_viandeRouge.append(EntreePage.prixVin_viandeRouge[i]['Vin'])

        elif (
                EntreePage.typeEntree.get() == 3 or EntreePage.typeEntree.get() == 4 or EntreePage.typeEntree.get() == 5) and \
                EntreePage.choixIngredient.get() == 2 and EntreePage.choixIngredientViande.get() == 2:
            for i in range(len(EntreePage.prixVin_gibier)):
                if EntreePage.prixVin_gibier[i]['Prix'] == self.prix:
                    EntreePage.vin_gibier.append(EntreePage.prixVin_gibier[i]['Vin'])

        elif (
                EntreePage.typeEntree.get() == 3 or EntreePage.typeEntree.get() == 4 or EntreePage.typeEntree.get() == 5) and \
                EntreePage.choixIngredient.get() == 3:
            for i in range(len(EntreePage.prixVin_legumes)):
                if EntreePage.prixVin_legumes[i]['Prix'] == self.prix:
                    EntreePage.vin_legumes.append(EntreePage.prixVin_legumes[i]['Vin'])

        EntreePage.vin_charcuteries_set = set(EntreePage.vin_charcuteries)
        EntreePage.vin_coquillages_set = set(EntreePage.vin_coquillages)
        EntreePage.vin_fromagesAffinés_set = set(EntreePage.vin_fromagesAffinés)
        EntreePage.vin_fromagesDoux_set = set(EntreePage.vin_fromagesDoux)
        EntreePage.vin_fromagesChevre_set = set(EntreePage.vin_fromagesChevre)
        EntreePage.vin_poissonMer_set = set(EntreePage.vin_poissonMer)
        EntreePage.vin_poissonEauDouce_set = set(EntreePage.vin_poissonEauDouce)
        EntreePage.vin_viandeBlanche_set = set(EntreePage.vin_viandeBlanche)
        EntreePage.vin_viandeRouge_set = set(EntreePage.vin_viandeRouge)
        EntreePage.vin_gibier_set = set(EntreePage.vin_gibier)
        EntreePage.vin_legumes_set = set(EntreePage.vin_legumes)

        self.newWindow = Toplevel(self.master)
        self.app = PageRecommandation(self.newWindow)

    def close_window(self):
        self.master.destroy()


class PageRecommandation:
    """
    Classe qui gère l'affichage de la variété de vin recommandée en fonction des choix effectués dans les étapes
    précédentes
    """
    def __init__(self, EntreePage):
        self.master = EntreePage
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
                                  command=self.conseilEntree)
        createCloseButton = self.canvasRecom.create_window(750, 200, window=self.RecomButton)

        self.CaveButton = Button(self.frame, padx=38, bd=5, text="Notre cave à vin", bg='white',
                                 command=self.new_window)
        createCaveButton = self.canvasRecom.create_window(750, 500, window=self.CaveButton)

        self.closeButton = Button(self.frame, padx=38, bd=5, text="Revenir à la page précédente", bg='white',
                                  command=self.close_window)
        createCloseButton = self.canvasRecom.create_window(750, 550, window=self.closeButton)

    def conseilEntree(self):
        self.RecomButton.destroy()

        var = StringVar()
        var.set("On vous conseille le cépage")
        self.label1 = Label(self.frame, textvariable=var, font=("Helvetica", 10, "bold"),
                            height=2, width=35, relief=FLAT).place(x=605, y=180)  # 180

        var2 = StringVar()

        PageRecommandation.vin = StringVar()
        self.label3 = Label(self.frame, textvariable=PageRecommandation.vin, fg="red", font=("Helvetica", 10, "bold"),
                            height=2, width=35, relief=FLAT).place(x=605, y=210)

        if EntreePage.typeEntree.get() == 0 and EntreePage.choixDuPrixEntree.get() == 0:
            if len(EntreePage.vin_charcuteries_set) != 0:
                PageRecommandation.vin.set(random.choice(tuple(EntreePage.vin_charcuteries_set)))

        elif EntreePage.typeEntree.get() == 1 and EntreePage.choixDuPrixEntree.get() == 0:
            if len(EntreePage.vin_coquillages_set) != 0:
                PageRecommandation.vin.set(random.choice(tuple(EntreePage.vin_coquillages_set)))

        elif EntreePage.typeEntree.get() == 2 and EntreePage.choixFromage.get() == 0 and \
                EntreePage.choixDuPrixEntree.get() == 0:
            if len(EntreePage.vin_fromagesAffinés_set) != 0:
                PageRecommandation.vin.set(random.choice(tuple(EntreePage.vin_fromagesAffinés_set)))

        elif EntreePage.typeEntree.get() == 2 and EntreePage.choixFromage.get() == 1 and \
                EntreePage.choixDuPrixEntree.get() == 0:
            if len(EntreePage.vin_fromagesDoux_set) != 0:
                PageRecommandation.vin.set(random.choice(tuple(EntreePage.vin_fromagesDoux_set)))


        elif EntreePage.typeEntree.get() == 2 and EntreePage.choixFromage.get() == 2 and \
                EntreePage.choixDuPrixEntree.get() == 0:
            if len(EntreePage.vin_fromagesChevre_set) != 0:
                PageRecommandation.vin.set(random.choice(tuple(EntreePage.vin_fromagesChevre_set)))

        elif (
                EntreePage.typeEntree.get() == 3 or EntreePage.typeEntree.get() == 4 or \
                EntreePage.typeEntree.get() == 5) and \
                EntreePage.choixIngredient.get() == 0 and EntreePage.choixIngredientFromage.get() == 0 and\
                EntreePage.choixDuPrixEntree.get() == 0:
            if len(EntreePage.vin_fromagesAffinés_set) != 0:
                PageRecommandation.vin.set(random.choice(tuple(EntreePage.vin_fromagesAffinés_set)))

        elif (
                EntreePage.typeEntree.get() == 3 or EntreePage.typeEntree.get() == 4 or \
                EntreePage.typeEntree.get() == 5) and EntreePage.choixIngredient.get() == 0 and \
                EntreePage.choixIngredientFromage.get() == 1 and EntreePage.choixDuPrixEntree.get() == 0:
            if len(EntreePage.vin_fromagesDoux_set) != 0:
                PageRecommandation.vin.set(random.choice(tuple(EntreePage.vin_fromagesDoux_set)))

        elif (
                EntreePage.typeEntree.get() == 3 or EntreePage.typeEntree.get() == 4 or \
                EntreePage.typeEntree.get() == 5) and EntreePage.choixIngredient.get() == 0 and \
                EntreePage.choixIngredientFromage.get() == 2 and EntreePage.choixDuPrixEntree.get() == 0:
            if len(EntreePage.vin_fromagesChevre_set) != 0:
                PageRecommandation.vin.set(random.choice(tuple(EntreePage.vin_fromagesChevre_set)))

        elif (
                EntreePage.typeEntree.get() == 3 or EntreePage.typeEntree.get() == 4 or \
                EntreePage.typeEntree.get() == 5) and EntreePage.choixIngredient.get() == 1 and \
                EntreePage.choixIngredientPoisson.get() == 0 and EntreePage.choixDuPrixEntree.get() == 0:
            if len(EntreePage.vin_poissonMer_set) != 0:
                PageRecommandation.vin.set(random.choice(tuple(EntreePage.vin_poissonMer_set)))

        elif (
                EntreePage.typeEntree.get() == 3 or EntreePage.typeEntree.get() == 4 or \
                EntreePage.typeEntree.get() == 5) and EntreePage.choixIngredient.get() == 1 and \
                EntreePage.choixIngredientPoisson.get() == 1 and EntreePage.choixDuPrixEntree.get() == 0:
            if len(EntreePage.vin_poissonEauDouce_set) != 0:
                PageRecommandation.vin.set(random.choice(tuple(EntreePage.vin_poissonEauDouce_set)))

        elif (
                EntreePage.typeEntree.get() == 3 or EntreePage.typeEntree.get() == 4 or \
                EntreePage.typeEntree.get() == 5) and EntreePage.choixIngredient.get() == 2 and \
                EntreePage.choixIngredientViande.get() == 0 and EntreePage.choixDuPrixEntree.get() == 0:
            if len(EntreePage.vin_viandeBlanche_set) != 0:
                PageRecommandation.vin.set(random.choice(tuple(EntreePage.vin_viandeBlanche_set)))

        elif (
                EntreePage.typeEntree.get() == 3 or EntreePage.typeEntree.get() == 4 or \
                EntreePage.typeEntree.get() == 5) and EntreePage.choixIngredient.get() == 2 and \
                EntreePage.choixIngredientViande.get() == 1 and EntreePage.choixDuPrixEntree.get() == 0:
            if len(EntreePage.vin_viandeRouge_set) != 0:
                PageRecommandation.vin.set(random.choice(tuple(EntreePage.vin_viandeRouge_set)))

        elif (
                EntreePage.typeEntree.get() == 3 or EntreePage.typeEntree.get() == 4 or \
                EntreePage.typeEntree.get() == 5) and EntreePage.choixIngredient.get() == 2 and \
                EntreePage.choixIngredientViande.get() == 2 and EntreePage.choixDuPrixEntree.get() == 0:
            if len(EntreePage.vin_gibier_set) != 0:
                PageRecommandation.vin.set(random.choice(tuple(EntreePage.vin_gibier_set)))

        elif (
                EntreePage.typeEntree.get() == 3 or EntreePage.typeEntree.get() == 4 or \
                EntreePage.typeEntree.get() == 5) and EntreePage.choixIngredient.get() == 3 and \
                EntreePage.choixDuPrixEntree.get() == 0:
            if len(EntreePage.vin_legumes_set) != 0:
                PageRecommandation.vin.set(random.choice(tuple(EntreePage.vin_legumes_set)))

        elif EntreePage.typeEntree.get() == 0 and EntreePage.choixDuPrixEntree.get() == 1:
            PageRecommandation.vin.set(random.choice(EntreePage.charcuteriesVin)['Vin'])

        elif EntreePage.typeEntree.get() == 1 and EntreePage.choixDuPrixEntree.get() == 1:
            PageRecommandation.vin.set(random.choice(EntreePage.coquillagesVin)['Vin'])

        elif EntreePage.typeEntree.get() == 2 and EntreePage.choixFromage.get() == 0 and \
                EntreePage.choixDuPrixEntree.get() == 1:
            PageRecommandation.vin.set(random.choice(EntreePage.fromagesAffinésVin)['Vin'])

        elif EntreePage.typeEntree.get() == 2 and EntreePage.choixFromage.get() == 1 and \
                EntreePage.choixDuPrixEntree.get() == 1:
            PageRecommandation.vin.set(random.choice(EntreePage.fromagesDouxVin)['Vin'])

        elif EntreePage.typeEntree.get() == 2 and EntreePage.choixFromage.get() == 2 and \
                EntreePage.choixDuPrixEntree.get() == 1:
            PageRecommandation.vin.set(random.choice(EntreePage.fromagesChevreVin)['Vin'])

        elif (
                EntreePage.typeEntree.get() == 3 or EntreePage.typeEntree.get() == 4 or \
                EntreePage.typeEntree.get() == 5) and EntreePage.choixIngredient.get() == 0 and \
                EntreePage.choixIngredientFromage.get() == 0 and EntreePage.choixDuPrixEntree.get() == 1:
            PageRecommandation.vin.set(random.choice(EntreePage.fromagesAffinésVin)['Vin'])

        elif (
                EntreePage.typeEntree.get() == 3 or EntreePage.typeEntree.get() == 4 or \
                EntreePage.typeEntree.get() == 5) and EntreePage.choixIngredient.get() == 0 and \
                EntreePage.choixIngredientFromage.get() == 1 and EntreePage.choixDuPrixEntree.get() == 1:
            PageRecommandation.vin.set(random.choice(EntreePage.fromagesDouxVin)['Vin'])

        elif (
                EntreePage.typeEntree.get() == 3 or EntreePage.typeEntree.get() == 4 or \
                EntreePage.typeEntree.get() == 5) and EntreePage.choixIngredient.get() == 0 and \
                EntreePage.choixIngredientFromage.get() == 2 and EntreePage.choixDuPrixEntree.get() == 1:
            PageRecommandation.vin.set(random.choice(EntreePage.fromagesChevreVin)['Vin'])

        elif (
                EntreePage.typeEntree.get() == 3 or EntreePage.typeEntree.get() == 4 or \
                EntreePage.typeEntree.get() == 5) and EntreePage.choixIngredient.get() == 1 and \
                EntreePage.choixIngredientPoisson.get() == 0 and EntreePage.choixDuPrixEntree.get() == 1:
            PageRecommandation.vin.set(random.choice(EntreePage.poissonMerVin)['Vin'])

        elif (
                EntreePage.typeEntree.get() == 3 or EntreePage.typeEntree.get() == 4 or \
                EntreePage.typeEntree.get() == 5) and EntreePage.choixIngredient.get() == 1 and \
                EntreePage.choixIngredientPoisson.get() == 1 and EntreePage.choixDuPrixEntree.get() == 1:
            PageRecommandation.vin.set(random.choice(EntreePage.poissonEauDouceVin)['Vin'])

        elif (
                EntreePage.typeEntree.get() == 3 or EntreePage.typeEntree.get() == 4 or \
                EntreePage.typeEntree.get() == 5) and EntreePage.choixIngredient.get() == 2 and \
                EntreePage.choixIngredientViande.get() == 0 and EntreePage.choixDuPrixEntree.get() == 1:
            PageRecommandation.vin.set(random.choice(EntreePage.viandeBlancheVin)['Vin'])

        elif (
                EntreePage.typeEntree.get() == 3 or EntreePage.typeEntree.get() == 4 or \
                EntreePage.typeEntree.get() == 5) and EntreePage.choixIngredient.get() == 2 and \
                EntreePage.choixIngredientViande.get() == 1 and EntreePage.choixDuPrixEntree.get() == 1:
            PageRecommandation.vin.set(random.choice(EntreePage.viandeRougeVin)['Vin'])

        elif (
                EntreePage.typeEntree.get() == 3 or EntreePage.typeEntree.get() == 4 or \
                EntreePage.typeEntree.get() == 5) and EntreePage.choixIngredient.get() == 2 and \
                EntreePage.choixIngredientViande.get() == 2 and EntreePage.choixDuPrixEntree.get() == 1:
            PageRecommandation.vin.set(random.choice(EntreePage.gibierVin)['Vin'])

        elif (
                EntreePage.typeEntree.get() == 3 or EntreePage.typeEntree.get() == 4 or \
                EntreePage.typeEntree.get() == 5) and EntreePage.choixIngredient.get() == 3 and \
                EntreePage.choixDuPrixEntree.get() == 1:
            PageRecommandation.vin.set(random.choice(EntreePage.legumesVin)['Vin'])

        descr = list(prolog.query("description(Vin, Description)"))

        for i in range(len(descr)):
            descr[i]['Vin'] = descr[i]['Vin'].replace("_", " ").capitalize()

        var3 = StringVar()
        for i in range(len(descr)):
            if descr[i]['Vin'] == PageRecommandation.vin.get():
                var3.set(descr[i]['Description'])

        self.description = Label(self.frame, textvariable=var3, font=("Helvetica", 10, "bold"),
                                 height=12, width=37, relief=FLAT).place(x=602, y=238)

        if len(EntreePage.vin_charcuteries_set) != 0 or len(EntreePage.vin_coquillages_set) != 0 or \
                len(EntreePage.vin_fromagesAffinés_set) != 0 or len(EntreePage.vin_fromagesDoux_set) != 0 or \
                len(EntreePage.vin_fromagesChevre_set) != 0 or len(EntreePage.vin_poissonMer_set) != 0 or \
                len(EntreePage.vin_poissonEauDouce_set) != 0 or len(EntreePage.vin_viandeBlanche_set) != 0 or \
                len(EntreePage.vin_viandeRouge_set) != 0 or len(EntreePage.vin_gibier_set) != 0 or \
                len(EntreePage.vin_legumes_set) != 0:
            self.label1
            self.label3
            self.description


        elif len(EntreePage.vin_charcuteries_set) == 0 or len(EntreePage.vin_coquillages_set) == 0 or \
                len(EntreePage.vin_fromagesAffinés_set) == 0 or len(EntreePage.vin_fromagesDoux_set) == 0 or \
                len(EntreePage.vin_fromagesChevre_set) == 0 or len(EntreePage.vin_poissonMer_set) == 0 or \
                len(EntreePage.vin_poissonEauDouce_set) == 0 or len(EntreePage.vin_viandeBlanche_set) == 0 or \
                len(EntreePage.vin_viandeRouge_set) == 0 or len(EntreePage.vin_gibier_set) == 0 or \
                len(EntreePage.vin_legumes_set) == 0:
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
