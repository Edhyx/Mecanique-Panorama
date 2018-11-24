try:
    import Tkinter as Tk # python 2
except ModuleNotFoundError:
    import tkinter as Tk # python 3

from controller import Controller

class View:
    def __init__(self):
        print "Init view"
        self.root = Tk.Tk()
        self.root.geometry('800x480') #Dimensions of 7' Raspberry Pi screen

        self.controller = Controller()
        self.first_page(self.root, self.controller)

    def get_iso(self):
        self.iso_page(self.root, self.controller)

    def first_page(self, root, controller):
        Tk.Grid.rowconfigure(root, 0, weight=1)
        Tk.Grid.columnconfigure(root, 0, weight=1)
        self.frame = Tk.Frame(root)

        self.frame.grid(row=0, column=0, sticky=Tk.N+Tk.S+Tk.E+Tk.W)

        for row_index in range(2):
            Tk.Grid.rowconfigure(self.frame, row_index, weight=1)
        for col_index in range(4):
            Tk.Grid.columnconfigure(self.frame, col_index, weight=1)
        btn_iso = Tk.Button(self.frame, text='ISO', command=self.get_iso) #create a button inside frame
        btn_iso.grid(row=0, column=0, padx=25, pady=25, sticky=Tk.N+Tk.S+Tk.E+Tk.W)
        btn_aper = Tk.Button(self.frame, text='Aperture') #create a button inside frame
        btn_aper.grid(row=0, column=1, padx=25, pady=25, sticky=Tk.N+Tk.S+Tk.E+Tk.W)
        btn_speed = Tk.Button(self.frame, text='Speed', command=controller.hello) #create a button inside frame
        btn_speed.grid(row=0, column=2, padx=25, pady=25, sticky=Tk.N+Tk.S+Tk.E+Tk.W)
        btn_inter = Tk.Button(self.frame, text='Intervall') #create a button inside frame
        btn_inter.grid(row=1, column=0, padx=25, pady=25, sticky=Tk.N+Tk.S+Tk.E+Tk.W)
        btn_live = Tk.Button(self.frame, text='Live View') #create a button inside frame
        btn_live.grid(row=1, column=1, padx=25, pady=25, sticky=Tk.N+Tk.S+Tk.E+Tk.W)
        btn_quit = Tk.Button(self.frame, text='Quit', command=quit) #create a button inside frame
        btn_quit.grid(row=1, column=2, padx=25, pady=25, sticky=Tk.N+Tk.S+Tk.E+Tk.W)
        btn_info = Tk.Button(self.frame, text='Infos') #create a button inside frame
        btn_info.grid(row=0, column=3, padx=25, pady=25, sticky=Tk.N+Tk.S+Tk.E+Tk.W)
        btn_ = Tk.Button(self.frame, text='Start') #create a button inside frame
        btn_.grid(row=1, column=3, padx=25, pady=25, sticky=Tk.N+Tk.S+Tk.E+Tk.W)


    def iso_page(self, root, controller):
        Tk.Grid.rowconfigure(root, 0, weight=1)
        Tk.Grid.columnconfigure(root, 0, weight=1)
        self.frame = Tk.Frame(root)

        self.frame.grid(row=0, column=0, sticky=Tk.N+Tk.S+Tk.E+Tk.W)
        for row_index in range(2):
            Tk.Grid.rowconfigure(self.frame, row_index, weight=1)
        for col_index in range(4):
            Tk.Grid.columnconfigure(self.frame, col_index, weight=1)

        self.btn_back = Tk.Button(self.frame, text='Back', command=self.first_page) #create a button inside frame
        self.btn_back.grid(row=0, column=0, padx=25, pady=25, sticky=Tk.N+Tk.W)
        self.btn_ok = Tk.Button(self.frame, text='OK')
        self.btn_ok.grid(row=1, column=2, padx=25, pady=25, sticky=Tk.S+Tk.E)
        self.label = Tk.Label(self.frame, text="ISO Parameter")
        self.label.grid(row=0, column=1)
        self.label2 = Tk.Label(self.frame, text='ISO : ' )
        self.label2.grid(row=0, column=2)
        self.listbox = Tk.Listbox(self.frame)
        self.listbox.grid(row=1, column=1)

        #self.listbox.bind("<<ListboxSelect>>", printer)

        for item in self.controller.iso_function():
            self.listbox.insert(Tk.END, item)


    def run(self):
        self.root.mainloop()
