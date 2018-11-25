try:
    import Tkinter as Tk # python 2
except ModuleNotFoundError:
    import tkinter as Tk # python 3

import subprocess
from os import listdir


class Controller:
    def __init__(self, model):

        self.model = model
        self.default_tmp_path = "." #TODO change with temp dir on Linux like /tmp

    def hello(self):
        p = subprocess.Popen("ls", stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        print output

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

    def aperture_function(self):
        pass

    def inter_function(self):
        pass

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

        p = subprocess.Popen("gphoto2 --capture-image-and-download -file %H%M%S", stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()

        self.refresh_live_view_pictures(self.default_tmp_path)

        return 'C:/Users/megga/Desktop/IMG_Test.JPG' #TODO: return the file path

    def info_function(self):
        pass
