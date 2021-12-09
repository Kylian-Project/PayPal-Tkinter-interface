from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from random import randint

def change_couleur():
    list_couleur = ['green','red','yellow','blue','black','white','purple']
    i = randint(0, 6)
    couleur = list_couleur[i]
    Fenetre.config(bg=list_couleur[i])

counter = 0
def connect():
    if Entree.get() == 'Prof' or Entree.get() == 'prof' and Entree2.get() == 'Nsi' or Entree2.get() == 'nsi':
        messagebox.showinfo('Connexion', "Identifiant correct")

        progbar = Toplevel(Fenetre)
        progresse = ttk.Progressbar(progbar, orient="horizontal", length=500, mode="determinate")

        ####### Centrer fenêtre #######

        page_height = 400
        page_width = 700
        screen_width_px = progbar.winfo_screenwidth()
        screen_height_px = progbar.winfo_screenheight()
        x_cordinate = int((screen_width_px / 2) - (page_width / 2))
        y_cordinate = int(((screen_height_px / 2) - (page_height / 2))-50) #le -50 relève un peut la fenêtre, je la trouvais trop basse
        progbar.geometry("{}x{}+{}+{}".format(page_width, page_height, x_cordinate, y_cordinate))

        ####### Centrer fenêtre #######

        progbar.config(bg="#0B56A9")
        progresse.place(x=100, y=230)

        vide2 = Label(progbar, text="", bg="#0B56A9")
        vide2.pack(pady=10)

        photo = PhotoImage(file="paypalback.png")
        lab1 = Label(progbar, image=photo, bg="#0B56A9")
        lab1.pack(side=TOP, pady=40)

        connectmsg = Label(progbar, text="Connexion en cours ...", bg="#0B56A9")
        connectmsg.configure(font=("Trebuchet MS", 20, "bold"))
        connectmsg.pack()

        def update(delay=10):
            global counter
            progresse.step(0.6)
            counter += 1
            if counter < 167:
                progresse.after(delay, update)
            else:
                progbar.destroy()
                Fenetre.iconify()
                openint1()

        update()
        progbar.mainloop()
    else :
        messagebox.showwarning('Attention', "Tentative de FRAUDE !")

def efface():
    Entree.delete(0, END)
    Entree2.delete(0, END)

def enterconnect(event):
    connect()

####################################
######## NOUVELLES FENETRE #########
####################################
def openint1():
    def affi(i):
        photo=PhotoImage(file=i)
        background.config(image=photo)
        background.image=photo

    Fenetre2 = Toplevel(Fenetre)

    ####### Centrer fenêtre #######

    page_height = 488
    page_width = 1000
    screen_width_px = Fenetre2.winfo_screenwidth()
    screen_height_px = Fenetre2.winfo_screenheight()
    x_cordinate = int((screen_width_px / 2) - (page_width / 2))
    y_cordinate = int(((screen_height_px / 2) - (page_height / 2))-50) #le -50 relève un peut la fenêtre, je la trouvais trop basse
    Fenetre2.geometry("{}x{}+{}+{}".format(page_width, page_height, x_cordinate, y_cordinate))

    ####### Centrer fenêtre #######

    Fenetre2.resizable(width=False, height=False)
    Fenetre2.title("Paypal - Service En Ligne")

    background = Label(Fenetre2)
    background.pack(side=BOTTOM)



    affi("interface1.png")

    imgmenu = PhotoImage(file="menu.PNG")
    menu = Label(Fenetre2, image=imgmenu)
    menu.pack(side=TOP)

    imgrecap = PhotoImage(file="recapbutton.PNG")
    recapbutton = Button(Fenetre2, image=imgrecap, command=lambda: affi("interface1.png"), borderwidth=0, highlightthickness=0, cursor='hand2')
    recapbutton.place(x=170, y=13)

    imgacti = PhotoImage(file="actibutton.PNG")
    activbutton = Button(Fenetre2, image=imgacti, command=lambda: affi("interface2.png"), borderwidth=0, highlightthickness=0, cursor='hand2')
    activbutton.place(x=253, y=13)

    imgdmd = PhotoImage(file="dmdbutton.png")
    dmdbutton = Button(Fenetre2, image=imgdmd, command=lambda: affi("interface3.png"), borderwidth=0, highlightthickness=0, cursor='hand2')
    dmdbutton.place(x=315, y=13)

    imgport = PhotoImage(file="portbutton.png")
    portbutton = Button(Fenetre2, image=imgport, command=lambda: affi("interface4.png"), borderwidth=0, highlightthickness=0, cursor='hand2')
    portbutton.place(x=444, y=13)

    imgleave = PhotoImage(file="leavebutton.PNG")
    leavebutton = Button(Fenetre2, image=imgleave, command=Fenetre.destroy, borderwidth=0, highlightthickness=0, cursor='hand2')
    leavebutton.place(x=800, y=12)

    Fenetre2.mainloop()

####################################
########### FIN FENETRE ############
####################################

Fenetre=Tk() #création de la fenêtre principale

####### Centrer fenêtre #######

page_height = 400
page_width = 700
screen_width_px = Fenetre.winfo_screenwidth()
screen_height_px = Fenetre.winfo_screenheight()
x_cordinate = int((screen_width_px / 2) - (page_width / 2))
y_cordinate = int(((screen_height_px / 2) - (page_height / 2))-50) #le -50 relève un peut la fenêtre, je la trouvais trop basse
Fenetre.geometry("{}x{}+{}+{}".format(page_width, page_height, x_cordinate, y_cordinate))

####### Centrer fenêtre #######

Fenetre.resizable(width=False, height=False)
Fenetre.title("Paypal - Service En Ligne")
Fenetre.config(bg="#0B56A9")
Fenetre.bind("<Return>", enterconnect)

mainmsg=Label(Fenetre,text="SERVICE D'ACCUEIL DE PAYPAL", bg="#0B56A9")
mainmsg.configure(font=("Trebuchet MS", 25, "bold"))
mainmsg.pack()

photo=PhotoImage(file="paypal.png")
lab1=Label(Fenetre, image=photo, bg="#0B56A9")
lab1.pack(side=LEFT)


vide=Label(Fenetre, text="", bg="#0B56A9")
msgposte1=Label(Fenetre, text="Entrer votre identifiant", bg="#0B56A9")
msgposte1.configure(font=("Trebuchet MS", 15, "bold"))
Entree = Entry(Fenetre, width=25, justify='center', relief='flat', font=("Trebuchet MS", 13, "bold"))
msgposte2=Label(Fenetre, text="Entrer votre mot de passe", bg="#0B56A9")
msgposte2.configure(font=("Trebuchet MS", 15, "bold"))
Entree2 = Entry(Fenetre, width=25, justify='center',  show='*', relief='flat', font=("Trebuchet MS", 13, "bold"))
trait=Button(Fenetre, text="Se connecter", command=connect, cursor='hand2')
trait.configure(font=("Trebuchet MS", 15, "bold"))
vide.pack(pady=35)
msgposte1.pack()
Entree.pack(pady=10)
msgposte2.pack()
Entree2.pack(pady=10)
trait.pack(pady=3)

clear=Button(Fenetre, text="Effacer", width=10, command=efface, cursor='hand2')
clear.configure(font=("Trebuchet MS", 10, "bold"))
clear.place(x=600, y=360)

leave=Button(Fenetre, text="Quitter", bg='red', fg='black', command=Fenetre.destroy, cursor='hand2')
leave.configure(font=("Trebuchet MS", 15, "bold"))
leave.place(x=10, y=350)

Fenetre.mainloop()