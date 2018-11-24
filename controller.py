try:
    import Tkinter as Tk # python 2
except ModuleNotFoundError:
    import tkinter as Tk # python 3


from model import Model
import subprocess


class Controller:
    def __init__(self):

        self.model = Model()

    def hello(self):
        p = subprocess.Popen("ls", stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        print output
