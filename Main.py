'''
Created on 29 nov. 2018

@author: zeineb
'''
from Tkinter import *
import Tkinter as tk
from datetime import datetime, timedelta
import subprocess
import tkMessageBox
from Param import Param 
from time import sleep
import time
import datetime as dt
from subprocess import call


#Create & Configure root
root = Tk()
root.geometry('800x480')
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)

#Create & Configure frame
frame=Frame(root)
frame.grid(row=0, column=0, sticky=N+S+E+W)

param=Param(0,0)
#Create a 5x10 (rows x columns) grid inside the frame
for row_index in range(2):
    Grid.rowconfigure(frame, row_index, weight=1)
    for col_index in range(4):
        Grid.columnconfigure(frame, col_index, weight=1)


def iso_button():

    def iso_ok():
        command = "gphoto2 --set-config=/main/imgsettings/iso=" + seltext
        p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        init_interface()


    def printer(event):
        print("SELECTED=",listbox.get(listbox.curselection()))
        index = listbox.curselection()[0]
        # get the line's text
        global seltext
        seltext= listbox.get(index)
        param.set_iso(seltext)
        label2["text"]="ISO : " + seltext
        print("Seltext = ", seltext)
        print("Value in object", param.get_iso())


    for widget in frame.winfo_children():
        widget.destroy()
    iso_list = []
    p = subprocess.Popen("gphoto2 --get-config=/main/imgsettings/iso", stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    end_line = output.find("END")
    choice_line = output.find("Choice")
    sub_chain = output[choice_line:end_line]
    print("sub chain : " + sub_chain)

    while len(sub_chain)>10:
        sub_chain=sub_chain[sub_chain.find(" ")+1:len(sub_chain)]
        sub_chain=sub_chain[sub_chain.find(" ")+1:len(sub_chain)]
        iso = sub_chain[0:sub_chain.find("\n")]
        sub_chain = sub_chain[sub_chain.find("\n")+1:len(sub_chain)]
        try:
            if int(iso)>51200:
                break
        except ValueError : print("")
        iso_list.append(iso)

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
        param.set_app(seltext)
        label2["text"]="Aperture : " + seltext
        print("Value in object", param.get_app())

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

def info_button():
    for widget in frame.winfo_children():
        widget.destroy()
    btn_back = Button(frame, text='Back', command=init_interface) #create a button inside frame
    btn_back.grid(row=0, column=0, padx=25, pady=25, sticky=N+W)


    p = subprocess.Popen("gphoto2 --auto-detect", stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()

    ## Wait for gphoto2 to terminate. Get return returncode ##
    p_status = p.wait()
    print "Command output : ", output
    print "Command exit status/return code : ", p_status
    label = Label(frame, text=output)
    label.grid(row=0, column=1)

def intervall_button():

    def intervall_ok():
        init_interface()

    for widget in frame.winfo_children():
        widget.destroy()
    btn_back = Button(frame, text='Back', command=init_interface) #create a button inside frame
    btn_back.place(relx=0.025, rely=0.042, height=29, width=58)

    Spinbox1 = tk.Spinbox(frame, from_=1.0, to=100.0)
    Spinbox1.place(relx=0.238, rely=0.521, relheight=0.125
                , relwidth=0.075)
    Spinbox1.configure(activebackground="#f9f9f9")
    Spinbox1.configure(background="white")
    Spinbox1.configure(highlightbackground="black")
    Spinbox1.configure(justify='center')
    Spinbox1.configure(selectbackground="#c4c4c4")
    Spinbox1.configure(from_=0, to=24)
    Spinbox1.configure(width=48)

    Spinbox1_1 = tk.Spinbox(frame, from_=1.0, to=100.0)
    Spinbox1_1.place(relx=0.563, rely=0.521, relheight=0.125
                , relwidth=0.075)
    Spinbox1_1.configure(activebackground="#f9f9f9")
    Spinbox1_1.configure(background="white")
    Spinbox1_1.configure(highlightbackground="black")
    Spinbox1_1.configure(justify='center')
    Spinbox1_1.configure(selectbackground="#c4c4c4")
    Spinbox1_1.configure(from_=0, to=60)

    Spinbox1_2 = tk.Spinbox(frame, from_=1.0, to=100.0)
    Spinbox1_2.place(relx=0.388, rely=0.521, relheight=0.125
                , relwidth=0.075)
    Spinbox1_2.configure(activebackground="#f9f9f9")
    Spinbox1_2.configure(background="white")
    Spinbox1_2.configure(highlightbackground="black")
    Spinbox1_2.configure(justify='center')
    Spinbox1_2.configure(selectbackground="#c4c4c4")
    Spinbox1_2.configure(from_=0, to=60)

    Label1 = tk.Label(frame)
    Label1.place(relx=0.325, rely=0.563, height=21, width=42)
    Label1.configure(text='''Hours''')

    Label2 = tk.Label(frame)
    Label2.place(relx=0.475, rely=0.563, height=21, width=56)
    Label2.configure(text='''Minutes''')

    Label3 = tk.Label(frame)
    Label3.place(relx=0.65, rely=0.563, height=21, width=58)
    Label3.configure(text='''Seconds''')

    ok_button = tk.Button(frame)
    ok_button.place(relx=0.913, rely=0.917, height=29, width=45)
    ok_button.configure(activebackground="#d9d9d9")
    ok_button.configure(text='''OK''')
    ok_button.configure(command=intervall_ok)

    Label4 = tk.Label(frame)
    Label4.place(relx=0.063, rely=0.542, height=41, width=128)
    Label4.configure(font='Helvetica 20 bold')
    Label4.configure(text='''Duration :''')
    Label4.configure(width=128)

    Label5 = tk.Label(frame)
    Label5.place(relx=0.063, rely=0.292, height=41, width=128)
    Label5.configure(activebackground="#f9f9f9")
    Label5.configure(font='Helvetica 20 bold')
    Label5.configure(justify='left')
    Label5.configure(text='''Interval :''')

    Spinbox_interval = tk.Spinbox(frame, from_=1.0, to=100.0)
    Spinbox_interval.place(relx=0.238, rely=0.271, relheight=0.125
            , relwidth=0.075)
    Spinbox_interval.configure(activebackground="#f9f9f9")
    Spinbox_interval.configure(background="white")
    Spinbox_interval.configure(highlightbackground="black")
    Spinbox_interval.configure(justify='center')
    Spinbox_interval.configure(from_=0, to=300)

    Label6 = tk.Label(frame)
    Label6.place(relx=0.338, rely=0.313, height=21, width=58)
    Label6.configure(text='''Seconds''')
    
class ElapsedTimeClock(Label):
    def __init__(self, parent, *args, **kwargs):
        time.sleep(1)
        Label.__init__(self, parent, *args, **kwargs)
        self.lastTime = ""
        t = time.localtime()
        self.zeroTime = dt.timedelta(hours=t[3], minutes=t[4], seconds=t[5])
        self.tick()
        
    def tick(self):
        done = True        
# get the current local time from the PC
        now = dt.datetime(1, 1, 1).now()
        elapsedTime = now - self.zeroTime
        if elapsedTime.hour == 23 and elapsedTime.minute == 59 and elapsedTime.second == 59 :
            done  = False
        time2 = elapsedTime.strftime('%H:%M:%S')
        # if time string has changed, update it
        if time2 != self.lastTime:
            self.lastTime = time2
            self.config(text=time2)
        if done:
                self.after(200, self.tick)

    
def capture_image():
    getPhotos = True
    totalPhotos = input("Enter number of photos: ")
    currentPhotoCount = 0
    while(getPhotos):
        if (currentPhotoCount < totalPhotos):
            call(["gphoto2","--capture-image-and-download","--filename","/home/pi/camera/photo-%Y%m%d-%H%M%S.jpg"])
            print("Current Photos: %s Total Photos: %s" %(currentPhotoCount, totalPhotos))
            sleep(10)
            currentPhotoCount += 1
        else:
            getPhotos = False
            print("Time Lapse Finished")
            call(["gphoto2", "--get-all-files"])
            print("Photos Downloaded")
    root = Tk()
    clock = ElapsedTimeClock(root, font=('times', 20, 'bold'), bg='green')
    clock.pack(fill=BOTH, expand=1)        
               
def start_button():
    msg = "iso: " + str(param.get_iso()) + " app : " + str(param.get_app())
    if tkMessageBox.askokcancel("resume", msg):
        capture_image()

     
      
def init_interface():
    for widget in frame.winfo_children(): 
        widget.destroy()
    btn_iso = Button(frame, text='ISO', command=iso_button) #create a button inside frame
    btn_iso.grid(row=0, column=0, padx=25, pady=25, sticky=N+S+E+W)
    btn_aper = Button(frame, text='Aperture', command=aperture_button) #create a button inside frame
    btn_aper.grid(row=0, column=1, padx=25, pady=25, sticky=N+S+E+W)
    btn_speed = Button(frame, text='Speed') #create a button inside frame
    btn_speed.grid(row=0, column=2, padx=25, pady=25, sticky=N+S+E+W)
    btn_inter = Button(frame, text='Intervall', command=intervall_button) #create a button inside frame
    btn_inter.grid(row=1, column=0, padx=25, pady=25, sticky=N+S+E+W)
    btn_live = Button(frame, text='Live View') #create a button inside frame
    btn_live.grid(row=1, column=1, padx=25, pady=25, sticky=N+S+E+W)
    btn_quit = Button(frame, text='Quit', command=quit) #create a button inside frame
    btn_quit.grid(row=1, column=2, padx=25, pady=25, sticky=N+S+E+W)
    btn_info = Button(frame, text='Infos', command=info_button) #create a button inside frame
    btn_info.grid(row=0, column=3, padx=25, pady=25, sticky=N+S+E+W)
    btn_ = Button(frame, text='Start',command=start_button) #create a button inside frame
    btn_.grid(row=1, column=3, padx=25, pady=25, sticky=N+S+E+W)




init_interface()


#Run the GUI event loop
root.mainloop()