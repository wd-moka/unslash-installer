import subprocess
import json
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import os as os
import sys as sys
import gi as gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk

forkOfDistrosRaw = DISTRO_FORKS_LIST = [
    {"distro": "absolute", "fork_of": "slackware"},
    {"distro": "almalinux", "fork_of": "fedora"},
    {"distro": "alpine", "fork_of": "independent"},
    {"distro": "amazon", "fork_of": "fedora"},
    {"distro": "antix", "fork_of": "debian"},
    {"distro": "arch", "fork_of": "arch"},
    {"distro": "artix", "fork_of": "arch"},
    {"distro": "blackarch", "fork_of": "arch"},
    {"distro": "calculate", "fork_of": "gentoo"},
    {"distro": "centos", "fork_of": "fedora"},
    {"distro": "chapeau", "fork_of": "fedora"},
    {"distro": "clear-linux-os", "fork_of": "independent"},
    {"distro": "debian", "fork_of": "debian"},
    {"distro": "deepin", "fork_of": "debian"},
    {"distro": "devuan", "fork_of": "debian"},
    {"distro": "elementary", "fork_of": "debian"},
    {"distro": "endeavouros", "fork_of": "arch"},
    {"distro": "fedora", "fork_of": "fedora"},
    {"distro": "garuda", "fork_of": "arch"},
    {"distro": "geckolinux", "fork_of": "suse"},
    {"distro": "gentoo", "fork_of": "gentoo"},
    {"distro": "kali", "fork_of": "debian"},
    {"distro": "neon", "fork_of": "debian"},
    {"distro": "knoppix", "fork_of": "debian"},
    {"distro": "korora", "fork_of": "fedora"},
    {"distro": "kubuntu", "fork_of": "debian"},
    {"distro": "opensuse-leap", "fork_of": "suse"},
    {"distro": "linuxmint", "fork_of": "debian"},
    {"distro": "lubuntu", "fork_of": "debian"},
    {"distro": "lxle", "fork_of": "debian"},
    {"distro": "manjaro", "fork_of": "arch"},
    {"distro": "mx", "fork_of": "debian"},
    {"distro": "nixos", "fork_of": "independent"},
    {"distro": "nobara", "fork_of": "fedora"},
    {"distro": "opensuse", "fork_of": "suse"},
    {"distro": "oracle", "fork_of": "fedora"},
    {"distro": "parrot", "fork_of": "debian"},
    {"distro": "pop", "fork_of": "debian"},
    {"distro": "pureos", "fork_of": "debian"},
    {"distro": "raspbian", "fork_of": "debian"},
    {"distro": "rhel", "fork_of": "fedora"},
    {"distro": "redcore", "fork_of": "gentoo"},
    {"distro": "rocky", "fork_of": "fedora"},
    {"distro": "sabayon", "fork_of": "gentoo"},
    {"distro": "salix", "fork_of": "slackware"},
    {"distro": "slax", "fork_of": "slackware"},
    {"distro": "solus", "fork_of": "independent"},
    {"distro": "steamos", "fork_of": "arch"},
    {"distro": "tails", "fork_of": "debian"},
    {"distro": "opensuse-tumbleweed", "fork_of": "suse"},
    {"distro": "ubuntu", "fork_of": "debian"},
    {"distro": "ubuntu-budgie", "fork_of": "debian"},
    {"distro": "ubuntu-mate", "fork_of": "debian"},
    {"distro": "ubuntu-studio", "fork_of": "debian"},
    {"distro": "ubuntu-unity", "fork_of": "debian"},
    {"distro": "void", "fork_of": "independent"},
    {"distro": "xubuntu", "fork_of": "debian"},
    {"distro": "zenwalk", "fork_of": "slackware"},
    {"distro": "zorin", "fork_of": "debian"}
]

for item in forkOfDistrosRaw:
    item['distro'] = item['distro'].lower()
    item['fork_of'] = item['fork_of'].lower()
pass

forkOfDistros = forkOfDistrosRaw

isAdavncedUsr = False #defult mode. can be checked in settings
isUsingArchBtw = False
currentDistro = None
mainDistro = None
line2 = None
protocol = None


def check_os():
    global isUsingArchBtw
    global currentDistro
    global mainDistro
    global forkOfDistros

    try:
        with open('/etc/os-release' , 'r') as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                line = line.lower()
                if 'id=' in line and not line.startswith('version_id='):
                    line2 = line.split('=')[1].strip('"')
                    currentDistro = line2
                    
                    found_match = False
                    for item in forkOfDistros:
                        if item['distro'].lower() == line2:
                            mainDistro = item['fork_of']
                            found_match = True
                            break
                    
                    if not found_match:
                        mainDistro = "independent"
                        
                    if mainDistro == 'arch':
                        isUsingArchBtw = True
                        
                    break
            pass
    
    except:
        print("Error: Could not read /etc/os-release. Defaulting to independent.")
        mainDistro = "independent"
        pass

    pass


def check_xdg():
    global protocol
    #check if user use x11 or wayland,

    if 'WAYLAND_DISPLAY' in os.environ:
        protocol = 'wayland'
    elif 'DISPLAY' in os.environ:
        protocol = 'x11'
    else:
        protocol = 'x11' #default to x11 if unknown

    pass


def create_gui():
    global protocol
    check_os()
    check_xdg()
    print(f"Current Distro: {currentDistro}")
    print(f"Main Distro: {mainDistro}")
    print(f"Is Using Arch: {isUsingArchBtw}")
    print(f"Protocol: {protocol}")

    if protocol == 'wayland':
        print("User is using Wayland. using GI")
        # basic gui setup
        app = Gtk.Application(application_id="com.unslash.installer")
        def on_activate(app):
            win = Gtk.ApplicationWindow(application=app)
            win.set_title("Unslash - Installer")
            win.set_default_size(400, 500)
            win.present()
        app.connect("activate", on_activate)
        app.run(None)
        pass

    elif protocol == 'x11':
        print("User is using X11. using customtkinter")
        # basic gui setup
        root = ctk.CTk()
        root.title("Unslash - Installer")
        root.geometry('400x500')
        root.mainloop()
        pass

    else:
        print("Unknown protocol. Defaulting to customtkinter.")
        root = ctk.CTk()
        root.title("Unslash - Installer")
        root.geometry('400x500')
        root.mainloop()
        pass
pass


def check_cartogory():
    pass

def check_source():
    pass

def check_package():

    if (isAdavncedUsr):

        # show package info

        pass
    pass

def install_package():
    pass

create_gui()