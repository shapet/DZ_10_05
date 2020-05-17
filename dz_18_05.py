fp = open('pars.txt', "r")

firefox = 0
with open('pars.txt', 'r') as f:
    for text in f:
        if 'Mozilla' in text :
            firefox += 1
print('Mozilla = ', firefox)

google = 0
with open('pars.txt', 'r') as f:
    for text in f:
        if 'Chrome' in text :
            google += 1
print('Chrome = ', google)

saf = 0
with open('pars.txt', 'r') as f:
    for text in f:
        if 'Safari' in text :
            saf += 1
print('Safari = ', saf)

get = 0
with open('pars.txt', 'r') as f:
    for text in f:
        if 'GET' in text :
            get += 1

print('Количество запросов = ', get)

import re
with open("C:\\Users\\smoke\Documents\\Python Scripts\\pars.txt","r") as file: 
    text1 = file.read()
Ip=re.findall(r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}',text1)
print('Количество IP адресов = ', len(Ip))
