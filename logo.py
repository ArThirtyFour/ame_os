from time import sleep
from colorama import Fore

logo = ''' 


    ▄▄▄       ███▄ ▄███▓▓█████     ▒█████    ██████ 
   ▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▒██    ▒ 
   ▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒░ ▓██▄   
   ░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒   ██▒
    ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░▒██████▒▒
    ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░
     ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░ ░ ░▒  ░ ░
     ░   ▒   ░      ░      ░      ░ ░ ░ ▒  ░  ░  ░  
         ░  ░       ░      ░  ░       ░ ░        ░  
                                                    
                                           
'''
def print_logo():
    for i in logo.split('\n'):
        sleep(0.05)
        print(Fore.LIGHTMAGENTA_EX+i,flush=True)