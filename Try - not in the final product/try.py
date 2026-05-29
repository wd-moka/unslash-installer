import subprocess
import json

forkOfDistros = DISTRO_FORKS_LIST = [  # i got that scipt online. its not mine
    {"distro": "Absolute Linux", "fork_of": "slackware"},
    {"distro": "AlmaLinux", "fork_of": "fedora"},
    {"distro": "Alpine Linux", "fork_of": "independent"},
    {"distro": "Amazon Linux 2023", "fork_of": "fedora"},
    {"distro": "AntiX", "fork_of": "debian"},
    {"distro": "Arch Linux", "fork_of": "arch"},
    {"distro": "Artix Linux", "fork_of": "arch"},
    {"distro": "BlackArch", "fork_of": "arch"},
    {"distro": "Calculate Linux", "fork_of": "gentoo"},
    {"distro": "CentOS Stream", "fork_of": "fedora"},
    {"distro": "Chapeau", "fork_of": "fedora"},
    {"distro": "Clear Linux", "fork_of": "independent"},
    {"distro": "Debian", "fork_of": "debian"},
    {"distro": "Deepin", "fork_of": "debian"},
    {"distro": "Devuan", "fork_of": "debian"},
    {"distro": "Elementary OS", "fork_of": "debian"},
    {"distro": "EndeavourOS", "fork_of": "arch"},
    {"distro": "Fedora", "fork_of": "fedora"},
    {"distro": "Garuda Linux", "fork_of": "arch"},
    {"distro": "GeckoLinux", "fork_of": "suse"},
    {"distro": "Gentoo", "fork_of": "gentoo"},
    {"distro": "Kali Linux", "fork_of": "debian"},
    {"distro": "KDE Neon", "fork_of": "debian"},
    {"distro": "Knoppix", "fork_of": "debian"},
    {"distro": "Korora", "fork_of": "fedora"},
    {"distro": "Kubuntu", "fork_of": "debian"},
    {"distro": "Leap", "fork_of": "suse"},
    {"distro": "Linux Mint", "fork_of": "debian"},
    {"distro": "Lubuntu", "fork_of": "debian"},
    {"distro": "LXLE", "fork_of": "debian"},
    {"distro": "Manjaro", "fork_of": "arch"},
    {"distro": "MX Linux", "fork_of": "debian"},
    {"distro": "NixOS", "fork_of": "independent"},
    {"distro": "Nobara Project", "fork_of": "fedora"},
    {"distro": "openSUSE", "fork_of": "suse"},
    {"distro": "Oracle Linux", "fork_of": "fedora"},
    {"distro": "Parrot OS", "fork_of": "debian"},
    {"distro": "Pop!_OS", "fork_of": "debian"},
    {"distro": "PureOS", "fork_of": "debian"},
    {"distro": "Raspberry Pi OS", "fork_of": "debian"},
    {"distro": "Red Hat Enterprise Linux (RHEL)", "fork_of": "fedora"},
    {"distro": "Redcore Linux", "fork_of": "gentoo"},
    {"distro": "Rocky Linux", "fork_of": "fedora"},
    {"distro": "Sabayon Linux", "fork_of": "gentoo"},
    {"distro": "Salix", "fork_of": "slackware"},
    {"distro": "Slax", "fork_of": "slackware"},
    {"distro": "Solus", "fork_of": "independent"},
    {"distro": "SteamOS 3.0+", "fork_of": "arch"},
    {"distro": "Tails", "fork_of": "debian"},
    {"distro": "Tumbleweed", "fork_of": "suse"},
    {"distro": "Ubuntu", "fork_of": "debian"},
    {"distro": "Ubuntu Budgie", "fork_of": "debian"},
    {"distro": "Ubuntu MATE", "fork_of": "debian"},
    {"distro": "Ubuntu Studio", "fork_of": "debian"},
    {"distro": "Ubuntu Unity", "fork_of": "debian"},
    {"distro": "Void Linux", "fork_of": "independent"},
    {"distro": "Xubuntu", "fork_of": "debian"},
    {"distro": "Zenwalk", "fork_of": "slackware"},
    {"distro": "Zorin OS", "fork_of": "debian"}
]

isAdavncedUsr = False #defult mode. can be checked in settings
isUsingArchBtw = False
currentDistro = None
mainDistro = None
line2 = None

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
    
    except():
        
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