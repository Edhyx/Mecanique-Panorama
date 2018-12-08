# Mechanic-Panorama

Mechanic Panorama is an interactive video installation. It reproduces 24h landscapes videos captured from windows of various cities inhabitants.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Compile Gphoto2 and libphoto2 from sources

**WARNING !!!**

We proposed a modification of gphoto2 sources using a fork on Github, in order to make the software completely compatible with our camera, the Sony Alpha 6300. However, the compiled archive is not yet available on the developer's website. We will show you how to compile the sources of libgphoto2. Once the compiled archive of libgphoto2 version 2.5.21 or higher is available, it will no longer be necessary to perform this operation.

For autoreconf to succeed, you require the following tools:

	automake
	autoconf
	pkg-config (to detect additional library dependencies)
	autopoint (needed if installing from github)
	gettext  (possibly from -dev or -devel package)
	libtool  (possibly from -dev or -devel package)

in versions compatible with each other and with libgphoto2. Most
combinations on current GNU/Linux systems work, whereas BSD systems tend to have some compatibility problems.

```bash
#First, clone libgphoto2
$ git clone https://github.com/gphoto/libgphoto2.git

#Then start the compilation
$ autoreconf --install --symlink
$ ./configure --prefix=/usr/local
$ make
$ make install
```


### How To Use

To clone and run this application, you'll need [Git](https://git-scm.com), [Python 2.7](https://www.python.org/download/releases/2.7/), Tkinter, PIL and [gPhoto 2](http://gphoto.org) installed on your computer.
You can find a tutorial for this installation of gPhoto 2 on a Raspberry Pi [here](https://medium.com/@cgulabrani/controlling-your-dslr-through-raspberry-pi-ad4896f5e225).

 From your command line:

```bash
#First, update the system
$ sudo apt-get update

# Install associated libraries and dependencies for Gphoto2 to work
$ sudo apt-get install libltdl-dev libusb-dev libexif-dev libpopt-dev

# Install libusb
$ wget http://ftp.de.debian.org/debian/pool/main/libu/libusbx/libusbx_1.0.11.orig.tar.bz2
$ tar xjvf libusbx_1.0.11.orig.tar.bz2
$ cd libusbx-1.0.11/
$ ./configure
$ make
$ sudo make install
$ cd..


# Install gphoto2
$ wget http://downloads.sourceforge.net/project/gphoto/gphoto/2.5.2/gphoto2-2.5.2.tar.bz2
$ tar xjvf gphoto2–2.5.2.tar.bz2
$ cd gphoto2–2.5.2/
$ ./configure
$ make
$ sudo make install
$ cd..

# Install Pillow (PIL)
$ pip install Pillow

# Or use easy_install to install Pillow
$ easy_install Pillow

# Install Tkinter
$ pip install Tkinter

# Clone this repository
$ git clone https://github.com/Edhyx/Mechanic-Panorama

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
