import math
getal_input = input()
getal = getal_input
x = 0
y = 0

if '.' in getal:
    getal = getal.replace('.', '')

for cijfer in getal:
    t = int(cijfer) * math.radians(36)
    x += math.sin(t)
    y += math.cos(t)
print('Getal {} wandelt naar positie ({:.2f}, {:.2f}).'.format(getal_input,x,y))
    