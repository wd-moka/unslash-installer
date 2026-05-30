import subprocess
import json

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
        print("Error: Could not read /etc/os-release. Defaulting to independent.")
        mainDistro = "independent"
        pass

    pass


def create_gui():

    check_os()
    print(f"Current Distro: {currentDistro}")
    print(f"Main Distro: {mainDistro}")
    print(f"Is Using Arch: {isUsingArchBtw}")

    # start creating the gui here. tommorw

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

