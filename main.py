from Tkinter import *
from datetime import datetime, timedelta
from subprocess import call


#Create & Configure root 
root = Tk()
root.geometry('800x480')
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)

#Create & Configure frame 
frame=Frame(root)
frame.grid(row=0, column=0, sticky=N+S+E+W)

#Create a 5x10 (rows x columns) grid inside the frame
for row_index in range(2):
    Grid.rowconfigure(frame, row_index, weight=1)
    for col_index in range(3):
        Grid.columnconfigure(frame, col_index, weight=1)
        
        
        

def iso_button():

    
    
    def iso_ok():
        print(["gphoto2", "--set-config=/main/imgsettings/iso=", "seltext"])
        print("OKseltext : ", seltext)
        call(["echo", "gphoto2", "--set-config=/main/imgsettings/iso=", seltext])
        init_interface()
    
    
    def printer(event):
        print("SELECTED=",listbox.get(listbox.curselection()))
        index = listbox.curselection()[0]
        # get the line's text
        global seltext 
        seltext= listbox.get(index)
        label2["text"]="ISO : " + seltext
        print("Seltext = ", seltext)
    
        
    for widget in frame.winfo_children():
        widget.destroy()
        
    iso_list = ["100", "200", "400", "800", "1600", "3200"]
    listbox = Listbox(frame)
    listbox.grid(row=1, column=1)
    listbox.bind("<<ListboxSelect>>", printer)

    for item in iso_list:
        listbox.insert(END, item)
    btn_back = Button(frame, text='Back', command=init_interface) #create a button inside frame
    btn_back.grid(row=0, column=0, padx=25, pady=25, sticky=N+W) 
    btn_ok = Button(frame, text='OK', command=iso_ok)
    btn_ok.grid(row=1, column=2, padx=25, pady=25, sticky=S+E) 
    label = Label(frame, text="ISO Parameter")
    label.grid(row=0, column=1)
    label2 = Label(frame, text='ISO : ' )
    label2.grid(row=0, column=2)


def aperture_button():
    for widget in frame.winfo_children():
        widget.destroy()
    
    
    seltext = ""
    
    
    def printer(event):
        print("SELECTED=",listbox.get(listbox.curselection()))
        index = listbox.curselection()[0]
        # get the line's text
        seltext = listbox.get(index)
        label2["text"]="Aperture : " + seltext 
    
    label = Label(frame, text="Aperture Parameter")
    label.grid(row=0, column=1)
    btn_back = Button(frame, text='Back', command=init_interface) #create a button inside frame
    btn_back.grid(row=0, column=0, padx=25, pady=25, sticky=N+W) 
    btn_ok = Button(frame, text='OK', command=init_interface)
    btn_ok.grid(row=1, column=2, padx=25, pady=25, sticky=S+E) 
    
    iso_list = ["3.5" , "4", "5.6", "7"]
    listbox = Listbox(frame)
    listbox.grid(row=1, column=1)
    listbox.bind("<<ListboxSelect>>", printer)

    for item in iso_list:
        listbox.insert(END, item)
        
    label2 = Label(frame, text='Aperture : ' + seltext)
    label2.grid(row=0, column=2)
    
def runtest():
    call(["gphoto2", "-v"])
    


def init_interface():
    for widget in frame.winfo_children():
        widget.destroy()
    btn_iso = Button(frame, text='ISO', command=iso_button) #create a button inside frame
    btn_iso.grid(row=0, column=0, padx=25, pady=25, sticky=N+S+E+W)  
    btn_aper = Button(frame, text='Aperture', command=aperture_button) #create a button inside frame
    btn_aper.grid(row=0, column=1, padx=25, pady=25, sticky=N+S+E+W) 
    btn_speed = Button(frame, text='Speed') #create a button inside frame
    btn_speed.grid(row=0, column=2, padx=25, pady=25, sticky=N+S+E+W)  
    btn_inter = Button(frame, text='Intervall', command=runtest) #create a button inside frame
    btn_inter.grid(row=1, column=0, padx=25, pady=25, sticky=N+S+E+W) 
    btn_live = Button(frame, text='Live View') #create a button inside frame
    btn_live.grid(row=1, column=1, padx=25, pady=25, sticky=N+S+E+W)  
    btn_quit = Button(frame, text='Quit', command=quit) #create a button inside frame
    btn_quit.grid(row=1, column=2, padx=25, pady=25, sticky=N+S+E+W) 





        

init_interface()



#Run the GUI event loop
root.mainloop()

