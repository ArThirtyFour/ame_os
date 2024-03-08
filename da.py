from time import sleep
from colorama import Fore
import os
from osss import get_os
from logo import print_logo
os.system('cls')
print(Fore.MAGENTA+'\n\n\n\nЗАПУСК ОС ПОЖАЛУЙСТА ПОДОЖДИТЕ',end='')
for _ in range(10,110,10):
    sleep(0.5)
    print(Fore.MAGENTA+f'. ',end='',flush=True)
sleep(5)
print_logo()
sleep(5)
while True:
    try:
        if 'exit' == get_os():
            os.system('cls')
            print(Fore.RESET+'')
            break
    except:
        pass
