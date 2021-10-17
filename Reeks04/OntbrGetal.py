invoer = input()
gevonden = False
aantal_plus_2 = 0
a = int(invoer[0])
l = 1
rest = invoer[1:]
ontbr_getal = 'nope'

while not gevonden and len(rest) > 0:
    while rest.startswith(str(a+1)):
        rest = rest[(len(str(a+1))):]
        a += 1
        
    while rest.startswith(str(a+2)) and aantal_plus_2 <= 1:
        rest = rest[(len(str(a+2))):]
        ontbr_getal = a+1
        a += 2
        aantal_plus_2 += 1
        
    if aantal_plus_2 <= 1 and (not (rest.startswith(str(a+1))) or not (rest.startswith(str(a+2)))):
        l += 1
        a = int(invoer[0:l])
        #aantal_plus_2 = 0
        rest = invoer[l:]
    if aantal_plus_2 > 1:
        gevonden = True
        ontbr_getal ='nope'

if ontbr_getal != 'nope':
    print(ontbr_getal)
else: print('geen ontbrekend getal')
