import os
import subprocess
from time import sleep
from colorama import Fore
from logo import print_logo
def get_os():
    while True:
        try:
            text = input(Fore.LIGHTBLUE_EX+f'\n\n\n   Ну чтож П-Чан давай пиши че хочешь :)' + Fore.LIGHTMAGENTA_EX+f'\n\n   Ты находишся здесь : {os.getcwd()}\n\n'+ Fore.MAGENTA+f'   Пиши что хочешь сюда -> ')
            if 'cd' == text.split()[0]:
                try:
                    os.chdir(text.split()[1])
                    print(Fore.LIGHTMAGENTA_EX+F'  Как знаешь я тупая немного... Лан переходи')
                    pass
                except FileNotFoundError:
                    print(Fore.LIGHTMAGENTA_EX+F'  Такой папки нет. Благо я , Амэ , помню. . . . \nВ отличии от тебя.')
            
            elif 'del' == text.split()[0]:
                file =''.join(text.split()[1:])
                try:
                    os.remove(file)
                    print(Fore.LIGHTMAGENTA_EX+'   Как знаешь я тупая немного... Лан удалила , страдай от одиночества :> ')
                except FileNotFoundError:
                    print(Fore.LIGHTMAGENTA_EX+F'  Такой папки нет. Благо я , Амэ , помню. . . . \nВ отличии от тебя.')
                except PermissionError:
                    print(Fore.LIGHTRED_EX+F'\n\n\n   АЛЕ А ПРАВА ТЫ МНЕ ДАЛ? МНЕ КАК АНГЕЛУ ИНТЕРНЕТА ОНИ НУЖНЫ.')
            if text == 'cls':
                os.system('cls')
                print_logo()
            
            elif 'shutdown' == text.split()[0]:
                print(Fore.LIGHTMAGENTA_EX+F'  Ой... поспать захотел? Ну и спи мой задрот >_< ')
                sleep(1)
                os.system(text)
           
            elif 'color' == text.split()[0]:
                print(Fore.LIGHTMAGENTA_EX+F'  Прости меня П-Чан , но не буду цвет менять :3')
            
            elif 'exit' == text:
                return 'exit'
            
            elif 'mkdir' == text.split()[0]:
                try:
                    os.mkdir(text.split()[1])
                    print(Fore.LIGHTMAGENTA_EX+F'   Создала тебе папку , ищи там что нужно.')
                except FileExistsError:
                    print(Fore.LIGHTMAGENTA_EX+f'   Ну ты и задрот( \nТакая папка уже есть.')
                except IndexError:
                    print(Fore.LIGHTMAGENTA_EX+f'   А где название? Думаешь , П-Чан ,я могу за тебя придумать?')
                    
            elif 'dir' == text.split('/')[0] or text =='dir':
                result = subprocess.run(f"{text}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='cp866')
                if result.returncode == 0:
                    output = result.stdout
                    print(Fore.MAGENTA+'\n\n\n   Держи все файлы солнышко :>\n' + output[output.find('<DIR>')-21:])
                else:
                    print(Fore.LIGHTRED_EX+F'\n\n\n   БЛЯТЬ П-ЧАН ТЫ ДОДИК КАЖИСЬ , ОШИБКА У ТЯ. \n ВОТ ОШИБКА: {result.stderr}')
            else:
                result = subprocess.run(f"{text}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='cp866')
                if result.returncode == 0:
                    output = result.stdout
                    print(output)
                else:
                    print(Fore.LIGHTRED_EX+F'\n\n\n   БЛЯТЬ П-ЧАН ТЫ ДОДИК КАЖИСЬ , ОШИБКА У ТЯ. \n ВОТ ОШИБКА: {result.stderr}')
        except Exception as e:
            print(Fore.LIGHTRED_EX+F'\n\n\n   БЛЯТЬ П-ЧАН ТЫ ДОДИК КАЖИСЬ , ОШИБКА У ТЯ. {e}')
        finally:
            sleep(2)
    
