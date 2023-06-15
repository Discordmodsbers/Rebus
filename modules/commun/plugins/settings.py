from colorama import Fore
import os, sys
import time as t
#---Colors---#

working = Fore.GREEN
warning = Fore.YELLOW
fail = Fore.RED
debug = Fore.BLUE
reset = Fore.RESET

#---Other color shits

y = Fore.LIGHTYELLOW_EX
b = Fore.LIGHTBLUE_EX
w = Fore.LIGHTWHITE_EX

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#---Misc functions---#

def cls():
    os.system('clear')
    
def setTitle(_str):
    system = os.name
    if system =='nt':
        ctypes.windll.kernel32.SetConsoleTitleW(f"{_str}")
    elif system =='posix':
        sys.stdout.write(f"\x1b]0;{_str}\x07")
    else:
        pass
    
def spinner():
    l = ['|', '/', '-', '\\']    
    for i in l+l+l:    
        sys.stdout.write(f"\r{y}[{b}#{y}]{w} Loading... {i}")
        sys.stdout.flush()
        t.sleep(0.2)    


def banner(colors):
    os.system("cls")
    if colors == True: 
        print(bcolors.HEADER + "#######" + bcolors.ENDC)
        print(bcolors.HEADER + "# SSM #" + bcolors.ENDC)
        print(bcolors.HEADER + "#######" + bcolors.ENDC)
    else:
        print("#######")
        print("# SSM #")
        print("#######")
    print(" ")
    print(" ")
    print(" ")


