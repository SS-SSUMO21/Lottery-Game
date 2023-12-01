import random

def cliqueTotal():

   nb_plat = nb.get()
   
   if (plat.get()==1):
     if(nb_plat>=1 and nb_plat<=10):
      rabais = nb_plat * plat1 * y
      Soustotal= nb_plat * plat1
      Taxes = (Soustotal - rabais) * 0.13
      Total = Soustotal - rabais + Taxes
     else:
       print("Erreur, veuillez entrer un montant entre (1 - 10)")
   
   elif(plat.get()==2):
    if(nb_plat>=1 and nb_plat<=10):
      rabais = nb_plat * plat1 * y
      Soustotal= nb_plat * plat1
      Taxes = (Soustotal - rabais) * 0.13
      Total = Soustotal - rabais + Taxes
    else:
       print("Erreur, veuillez entrer un montant entre (1 - 10)")
   
   elif(plat.get()==3):
    if(nb_plat>=1 and nb_plat<=10):
      rabais = nb_plat * plat1 * y
      Soustotal= nb_plat * plat1
      Taxes = (Soustotal - rabais) * 0.13
      Total = Soustotal - rabais + Taxes
    else:
       print("Erreur, veuillez entrer un montant entre (1 - 10)")

   elif(plat.get()==4):
    if(nb_plat>=1 and nb_plat<=10):
      rabais = nb_plat * plat1 * y
      Soustotal= nb_plat * plat1
      Taxes = (Soustotal - rabais) * 0.13
      Total = Soustotal - rabais + Taxes
    else:
       print("Erreur, veuillez entrer un montant entre (1 - 10)")
   else:
     print("Erreur, veuillez choisir un plat de 1 à 4")

   lblTotal['text'] = "Soutotal : {:.2f}, Rabais(%) : {:.2f}, Rabais($) : {:.2f}, Taxes - TVH (13%) : {:.2f}, Total : {:.2f} ".format(Soustotal, x, rabais, Taxes, Total)

  
# ----------Intialisation de la variable-----------

x = random.randint(1,99)
y = x / 100


Soustotal=0
rabais=0
Total=0
Taxes=0

plat1 = 12.50
plat2 = 11.50
plat3 = 10.50
plat4 = 13.50


import tkinter as tk

#déclaration de la fenetre

fenetre= tk.Tk()
fenetre.title("Le restaurant de Sam")
fenetre['bg']= "#2b592a"
fenetre.geometry("500x400")



lblTitre = tk.Label(fenetre)

lblTitre['text'] = "Menu du resto"
lblTitre['background'] = "#2b592a"
lblTitre['foreground'] = "#d3dbd3"
lblTitre['font'] = "Arial 18"
lblTitre.grid(padx=150)

#---Création du Sous-titres--------

lblSousTitrePi = tk.Label(fenetre)
lblSousTitrePi['text'] = "plat #1 Pizza.......12,50$"
lblSousTitrePi['background'] = "#2b592a"
lblSousTitrePi['foreground'] = "#d3dbd3"
lblSousTitrePi['font'] = "Times 13"
lblSousTitrePi.grid(row=1, column=0, padx=1, pady=1, sticky=tk.W)


lblSousTitreL = tk.Label(fenetre)
lblSousTitreL['text'] = "plat #2 Lasagne..11,50$"
lblSousTitreL['background'] = "#2b592a"
lblSousTitreL['foreground'] = "#d3dbd3"
lblSousTitreL['font'] = "Times 13"
lblSousTitreL.grid(row=2, column=0, padx=1, pady=4, sticky=tk.W)

lblSousTitreB = tk.Label(fenetre)
lblSousTitreB['text'] = "plat #3 Burger....10,50$"
lblSousTitreB['background'] = "#2b592a"
lblSousTitreB['foreground'] = "#d3dbd3"
lblSousTitreB['font'] = "Times 13"
lblSousTitreB.grid(row=3, column=0, padx=2, pady=5, sticky=tk.W)

lblSousTitreP = tk.Label(fenetre)
lblSousTitreP['text'] = "plat #4 Pâtes......13,50$"
lblSousTitreP['background'] = "#2b592a"
lblSousTitreP['foreground'] = "#d3dbd3"
lblSousTitreP['font'] = "Times 13"
lblSousTitreP.grid(row=4, column=0, padx=2, pady=6, sticky=tk.W)

# Affiche les sous-titres

lblSousTitreX = tk.Label(fenetre)
lblSousTitreX['text'] = "Quel plat (1,2,3 ou 4) = "
lblSousTitreX['background'] = "#2b592a"
lblSousTitreX['foreground'] = "#d3dbd3"
lblSousTitreX['font'] = "Arial 10"
lblSousTitreX.grid(row=5, column=0, columnspan=2, padx=34, pady=5, sticky=tk.W)
lblSousTitreY = tk.Label(fenetre)

lblSousTitreY['text'] = "Nombre de plat(s) (1 - 10) = "
lblSousTitreY['background'] = "#2b592a"
lblSousTitreY['foreground'] = "#d3dbd3"
lblSousTitreY['font'] = "Arial 10"
lblSousTitreY.grid(row=6, column=0, columnspan=2, padx=3, pady=5, sticky=tk.W)




# Entrez le nombre de plat (text)


plat = tk.IntVar()
txtX= tk.Entry(fenetre)
txtX['font'] = "Arial 10"
txtX['width'] = 10
txtX['textvariable'] = plat
txtX.grid(row=5, column=0, padx=8, pady=5)

nb = tk.IntVar()
txtX= tk.Entry(fenetre)
txtX['font'] = "Arial 10"
txtX['width'] = 10
txtX['textvariable'] = nb
txtX.grid(row=6, column=0, padx=10, pady=5)

# Bouton Calculer le total

btnCalculer = tk.Button(fenetre)
btnCalculer['text'] = "Calculer la Total"
btnCalculer['font'] = "Arial 10"
btnCalculer['width'] = 35
btnCalculer['command'] = cliqueTotal
btnCalculer.grid(row=7, padx=80)

# Label pour afficher le total

lblTotal = tk.Label(fenetre)
lblTotal['text'] = ""
lblTotal['background'] = "#2b592a"
lblTotal['foreground'] = "#d3dbd3"
lblTotal['font'] = "Arial 15"
lblTotal['wraplength'] = 375
lblTotal.grid(row=8, column=0, padx=5, pady=5)


print("Ce programme calcule votre prix total pour votre plat choisi, le montant de ce plat choisi avec un rabais sélectionné aléatoirement.")


fenetre.mainloop()
