from Tkinter import *

def new_windowEuro():
    rec_a = float(a.get())

    if rec_a != 0:
        n_window = Tk()
        n_frame = Frame(n_window, bg='#41B77F')
        text_som = Label(n_frame, text="La convertion de cette somme en Euro est : ")
        eur = Label(n_frame, text='Euro.', bg='#41B77F', fg='red')
        conv = float(rec_a/650)
        new_label = Label(n_frame, text=conv, font="Cursive, 15", bg="#41B77F", fg="red")
        n_window.geometry("330x170+800+420")
        n_window.minsize(330, 170)
        n_window.maxsize(330, 170)
        n_window.config(background='#41B77F')
        n_window.title('ConvertiseurEURO')
        eur.pack(side=RIGHT)
        n_frame.pack(expand=YES)
        text_som.pack(expand=YES, pady=10)
        new_label.pack(expand=YES)
        n_window.mainloop()

    else:
        n_win_error = Tk()
        n_frame_error = Frame(n_win_error)
        n_label_error = Label(n_frame_error, text='Veuillez saisir une valeurs differente de 0', fg='red')
        n_win_error.geometry("200x150+800+420")
        n_win_error.minsize(200, 150)
        n_win_error.maxsize(200, 150)
        n_win_error.title("FatalERROR")

        n_label_error.pack(expand=YES)
        n_frame_error.pack(expand=YES, pady=10)
        n_win_error.mainloop()


def new_windowCFA():
    rec_a = float(a.get())
    if rec_a != 0:
        n_window = Tk()
        n_frame = Frame(n_window, bg='#41B77F')
        text_som = Label(n_frame, text="La convertion de cette somme en FCFA est : ")
        eur = Label(n_frame, text='Fcfa.', bg='#41B77F', fg='red')
        conv = float(rec_a*650)
        new_label = Label(n_frame, text=conv, font="Cursive, 15", bg="#41B77F", fg="red")
        n_window.geometry("330x170+800+420")
        n_window.minsize(330, 170)
        n_window.maxsize(330, 170)
        n_window.config(background='#41B77F')
        n_window.title('ConvertiseurCFA')
        eur.pack(side=RIGHT)
        n_frame.pack(expand=YES)
        text_som.pack(expand=YES, pady=10)
        new_label.pack(expand=YES)
        n_window.mainloop()

    else:
        n_win_error = Tk()
        n_frame_error = Frame(n_win_error)
        n_label_error = Label(n_frame_error, text='Veuillez saisir une valeurs differente de 0', fg='red')
        n_win_error.geometry("200x150")
        n_win_error.minsize(250, 150)
        n_win_error.maxsize(250, 150)
        n_win_error.title("FatalERROR")

        n_label_error.pack(expand=YES)
        n_frame_error.pack(expand=YES, pady=10)
        n_win_error.mainloop()


# creeation fenetre main
main_window = Tk()
frame = Frame(main_window, bg='#41B77F')
frame1 = Frame(main_window)
button = Button(frame, text='Convertir en Euro', font=("Cursive", 15), bg='green', fg='white', command=new_windowEuro)
button1 = Button(frame, text='Convertir En CFA', font=("Cursive", 15), bg='orange', fg='white', command=new_windowCFA)

a = Entry(frame, bg='darkcyan', fg='white', width=30, font="15")

main_window.title("App-Convertisseur")
main_window.geometry("1024x724+470+150")
main_window.minsize(700, 500)
main_window.maxsize(1024, 724)
main_window.config(background='#aedbc3')

window_label = Label(frame1, text="@franzdeussom", font=("Cursive", 15), bg='#41B77F', fg='white')
window_label.pack()
window_label = Label(frame, text="Entrer la somme a convertir en Euro/Fcfa :", font=("Courrier", 15), bg='#41B77F', fg='white')
window_label.pack()

a.pack(pady=8, padx=25)
frame.pack(expand = YES)
frame1.pack(expand = NO)
button.pack(pady=25)
button1.pack(pady=25)
#affichage de la fenetre
main_window.mainloop()

