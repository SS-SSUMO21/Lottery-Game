import random


def cliqueLancer():
 
 lblResultats['text'] = ""
 tableau=[]
 tableau2=[]
 n = 0
 i = 0

 while n < 2 : 
   x = random.randint(1,6)
   tableau.append(x)
   n += 1
 print("{}".format(tableau))

 while i < 2 : 
  x = random.randint(1,6)
  tableau2.append(x)
  i += 1
 print("{}".format(tableau2))

 if(tableau==tableau2):
  lblResultats ['text'] = ("Vous avez gagné!, vos numéros sont {}, les numéros gagnants sont {}".format(tableau, tableau2))
  print("Yay!, vous avez gagné 100 000 $")
   
 else: 
  lblResultats ['text'] =("Vous avez perdu, vos numéros sont {}, les numéros gagnants sont {}".format(tableau, tableau2))

 


import tkinter as tk

#déclaration de la fenetre

fenetre= tk.Tk()
fenetre.title("La loterie de Sam")
fenetre['bg']= "#2b592a"
fenetre.geometry("500x600")



lblTitre = tk.Label(fenetre)

lblTitre['text'] = "Jeu de Loterie"
lblTitre['background'] = "#2b592a"
lblTitre['foreground'] = "#d3dbd3"
lblTitre['font'] = "Arial 18"
lblTitre.grid(padx=150)

#---Création du Sous-titres--------

lblCommence = tk.Label(fenetre)
lblCommence['text'] = "cliqué sur le bouton (Lancer) pour commencer"
lblCommence['background'] = "#2b592a"
lblCommence['foreground'] = "#d3dbd3"
lblCommence['font'] = "Arial 10"
lblCommence.grid(row=1, column=0, padx=5, pady=5)


lblBon = tk.Label(fenetre)
lblBon ['text'] = "Bonne chance!"
lblBon['background'] = "#2b592a"
lblBon['foreground'] = "#d3dbd3"
lblBon['font'] = "Arial 10"
lblBon.grid(row=3, column=0, padx=5, pady=5)


# Bouton Lancer

btnLancer = tk.Button(fenetre)
btnLancer['text'] = "Lancer"
btnLancer['font'] = "Arial 10"
btnLancer['width'] = 35
btnLancer['command'] = cliqueLancer
btnLancer.grid(row=7, padx=80)

# Label pour afficher les résultats

lblResultats = tk.Label(fenetre)
lblResultats['text'] = ""
lblResultats['background'] = "#2b592a"
lblResultats['foreground'] = "#d3dbd3"
lblResultats['font'] = "Arial 15"
lblResultats['wraplength'] = 375
lblResultats.grid(row=8, column=0, padx=5, pady=5)



print("Bienvenue à la loterie de Sam. Pour commencer, vous devrez lancer le dé. si vous obtenez les bons nombres, vous gagnerez 100 000 $. Veuillez noter que vous ne gagnerez pas réellement d'argent, c'est juste pour s'amuser.")

# Création du image

imgMovie = tk.PhotoImage(file="dice.gif")

lblExample = tk.Label(fenetre)
lblExample['image'] = imgMovie
lblExample.grid()

#---------Programme principal--------------

fenetre.mainloop()
