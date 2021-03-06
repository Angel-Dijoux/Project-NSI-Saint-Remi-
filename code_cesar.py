# --- Angel Dijoux - Manon Da-Rocha - Camille Deslis --- 
# --- Projet CESAR NSI --- 

from tkinter import *
import tkinter.messagebox
import webbrowser

#-----------------------------------------------------------------------------------------------

def code_cesar_encryp(): #Code de chiffrement
    text = entry_user.get()
    shift = int(entry_shift.get())
    letter = [] #Crée un liste vide où sera stocké le texte
    if text >= chr(65) and text <= chr(122):
        if text >= chr(65) and text <= chr(90): #prends que les valeurs ASCII entre 65 et 90
            if shift <= 0 or shift > 50:
                return tkinter.messagebox.showerror('Code de César', 'Veuillez saisir un décalage correct !' )#Message d'erreur en cas de mauvais décalage
            else:
                for char_user in text:
                    if char_user == " ":
                        letter.append(chr(32)) #Ajoute un espace, quand on en entre un
                    else:
                        code_ascii = ord(char_user)+shift #Effectue un décalage inscrit par l'utilisateur
                        if code_ascii > 90: #retourne au débur de l'alphabet
                            code_ascii = code_ascii-26
                        char_user_result = chr(code_ascii) #transforme un caractère en entier pour pouvoir être calculer
                        letter.append(char_user_result)
                    str_maj = ''.join(letter) #transforme la liste en chaine de caractères
                return label_resul.configure(text=str_maj)
        elif text >= chr(97) and text <= chr(122): #Pour les minuscules
            if shift <= 0 or shift > 50:
                return tkinter.messagebox.showerror('Code de César', 'Veuillez saisir un décalage correct !' ) #Message d'erreur en cas de mauvais décalage
            else:
                for char_user in text:
                    if char_user == " ":
                        letter.append(chr(32)) #Ajoute un espace, quand on en entre un
                    else:
                        code_ascii = ord(char_user)+shift #Effectue un décalage inscrit par l'utilisateur
                        if code_ascii > 122:
                            code_ascii = code_ascii-26
                        char_user_result = chr(code_ascii)
                        letter.append(char_user_result)
                    str_minu = ''.join(letter) #transforme la liste en chaine de caractères
                return label_resul.configure(text=str_minu)
    else:
        return tkinter.messagebox.showerror('Code de César', 'Mauvais caractères')
#-----------------------------------------------------------------------------------------------

def code_cesar_unscramble(): #Code de déchiffrement
    text = entry_user.get()
    shift = int(entry_shift.get())
    letter = [] #Crée un liste vide où sera stocké le texte
    if text >= chr(65) and text <= chr(122):
        if text >= chr(65) and text <= chr(90): #prends que les valeurs ASCII entre 65 et 90
            if shift <= 0 or shift > 50:
                return tkinter.messagebox.showerror('Code de César', 'Veuillez saisir un décalage correct !' )#Message d'erreur en cas de mauvais décalage
            else:
                for char_user in text:
                    if char_user == " ":
                        letter.append(chr(32)) #Ajoute un espace, quand on en entre un
                    else:
                        code_ascii = ord(char_user)-shift #Effectue un décalage inscrit par l'utilisateur
                        if code_ascii < 65 and code_ascii < 90: #retourne au débur de l'alphabet
                            code_ascii = code_ascii+26
                        char_user_result = chr(code_ascii) #transforme un caractère en entier pour pouvoir être calculer
                        letter.append(char_user_result)
                    str_maj = ''.join(letter) #transforme la liste en chaine de caractères
                return label_resul.configure(text=str_maj)
        elif text >= chr(97) and text <= chr(122): #Pour les minuscules
            if shift <= 0 or shift > 50:
                return tkinter.messagebox.showerror('Code de César', 'Veuillez saisir un décalage correct !' ) #Message d'erreur en cas de mauvais décalage
            else:
                for char_user in text:
                    if char_user == " ":
                        letter.append(chr(32)) #Ajoute un espace, quand on en entre un
                    else:
                        code_ascii = ord(char_user)-shift #Effectue un décalage inscrit par l'utilisateur
                        if code_ascii < 97 and code_ascii < 122:
                            code_ascii = code_ascii+26
                        char_user_result = chr(code_ascii)
                        letter.append(char_user_result)
                    str_minu = ''.join(letter) #transforme la liste en chaine de caractères
                return label_resul.configure(text=str_minu)
    else:
        return tkinter.messagebox.showerror('Code de César', 'Mauvais caractères')

#-----------------------------------------------------------------------------------------------

#help 


def github():
    lien_github='https://github.com/Angel-Dijoux/Code-Cesar/tree/main'
    return webbrowser.open(lien_github)
def instagram():
    lien_instagram='https://www.instagram.com/elki_8/'
    return webbrowser.open(lien_instagram)
windows = Tk()

#Paramètres de base de la fenêtre
windows.title("Code de César") #Nom de la fenêtre
windows.geometry("1080x720") #Taille de base de la fenêtre
windows.minsize(480, 360) #Taille minimal de la fenêtre
windows.config(background='#2f3136') #Coueleur de font de la fenêtre

#Compartiment pour classer chaque éléments de la fenêtre
frame = Frame(windows, bg='#2f3136')
frame_entry = Frame(windows, bg='#2f3136')
frame_result = Frame(windows, bg='#2f3136')

#Premier texte
label_title = Label(windows, text="Code de César", font=("arial", 25), bg='#2f3136', fg='white')
label_title.pack()

#Zones d'entrées
entry_text = Label(frame_entry,text="Entrez du texte à crypté ou décrypté", font=("arial", 15), bg='#2f3136', fg='white')
entry_text.pack()
entry_user = Entry(frame_entry, font=("arial", 18), bg='#696969',fg='white')
entry_user.pack()
shift_text = Label(frame_entry,text="Saisissez un décallage", font=("arial", 15), bg='#2f3136', fg='white')
shift_text.pack()
entry_shift = Entry(frame_entry, font=("arial", 18), bg='#696969',fg='white')
entry_shift.pack()

#Zone d'affichage 
label_resul = Label(frame_result,font=("arial", 18), bg='#2f3136',fg='white',width=150, height=10 )
label_resul.pack()

#Boutons crypté et décrypté
button_encypt = Button(frame, text="Crypté", font=("arial",15), bg="#6A5ACD" ,fg='white', command=code_cesar_encryp )
button_encypt.grid(row=1, column=1, sticky=E)
button_unscramble = Button(frame, text="Décrypté", font=("arial", 15), bg="#6A5ACD", fg="white", command=code_cesar_unscramble )
button_unscramble.grid(row=1, column=2, sticky=E)

#Barre des menus
menu_bar = Menu(windows,background='white', foreground='black', activebackground='#6A5ACD', activeforeground='black')
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_command(label="Quit", command=windows.quit)
windows.config(menu=menu_bar)

help = Menu(menu_bar, tearoff=0,background='white', foreground='black', activebackground='#6A5ACD', activeforeground='black')  
help.add_command(label="GitHub", command=github) 
help.add_command(label="Instagram", command=instagram) 
menu_bar.add_cascade(label="Help", menu=help) 

frame_entry.pack(expand=YES)
frame_result.pack(expand=YES)
frame.pack(expand=YES)

windows.mainloop()

#-----------------------------------------------------------------------------------------------
