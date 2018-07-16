import tkinter as tk
from tkinter import messagebox
from sqlite3 import Error
import sqlite3

LARGE_FONT= ('Verdana',12)

class mainWindow(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.grid(row=1)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in  (StartPage, Cadastro, Logado):

            frame = F(container,self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky='nsew')

        #frame.grid(row=0,column=0,sticky='nsew')
        #frame.grid(row=110,column=110,sticky='nsew')

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()



class StartPage(tk.Frame): #Frame inicial

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Bem vindo ao $sistema$')
        label.place(relx=0.32, rely=0.09, height=21, width=244)

        #Labels
        #nameL = tk.Label(self, text='Usuario: ')
        #nameL.grid(row= 2, column= 7,padx=5, pady=5, sticky='e')
        #pwordL = tk.Label(self, text='Senha: ')
        #pwordL.grid(row= 6, column=3, padx=5, pady=5, sticky='e')

        #Entrys
        nameE = tk.Entry(self)
        #nameE.grid(row=3, column=0,pady=100)
        pwordE = tk.Entry(self, show='*')
        #pwordE.grid(padx=0, pady=0)


        def verify():  # conecta ao db
            conn = sqlite3.connect('logins.db')
            c = conn.cursor()
            login = nameE.get()
            senha = pwordE.get()
            print(login,senha)

            c.execute("""select user,pword from login where user='{}' and pword='{}'""".format(login, senha))
            exist = c.fetchone()

            if exist is not None:
                messagebox.showinfo("Sucesso", "Usuário logado com sucesso!")
                controller.show_frame(Logado)

            else:
                messagebox.showerror("Erro", "Usuário ou senha incorretos!")
            #print(login, senha)
            conn.close()
            return

        #Botoes
        #button1 = tk.Button(self, text='Login', command=verify)
        #button1.grid(row=30, column=1, sticky='E')
        #button1.configure(takefocus="")
        #button2 = tk.Button(self, text='Cadastrar', command=lambda: controller.show_frame(Cadastro)).grid(row=30, column=5, sticky='e')

class Cadastro(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Novo cadastro')
        label.grid(row=0, column=1)

        #Labels
        nameL = tk.Label(self, text='Novo usuario: ')
        nameL.grid(row=2,sticky='E')
        pwordL = tk.Label(self, text='Nova senha: ')
        pwordL.grid(row=3, sticky='E')

        #Entrys
        nameE = tk.Entry(self)
        nameE.grid(row=2, column=1, sticky='E')
        pwordE = tk.Entry(self, show='*')
        pwordE.grid(row=3, column=1,  sticky='E')

        def cadastro():  # conecta ao db
            conn = sqlite3.connect('logins.db')
            c = conn.cursor()
            login = nameE.get()

            senha = pwordE.get()

            try:
                c.execute("""
                INSERT INTO login (user, pword) 
                VALUES(?,?);""", (login,senha))
                messagebox.showinfo("Sucesso", "Usuário cadastrado!")
                conn.commit()
            except Error as e:
                print(e)
                messagebox.showinfo("Erro", "Usuário já cadastrado!")
            print(login, senha)
            conn.close()
            return

        button1 = tk.Button(self, text='Cadastrar', command=cadastro).grid(row=4, sticky='E')
        button2 = tk.Button(self, text='Voltar', command=lambda: controller.show_frame(StartPage)).grid(row=4, column=2, sticky='E')

class Logado(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Sistema')
        label.grid(row=0, column=1)



app = mainWindow()
app.geometry("400x200")
app.mainloop()