import tkinter as tk
creds = 'tempfile.temp'

class MainWindow(tk.Tk):

    def __init__(self, *args, **kwargs):
        self.roots = tk.Tk()

    def Cadastrar(self):
        self.roots.title('Signup')
        intruction = Label(roots, text='Novo login\n')
        intruction.grid(row=0, column=1, sticky=W)
        self.roots.minsize(width=300, height=350)
        self.roots.maxsize(width=300, height=350)

        nameL = Label(self.roots, text='Novo usuario: ')
        pwordL = Label(self.roots, text='Nova senha: ')
        nameL.grid(row=1,column=0,sticky=E)
        pwordL.grid(row=2,column=0,sticky=E)

        nameE = Entry(self.roots)
        pwordE = Entry(self.roots, show='*')
        nameE.grid(row=1, column=1, stick=E)
        pwordE.grid(row=2, column=1, sticky=E)

        signupBut = Button(self.roots, text='Cadastrar', command=FSSignup)
        signupBut.grid(columnspan=2, sticky=W)
        self.roots.mainloop()

    def Login(self):
        pass

    def FSSignup(self):
        with open(creds, 'w') as f:
            f.write(nameE.get())
            f.write('\n')
            f.write(pwordE.get())
            f.close()
        self.roots.destroy()
        Login()


#Cadastrar()

