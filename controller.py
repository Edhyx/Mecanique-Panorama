# -*- coding: utf-8 -*-
'''

    File name: controller.py
    Author: Maxime FELICI, Meggan ESCARTEFIGUE, Mohamed Anis BEN MAHMOUD, Zeineb LAKNECH
    Python Version: 2.7
    This class handles calls to the gphoto2 software
'''


try:
    import Tkinter as Tk # python 2
except ModuleNotFoundError:
    import tkinter as Tk # python 3

import subprocess
from os import listdir
from intervall import Inter
import time
import os

after_id = None
compt = 0

class Controller:
    output = ""

    def __init__(self, model):
        self.model = model
        p = subprocess.Popen("rm -Rf tmp", stdout=subprocess.PIPE, shell=True) #Delete tmp directory
        (output, err) = p.communicate()
        p = subprocess.Popen("mkdir tmp", stdout=subprocess.PIPE, shell=True) #Create empty tmp directory
        (output, err) = p.communicate()
        self.default_tmp_path = "tmp/" #TODO change with temp dir on Linux like /tmp

    def get_iso(self):
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

        print iso_list
        return iso_list

    def set_iso(self, selected_iso):
        command = "gphoto2 --set-config=/main/imgsettings/iso=" + selected_iso
        p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()


    def get_aperture(self):
        p = subprocess.Popen("gphoto2 --get-config /main/status/cameramodel", stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()

        print output
        index = output.find('ILCE-6300')
        if index == -1:
            aperture_list = []
            p = subprocess.Popen("gphoto2 --get-config=/main/capturesettings/f-number", stdout=subprocess.PIPE, shell=True)
            (output, err) = p.communicate()

            end_line = output.find("END")
            choice_line = output.find("Choice")
            sub_chain = output[choice_line:end_line]
            print("sub chain : " + sub_chain)

            while len(sub_chain)>10:
                sub_chain=sub_chain[sub_chain.find(" ")+1:len(sub_chain)]
                sub_chain=sub_chain[sub_chain.find(" ")+1:len(sub_chain)]
                aperture = sub_chain[0:sub_chain.find("\n")]
                sub_chain = sub_chain[sub_chain.find("\n")+1:len(sub_chain)]
                aperture_list.append(aperture)

            print aperture_list
            return aperture_list
        else:
            aperture_list=["3,5", "4", "5", "5,6", "6,3", "7,1", "8","9","10","11", "13", "14", "16", "18", "20", "22"]
            return aperture_list





    def set_aperture(self, selected_aperture):
        command = "gphoto2 --set-config=/main/capturesettings/f-number=" + selected_aperture
        p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()

    def refresh_live_view_pictures(self, dir):
        if self.model != None:
            allfiles = listdir(dir)
            imgfiles = []

            print allfiles

            for file in allfiles:
                if file.lower().endswith('.png') or file.lower().endswith('.jpg'):
                    imgfiles.append(file)
            self.model.set_live_view_pictures(imgfiles)
            print imgfiles

    def take_picture(self):
        #TODO: set the output file
        #TODO: temp dir: self.default_tmp_path+"/img1.jpg"
        cmd = "gphoto2 --capture-image-and-download --filename tmp/"
        allfiles = listdir(self.default_tmp_path)
        imgfiles = []
        print allfiles
        for file in allfiles:
            if file.lower().endswith('.png') or file.lower().endswith('.jpg'):
                imgfiles.append(file)
        nb = len(imgfiles)
        cmd = cmd + str(nb+1) + ".png"
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        self.refresh_live_view_pictures(self.default_tmp_path)
        rtrn = str(nb+1) + ".png"
        return rtrn #TODO: return the name

    def start(self, inter, label, root, label_text):

        # var = Tk.StringVar()
        # label.configure(textvariable=var)

        def shoot():
            start = time.time()
            global compt
            global after_id
            compt += 1
            textlabel = "Photo " + str(compt) + "/" + str(inter.get_nbphotos())
            label_text.set(textlabel)
            label.update()
            filename = str(compt)
            filename = filename.zfill(5)
            print "filename = " + filename
            cmd = "gphoto2 --capture-image-and-download --filename /media/pi/USBKEY/MCphotos/" + str(foldername) + "/" + filename + ".png"
            print cmd
            p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
            (output, err) = p.communicate()

            elapsed = time.time() - start
            print elapsed
            time_inter = inter.get_inter()
            if elapsed < time_inter:
                diff = int((time_inter - elapsed)*1000)
                after_id = root.after(diff, shoot)
            else:
                after_id = root.after(0, shoot)
            if compt >= inter.get_nbphotos():
                self.stop(root)






        #create new dir in USBKEY if necessary
        p = subprocess.Popen("mkdir /media/pi/USBKEY/MCphotos", stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()

        p = subprocess.Popen("ls /media/pi/USBKEY/MCphotos/ | wc -l", stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        foldername = int(output) + 1
        print "FOLDERNAME "
        print foldername

        cmd = "mkdir /media/pi/USBKEY/MCphotos/" + str(foldername)
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()

        shoot()

        # for x in range(0, inter.get_nbphotos()):
            # filename = str(x)
            # filename = filename.zfill(5)
            # print "filename = " + filename
            # cmd = "gphoto2 --capture-image-and-download --filename /Users/maxime/Desktop/MCphotos/" + str(foldername) + "/" + filename + ".png"
            # print cmd
            # p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
            # (output, err) = p.communicate()
            # label.configure(text = output)
            # label.update()
            # while True:
            #     output = p.stdout.readline()
            #     if output == '' and p.poll() is not None:
            #         break
            #     if output:
            #         print output.strip()
            #         label.configure(text = output)
            #         label.update()



        # cmd = "gphoto2 --capture-image-and-download --filename /Volumes/USBKEY/MCphotos/" + str(foldername) + "/%05n.png -F " + str(inter.get_nbphotos()) + " -I " + str(inter.get_inter())
        # print cmd
        # p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        # while True:
        #     output = p.stdout.readline()
        #     if output == '' and p.poll() is not None:
        #         break
        #     if output:
        #         print output.strip()
        #         label.configure(text = output)
        #         label.update()

    def stop(self, root):
        global after_id
        if after_id:
            root.after_cancel(after_id)
            after_id = None
        # kill = subprocess.Popen("pkill -f gphoto2", stdout=subprocess.PIPE, shell=True)
        # (output, err) = kill.communicate()


    def get_info(self):
        p = subprocess.Popen("gphoto2 --auto-detect", stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        return output
