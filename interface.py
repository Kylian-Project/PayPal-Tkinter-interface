from tkinter import *

def affi(i):
    photo=PhotoImage(file=i)
    lab1.config(image=photo)
    lab1.image=photo

Fenetre=Tk() #création de la fenêtre principale
Fenetre.geometry("1000x488") #précise la taille de la fenêtre
Fenetre.resizable(width=False, height=False)
Fenetre.title("Paypal - Service En Ligne")

lab1=Label(Fenetre)
lab1.place(x=0, y=0, relwidth=1, relheight=1)

imgacti=PhotoImage(file="actibutton.PNG")
activbutton=Button(Fenetre,image=imgacti, command=Fenetre.destroy, borderwidth=0, highlightthickness=0, cursor='hand2')
activbutton.place(x=250, y=12)

Button(Fenetre,text="Etape 1",command=lambda: affi("interface1.png")).pack(side="left")

imgleave=PhotoImage(file="leavebutton.PNG")
leavebutton=Button(Fenetre,image=imgleave, command=Fenetre.destroy, borderwidth=0, highlightthickness=0, cursor='hand2')
leavebutton.place(x=800, y=12)

Fenetre.mainloop()