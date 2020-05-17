fp = open('pars.txt', "r")

firefox = 0
with open('pars.txt', 'r') as f:
    for text in f:
        if 'Mozilla' in text :
            firefox += 1
firefox = str(firefox)
print('Mozilla = ', firefox)

google = 0
with open('pars.txt', 'r') as f:
    for text in f:
        if 'Chrome' in text :
            google += 1
google = str(google)
print('Chrome = ', google)

saf = 0
with open('pars.txt', 'r') as f:
    for text in f:
        if 'Safari' in text :
            saf += 1
saf = str(saf)
print('Safari = ', saf)