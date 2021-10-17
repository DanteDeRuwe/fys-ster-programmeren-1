
def dwarsdoorsnede(r, gangen):
    """
    >>> dwarsdoorsnede(4, 'NZZWNZZWNWNWOWZWNZZOOWZWOWZONZZWNONWNZNOOWOWZWZONWNOZOOWNWNWZOZW')
    [['NZ', 'ZW', 'NZ', 'ZW', 'NW', 'NW', 'OW', 'ZW'], ['NZ', 'ZO', 'OW', 'ZW', 'OW', 'ZO', 'NZ', 'ZW'], ['NO', 'NW', 'NZ', 'NO', 'OW', 'OW', 'ZW', 'ZO'], ['NW', 'NO', 'ZO', 'OW', 'NW', 'NW', 'ZO', 'ZW']]
    >>> dwarsdoorsnede(4, 'NZZWNZZWNWNWOWZWNZZ')
    Traceback (most recent call last):
    AssertionError: ongeldige dwarsdoorsnede
    """
    assert len(gangen) % (2*r) == 0, "ongeldige dwarsdoorsnede"
    k = int(len(gangen) // (2*r)) #ook gedeeld door 2 want 2 letters per coordinaat
    lijst = []
    for j in range(r):
        lijst.append([gangen[i:i+2] for i in range(j*k*2,j*k*2+k*2,2)]) #van 0 tot 2k, van 2k tot 4k, van 4k tot...
    return lijst    

def switch(windrichting):
    d = {'N':'Z', 'Z':'N', 'W':'O', 'O':'W'}
    return d[str(windrichting)]

def step(windrichting):
    d = {'N':(-1,0), 'Z':(1,0), 'W':(0,-1), 'O': (0,1)} # (rij,kolom)
    return d[str(windrichting)]

def diepte(doorsnede):
    """
    >>> diepte([['NZ', 'ZW', 'NZ', 'ZW', 'NW', 'NW', 'OW', 'ZW'], ['NZ', 'ZO', 'OW', 'ZW', 'OW', 'ZO', 'NZ', 'ZW'], ['NO', 'NW', 'NZ', 'NO', 'OW', 'OW', 'ZW', 'ZO'], ['NW', 'NO', 'ZO', 'OW', 'NW', 'NW', 'ZO', 'ZW']])
    11
    """
    r,k,diepte= 0,0,0
    vak = doorsnede[r][k]
    windrichting_uitgang = (vak).replace('N','')#We gaan via het noorden binnen.
    diepte = 1 #we komen al in het 1ste vakje aan, diepte is dus zeker 1
    doodlopend = False
    while not doodlopend:
        r += step(windrichting_uitgang)[0] #verhoog r met de step
        k += step(windrichting_uitgang)[1] #verhoog k met de step
        if r in range(len(doorsnede)) and k in range(len(doorsnede[0])): # aantal rijen is max het aantal lijsten in doorsnede, kolommen is max het aantal elementen in 1 van die lijsten (ze zijn toch allemaal van de zlefde lengte)
            vak = doorsnede[r][k]
            windrichting_ingang = switch(windrichting_uitgang) #ingang is omgekeerde van uitgang
            if windrichting_ingang in vak:
                windrichting_uitgang = (vak).replace(windrichting_ingang,'')
                diepte +=1
            else:
                doodlopend = True
        else: doodlopend = True
    return diepte

if __name__ == '__main__':
    import doctest
    doctest.testmod()