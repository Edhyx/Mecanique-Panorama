try:
    import Tkinter as Tk # python 2
except ModuleNotFoundError:
    import tkinter as Tk # python 3

from controller import Controller
from PIL import Image, ImageTk

class View:
    def __init__(self):
        print "Init view"
        self.root = Tk.Tk()
        self.root.geometry('800x480') #Dimensions of 7' Raspberry Pi screen
        Tk.Grid.rowconfigure(self.root, 0, weight=1)
        Tk.Grid.columnconfigure(self.root, 0, weight=1)
        self.frame = Tk.Frame(self.root)
        self.frame.grid(row=0, column=0, sticky=Tk.N+Tk.S+Tk.E+Tk.W)

        self.controller = Controller()
        self.first_page(self.frame, self.controller)



    def first_page(self, frame, controller):
        for widget in self.frame.winfo_children():
            widget.destroy()
        for row_index in range(2):
            Tk.Grid.rowconfigure(self.frame, row_index, weight=1)
        for col_index in range(4):
            Tk.Grid.columnconfigure(self.frame, col_index, weight=1)
        btn_iso = Tk.Button(self.frame, text='ISO', command=lambda: self.iso_page(self.frame, self.controller)) #create a button inside frame
        btn_iso.grid(row=0, column=0, padx=25, pady=25, sticky=Tk.N+Tk.S+Tk.E+Tk.W)
        btn_aper = Tk.Button(self.frame, text='Aperture') #create a button inside frame
        btn_aper.grid(row=0, column=1, padx=25, pady=25, sticky=Tk.N+Tk.S+Tk.E+Tk.W)
        btn_speed = Tk.Button(self.frame, text='Speed', command=controller.hello) #create a button inside frame
        btn_speed.grid(row=0, column=2, padx=25, pady=25, sticky=Tk.N+Tk.S+Tk.E+Tk.W)
        btn_inter = Tk.Button(self.frame, text='Intervall') #create a button inside frame
        btn_inter.grid(row=1, column=0, padx=25, pady=25, sticky=Tk.N+Tk.S+Tk.E+Tk.W)
        btn_live = Tk.Button(self.frame, text='Live View', command=self.live_view_page) #create a button inside frame
        btn_live.grid(row=1, column=1, padx=25, pady=25, sticky=Tk.N+Tk.S+Tk.E+Tk.W)
        btn_quit = Tk.Button(self.frame, text='Quit', command=quit) #create a button inside frame
        btn_quit.grid(row=1, column=2, padx=25, pady=25, sticky=Tk.N+Tk.S+Tk.E+Tk.W)
        btn_info = Tk.Button(self.frame, text='Infos') #create a button inside frame
        btn_info.grid(row=0, column=3, padx=25, pady=25, sticky=Tk.N+Tk.S+Tk.E+Tk.W)
        btn_ = Tk.Button(self.frame, text='Start') #create a button inside frame
        btn_.grid(row=1, column=3, padx=25, pady=25, sticky=Tk.N+Tk.S+Tk.E+Tk.W)


    def iso_page(self, frame, controller):
        for widget in frame.winfo_children():
                widget.destroy()

        def ok_button():
            print seltext
            controller.set_iso(seltext)
            self.first_page(self.frame, self.controller)

        def printer(event, listbox, label2):
            #print("SELECTED=",self.listbox.get(self.listbox.curselection()))
            index = self.listbox.curselection()[0]
            # get the line's text
            global seltext
            seltext= self.listbox.get(index)
            self.label2["text"]="ISO : " + seltext
            print("Seltext = ", seltext)

        for row_index in range(2):
            Tk.Grid.rowconfigure(self.frame, row_index, weight=1)
        for col_index in range(4):
            Tk.Grid.columnconfigure(self.frame, col_index, weight=1)

        self.btn_back = Tk.Button(self.frame, text='Back', command=lambda: self.first_page(self.frame, self.controller)) #create a button inside frame
        self.btn_back.grid(row=0, column=0, padx=25, pady=25, sticky=Tk.N+Tk.W)
        self.btn_ok = Tk.Button(self.frame, text='OK', command=ok_button)
        self.btn_ok.grid(row=1, column=2, padx=25, pady=25, sticky=Tk.S+Tk.E)
        self.label = Tk.Label(self.frame, text="ISO Parameter")
        self.label.grid(row=0, column=1)
        self.label2 = Tk.Label(self.frame, text='ISO : ' )
        self.label2.grid(row=0, column=2)
        self.listbox = Tk.Listbox(self.frame)
        self.listbox.grid(row=1, column=1)

        for item in self.controller.get_iso():
            self.listbox.insert(Tk.END, item)

        self.listbox.bind("<<ListboxSelect>>", lambda _: printer(self, self.listbox, self.label2))


    def live_view_page(self):
        print "Live view selected"

        for widget in self.frame.winfo_children():
            widget.destroy()

        for row_index in range(2):
            Tk.Grid.rowconfigure(self.frame, row_index, weight=1)
        for col_index in range(4):
            Tk.Grid.columnconfigure(self.frame, col_index, weight=1)


        def shoot():
            # TODO: Put gphoto functions in controller
            
            img_path = self.controller.take_picture()
            image = Image.open(img_path)

            image = image.resize((495,315), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)
            label = Tk.Label(self.frame,image=photo,borderwidth=2,relief='solid')
            label.grid(row=3, column=3, pady= 25,padx= 25, rowspan=2,columnspan=2, sticky=Tk.S)
            label.image = photo # keep a reference!
            label.pack()

        btn_back = Tk.Button(self.frame, text='Back', command=lambda: self.first_page(self.frame, self.controller)) #create a button inside frame
        btn_back.grid(row=0, column=0, padx=25, pady=25, sticky=Tk.N+Tk.W)
        btn_ok = Tk.Button(self.frame, text='Previsualisation', command=shoot)
        btn_ok.grid(row=1, column=0, padx=25, pady=25, sticky=Tk.N+Tk.W)




    def run(self):
        self.root.mainloop()
