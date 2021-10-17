def switch(windrichting):
    d = {'N':'Z', 'Z':'N', 'W':'O', 'O':'W'}
    return d[str(windrichting)]

def step(windrichting):
    d = {'N':(-1,0), 'Z':(1,0), 'W':(0,-1), 'O': (0,1)} # (rij,kolom)
    return d[str(windrichting)]

doorsnede = [['NZ', 'ZW', 'NZ', 'ZW', 'NW', 'NW', 'OW', 'ZW'], ['NZ', 'ZO', 'OW', 'ZW', 'OW', 'ZO', 'NZ', 'ZW'], ['NO', 'NW', 'NZ', 'NO', 'OW', 'OW', 'ZW', 'ZO'], ['NW', 'NO', 'ZO', 'OW', 'NW', 'NW', 'ZO', 'ZW']]  
r = 0
k = 0
diepte = 0
vak = doorsnede[r][k] #NZ
windrichting_uitgang = (vak).replace('N','') #Z
diepte = 1
doodlopend = False
while not doodlopend:
    r += step(windrichting_uitgang)[0]
    k += step(windrichting_uitgang)[1]
    if r in range(len(doorsnede)) and k in range(len(doorsnede[0])):
        vak = doorsnede[r][k]
        windrichting_ingang = switch(windrichting_uitgang)
        if windrichting_ingang in vak:
            windrichting_uitgang = (vak).replace(windrichting_ingang,'')
            diepte +=1
        else:
            doodlopend = True
    else: doodlopend = True
print(diepte)