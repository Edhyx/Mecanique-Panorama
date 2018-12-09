'''
    File name: view.py
    Author: Maxime FELICI, Meggan ESCARTEFIGUE, Mohamed Anis BEN MAHMOUD, Zeineb LAKNECH
    Python Version: 2.7
    This class manages the Human Machine Interface of the program.
'''


try: #Tkinter used for the interface
    import Tkinter as Tk # python 2
except ModuleNotFoundError:
    import tkinter as Tk # python 3

from model import Model
from controller import Controller
from PIL import Image, ImageTk  #PIL used to display pictures in liveView
import tkMessageBox
from intervall import Inter

class View:
    def __init__(self):
        print "Init view"
        self.root = Tk.Tk()
        self.root.geometry('800x480') #Dimensions of 7' Raspberry Pi screen
        Tk.Grid.rowconfigure(self.root, 0, weight=1)
        Tk.Grid.columnconfigure(self.root, 0, weight=1)
        self.frame = Tk.Frame(self.root)
        self.frame.grid(row=0, column=0, sticky=Tk.N+Tk.S+Tk.E+Tk.W)

        self.model = Model()
        self.controller = Controller(self.model)

        self.first_page(self.frame, self.controller) #Prints the menu page

    #This page shows the different selection buttons
    def first_page(self, frame, controller):
        for widget in self.frame.winfo_children():
            widget.destroy()


        self.Intervall_button = Tk.Button(self.frame)
        self.Intervall_button.place(relx=0.025, rely=0.063, height=175, width=175)
        self.Intervall_button.configure(activebackground="#d9d9d9")
        self.Intervall_button.configure(text='''Interval''', command=lambda: self.intervall_page(self.frame, self.controller))
        self.Intervall_button.configure(width=179)

        self.Iso_button = Tk.Button(self.frame)
        self.Iso_button.place(relx=0.269, rely=0.063, height=175, width=175)
        self.Iso_button.configure(activebackground="#d9d9d9")
        self.Iso_button.configure(text='''ISO''', command=lambda: self.iso_page(self.frame, self.controller))

        self.Aperture_button = Tk.Button(self.frame)
        self.Aperture_button.place(relx=0.513, rely=0.063, height=175, width=175)
        self.Aperture_button.configure(activebackground="#d9d9d9")
        self.Aperture_button.configure(text='''Aperture''', command=lambda: self.aperture_page(self.frame, self.controller))

        self.Liveview_button = Tk.Button(self.frame)
        self.Liveview_button.place(relx=0.756, rely=0.063, height=175, width=175)
        self.Liveview_button.configure(activebackground="#d9d9d9")
        self.Liveview_button.configure(text='''Live View''', command=self.live_view_page)

        self.Infos_button = Tk.Button(self.frame)
        self.Infos_button.place(relx=0.138, rely=0.563, height=175, width=175)
        self.Infos_button.configure(activebackground="#d9d9d9")
        self.Infos_button.configure(text='''Infos''', command=lambda: self.info_page(self.frame, self.controller))

        self.Start_button = Tk.Button(self.frame)
        self.Start_button.place(relx=0.388, rely=0.563, height=175, width=175)
        self.Start_button.configure(activebackground="#d9d9d9")
        self.Start_button.configure(background="#5dd88e")
        self.Start_button.configure(text='''START''', command=lambda: self.start(self.frame, self.controller))

        self.Quit_button = Tk.Button(self.frame)
        self.Quit_button.place(relx=0.638, rely=0.563, height=175, width=175)
        self.Quit_button.configure(activebackground="#d9d9d9")
        self.Quit_button.configure(background="#d85959")
        self.Quit_button.configure(text='''QUIT''', command=quit)


    #This page allows the selection of the ISO of the device
    def iso_page(self, frame, controller):
        for widget in frame.winfo_children():
                widget.destroy()

        def ok_button():
            print seltext
            controller.set_iso(seltext)
            self.first_page(self.frame, self.controller)

        def printer(event, listbox, label2):
            index = self.listbox.curselection()[0]
            global seltext # get the line's text
            seltext= self.listbox.get(index)
            self.label2["text"]="ISO : " + seltext
            print("ISO = ", seltext)

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


    #This page allows the selection of the Aperture of the device
    def aperture_page(self, frame, controller):
        for widget in frame.winfo_children():
                widget.destroy()

        def ok_button():
            print seltext
            controller.set_aperture(seltext)
            self.first_page(self.frame, self.controller)

        def printer(event, listbox, label2):
            index = self.listbox.curselection()[0] # get the line's text
            global seltext
            seltext= self.listbox.get(index)
            self.label2["text"]="APERTURE : " + seltext
            print("Aperture = ", seltext)


        for row_index in range(2):
            Tk.Grid.rowconfigure(self.frame, row_index, weight=1)
        for col_index in range(4):
            Tk.Grid.columnconfigure(self.frame, col_index, weight=1)

        self.btn_back = Tk.Button(self.frame, text='Back', command=lambda: self.first_page(self.frame, self.controller)) #create a button inside frame
        self.btn_back.grid(row=0, column=0, padx=25, pady=25, sticky=Tk.N+Tk.W)
        self.btn_ok = Tk.Button(self.frame, text='OK', command=ok_button)
        self.btn_ok.grid(row=1, column=2, padx=25, pady=25, sticky=Tk.S+Tk.E)
        self.label = Tk.Label(self.frame, text="Aperture Parameter")
        self.label.grid(row=0, column=1)
        self.label2 = Tk.Label(self.frame, text='APERTURE : ' )
        self.label2.grid(row=0, column=2)
        self.listbox = Tk.Listbox(self.frame)
        self.listbox.grid(row=1, column=1)

        for item in self.controller.get_aperture():
            self.listbox.insert(Tk.END, item)

        self.listbox.bind("<<ListboxSelect>>", lambda _: printer(self, self.listbox, self.label2))

    #This page allows you to take a preview.
    #It is possible to take several previews and to browse them.
    #These previews will be erased at the next launch of the program.
    def live_view_page(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        for row_index in range(2):
            Tk.Grid.rowconfigure(self.frame, row_index, weight=1)
        for col_index in range(4):
            Tk.Grid.columnconfigure(self.frame, col_index, weight=1)

        def show_picture(img_path):
            image = Image.open("tmp/" + img_path)
            image = image.resize((689,479), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)
            label.configure(image=photo)
            label.image = photo # keep a reference!
            label.place(relx=0.138, rely=0.0, height=479, width=689)

        def shoot():
            img_path = self.controller.take_picture()
            show_picture(img_path)

        def show_previous():
            img_path = self.model.get_live_view_previous_picture()
            if img_path != "":
                show_picture(img_path)

        def show_next():
            img_path = self.model.get_live_view_next_picture()
            print "selected img: " + img_path
            if img_path != "":
                show_picture(img_path)

        label = Tk.Label(self.frame, borderwidth=2) # ,relief='solid'
        label.grid(row=2, column=2, pady= 25,padx= 25, rowspan=2,columnspan=2, sticky=Tk.S)
        self.Button1 = Tk.Button(self.frame)
        self.Button1.place(relx=0.025, rely=0.771, height=30, width=80)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(text='''Previous''', command=show_previous)
        self.Button1.configure(width=74)

        self.Button2 = Tk.Button(self.frame)
        self.Button2.place(relx=0.025, rely=0.854, height=30, width=80)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(text='''Next''', command=show_next)
        self.Button2.configure(width=71)

        self.Button3 = Tk.Button(self.frame)
        self.Button3.place(relx=0.025, rely=0.042, height=30, width=80)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(text='''Back''', command=lambda: self.first_page(self.frame, self.controller))

        self.Button4 = Tk.Button(self.frame)
        self.Button4.place(relx=0.025, rely=0.688, height=30, width=80)
        self.Button4.configure(activebackground="#d9d9d9")
        self.Button4.configure(text='''Shoot''', command=shoot)

    def intervall_page(self, frame, controller):

        self.nbphotos = 0
        self.inter = Inter(0,0)

        def intervall_ok():
            self.inter.set_nbphotos(self.nbphotos)
            self.inter.set_inter(int(self.Spinbox_interval.get()))
            self.first_page(self.frame, self.controller)

        def calculation():
            self.nbphotos = (int(self.Spinbox1.get())*3600 + int(self.Spinbox1_2.get())*60 + int(self.Spinbox1_1.get()))/int(self.Spinbox_interval.get())
            text = "Nb Photos = " + str(self.nbphotos)
            self.Label7.configure(text = text)


        for widget in self.frame.winfo_children():
            widget.destroy()


        self.btn_back = Tk.Button(self.frame, text='Back', command=lambda: self.first_page(self.frame, self.controller)) #create a button inside frame
        self.btn_back.place(relx=0.025, rely=0.042, height=29, width=58)

        #HOURS
        self.Spinbox1 = Tk.Spinbox(self.frame, from_=1.0, to=100.0, command = calculation)
        self.Spinbox1.place(relx=0.238, rely=0.521, relheight=0.125, relwidth=0.075)
        self.Spinbox1.configure(activebackground="#f9f9f9")
        self.Spinbox1.configure(background="white")
        self.Spinbox1.configure(highlightbackground="black")
        self.Spinbox1.configure(justify='center')
        self.Spinbox1.configure(selectbackground="#c4c4c4")
        self.Spinbox1.configure(from_=0, to=48)
        self.Spinbox1.configure(width=48)

        #SEC0NDS
        self.Spinbox1_1 = Tk.Spinbox(self.frame, from_=1.0, to=100.0, command = calculation)
        self.Spinbox1_1.place(relx=0.563, rely=0.521, relheight=0.125, relwidth=0.075)
        self.Spinbox1_1.configure(activebackground="#f9f9f9")
        self.Spinbox1_1.configure(background="white")
        self.Spinbox1_1.configure(highlightbackground="black")
        self.Spinbox1_1.configure(justify='center')
        self.Spinbox1_1.configure(selectbackground="#c4c4c4")
        self.Spinbox1_1.configure(from_=0, to=60)

        #MINUTES
        self.Spinbox1_2 = Tk.Spinbox(self.frame, from_=1.0, to=100.0, command = calculation)
        self.Spinbox1_2.place(relx=0.388, rely=0.521, relheight=0.125, relwidth=0.075)
        self.Spinbox1_2.configure(activebackground="#f9f9f9")
        self.Spinbox1_2.configure(background="white")
        self.Spinbox1_2.configure(highlightbackground="black")
        self.Spinbox1_2.configure(justify='center')
        self.Spinbox1_2.configure(selectbackground="#c4c4c4")
        self.Spinbox1_2.configure(from_=0, to=60)

        self.Label1 = Tk.Label(self.frame)
        self.Label1.place(relx=0.325, rely=0.563, height=21, width=42)
        self.Label1.configure(text='''Hours''')

        self.Label2 = Tk.Label(self.frame)
        self.Label2.place(relx=0.475, rely=0.563, height=21, width=56)
        self.Label2.configure(text='''Minutes''')

        self.Label3 = Tk.Label(self.frame)
        self.Label3.place(relx=0.65, rely=0.563, height=21, width=58)
        self.Label3.configure(text='''Seconds''')

        self.ok_button = Tk.Button(self.frame)
        self.ok_button.place(relx=0.913, rely=0.917, height=29, width=45)
        self.ok_button.configure(activebackground="#d9d9d9", command=intervall_ok)
        self.ok_button.configure(text='''OK''')

        self.Label4 = Tk.Label(self.frame)
        self.Label4.place(relx=0.063, rely=0.542, height=41, width=128)
        self.Label4.configure(font='Helvetica 20 bold')
        self.Label4.configure(text='''Duration :''')
        self.Label4.configure(width=128)

        self.Label5 = Tk.Label(self.frame)
        self.Label5.place(relx=0.063, rely=0.292, height=41, width=128)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(font='Helvetica 20 bold')
        self.Label5.configure(justify='left')
        self.Label5.configure(text='''Interval :''')

        self.Label6 = Tk.Label(self.frame)
        self.Label6.place(relx=0.338, rely=0.313, height=21, width=58)
        self.Label6.configure(text='''Seconds''')

        self.Label7 = Tk.Label(self.frame)
        self.Label7.place(relx=0.063, rely=0.792, height=41, width=250)
        self.Label7.configure(activebackground="#f9f9f9")
        self.Label7.configure(font='Helvetica 20 bold')
        self.Label7.configure(justify='left')
        self.Label7.configure(text='''Nb Photos :''')

        #INTERVAL
        self.Spinbox_interval = Tk.Spinbox(self.frame, from_=1.0, to=100.0, command = calculation)
        self.Spinbox_interval.place(relx=0.238, rely=0.271, relheight=0.125, relwidth=0.075)
        self.Spinbox_interval.configure(activebackground="#f9f9f9")
        self.Spinbox_interval.configure(background="white")
        self.Spinbox_interval.configure(highlightbackground="black")
        self.Spinbox_interval.configure(justify='center')
        self.Spinbox_interval.configure(from_=3, to=300)

    def start(self, frame, controller):


        def start_subprocess():
            self.controller.start(self.inter, self.Label5)


        def stop_subprocess():
            self.controller.stop()
            self.first_page(self.frame, self.controller)

        for widget in self.frame.winfo_children():
            widget.destroy()
        self.frame.update_idletasks()



        self.Label5 = Tk.Label(self.frame)
        self.Label5.place(relx=0.063, rely=0.292, height=41, width=500)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(font='Helvetica 15 bold')
        self.Label5.configure(justify='left')
        self.Label5.configure(text="TEXT")
        self.Label5.update()

        self.Button1 = Tk.Button(self.frame)
        self.Button1.place(relx=0.438, rely=0.875, height=40, width=100)
        self.Button1.configure(activebackground="#d9d9d9", command = stop_subprocess)
        self.Button1.configure(background="#d80000")
        self.Button1.configure(font='Helvetica 15 bold')
        self.Button1.configure(text='''STOP''')
        self.Button1.update()



        print(self.inter.get_nbphotos())
        print(self.inter.get_inter())
        start_subprocess()


    def info_page(self, frame, controller):
        for widget in self.frame.winfo_children():
            widget.destroy()

        self.Label_info = Tk.Label(self.frame)
        self.Label_info.place(relx=0.138, rely=0.104, height=200, width=589)
        self.Label_info.configure(text = self.controller.get_info())

        self.Label_info2 = Tk.Label(self.frame)
        self.Label_info2.place(relx=0.138, rely=0.404, height=200, width=589)
        self.Label_info2.configure(text = "Mechanic-Panorama - Version 1.0")

        self.btn_back = Tk.Button(self.frame, text='Back', command=lambda: self.first_page(self.frame, self.controller)) #create a button inside frame
        self.btn_back.place(relx=0.025, rely=0.042, height=29, width=58)

    def run(self):
        self.root.mainloop()
