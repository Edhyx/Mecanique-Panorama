# Mecanique-Panorama

Mecanique Panorama is an interactive video installation. It reproduces 24h landscapes videos captured from windows of various cities inhabitants.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.



### How To Use

To clone and run this application, you'll need [Git](https://git-scm.com), [Python 2.7](https://www.python.org/download/releases/2.7/), Tkinter, PIL and [gPhoto 2](http://gphoto.org) installed on your computer.
We will use a script to install libgphoto2 and gphoto2.

 From your command line:

```bash
#First, update the system
$ sudo apt-get update

# Install associated libraries and dependencies for Gphoto2 to work
$ git clone https://github.com/gonzalo/gphoto2-updater.git
$ cd gphoto2-updater
$ sudo ./gphoto2-updater.sh
```

Then, in the script, type **1** then **ENTER**. It will install the latest dev version of libgphoto2 and gPhoto2.

Then we will install the dependencies for Python :

```bash
# Install Pillow (PIL)
$ sudo apt-get install python-imaging
$ sudo apt-get install python-imaging-tk

# Install Tkinter
$ pip install Tkinter

# Clone this repository
$ git clone https://github.com/Edhyx/Mechanique-Panorama

# Go into the repository
$ cd Mechanic-Panorama

# Run the application
$ python main.py
```

### System

* It is recommended to use a USB key with a capacity greater than or equal to 32GB.

* Your USB stick must be formatted in **FAT32** and be named exactly **"USBKEY"**.

### Compatibility

You can find the list of supported cameras [here](http://gphoto.org/proj/libgphoto2/support.php).

## Authors

* **Maxime FELICI**
* **Mohamed Anis BEN MAHMOUD**
* **Meggan ESCARTEFIGUE**
* **Zeineb LAKNECH**
