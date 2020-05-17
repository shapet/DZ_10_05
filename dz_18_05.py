fp = open('pars.txt', "r")

firefox = 0
with open('pars.txt', 'r') as f:
    for line in f:
        if 'Mozilla' in line :
            firefox += 1
firefox = str(firefox)
print('Mozilla = ', firefox)

google = 0
with open('pars.txt', 'r') as f:
    for line in f:
        if 'Chrome' in line :
            google += 1
google = str(google)
print('Chrome = ', google)

saf = 0
with open('pars.txt', 'r') as f:
    for line in f:
        if 'Safari' in line :
            saf += 1
saf = str(saf)
print('Safari = ', saf)