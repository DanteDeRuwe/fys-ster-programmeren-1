def coordinaten(bestand):
    '''
    >>> coordinaten('foto1.txt') == {(10, 8), (5, 5), (6, 8), (6, 6), (7, 1), (10, 7), (9, 8), (10, 10), (6, 0), (1, 4), (0, 10), (1, 10), (5, 1), (8, 6), (10, 0), (9, 6), (2, 4), (7, 2), (8, 4)}
    True
    >>> coordinaten('foto2.txt') == {(10, 8), (4, 7), (6, 8), (7, 1), (10, 7), (10, 10), (9, 8), (6, 0), (0, 7), (1, 4), (7, 7), (8, 7), (1, 10), (5, 1), (10, 0), (9, 6), (2, 4), (7, 2), (8, 4)}
    True
    '''
    bestand = open(bestand, 'r')
    outputset = set()
    for r, m in enumerate(bestand):
        for k, n in enumerate(m):
            if n == '*':
                outputset.add( (r,k) )
    return outputset

def afwijkingen(bestand1, bestand2):
    '''
    >>> afwijkingen('foto1.txt', 'foto2.txt') == ({(8, 6), (5, 5), (0, 10), (6, 6)}, {(4, 7), (7, 7), (0, 7), (8, 7)})
    True
    '''
    co1, co2 = coordinaten(bestand1), coordinaten(bestand2)
    return ( set(e1 for e1 in co1 if e1 not in co2) , set(e2 for e2 in co2 if e2 not in co1))

def afstand(pos1, pos2):
    r1 , k1 = pos1
    r2 , k2 = pos2
    return (r1 - r2)**2 + (k1 - k2)**2

def planeten(bestand1, bestand2):
    '''
    >>> planeten('foto1.txt', 'foto2.txt') == {(4, 7): {(5, 5), (6, 6)}, (8, 7): {(8, 6)}, (7, 7): {(8, 6), (6, 6)}, (0, 7): {(0, 10)}}
    True
    '''
    d = {}
    for e2 in afwijkingen(bestand1, bestand2)[1]:
        
        afstanden = {}
        for e1 in afwijkingen(bestand1, bestand2)[0]:
            if afstand(e1, e2) not in afstanden:
                afstanden[afstand(e1, e2)] = {e1}   #astand tot bepaalde co2 : {co1}
            else:
                afstanden[afstand(e1, e2)].add(e1)  #zit de afstand al in de dict, voeg in de valueset dit toe
        
        if afstanden:              
            d[e2] = afstanden[min((a for a in afstanden))] #verkrijg de set met de kleinste key en zet dit als value bij een e2
        else:
            d[e2] = set()
    return d

def comparator(bestand1, bestand2):
    '''
    >>> print(comparator('foto1.txt', 'foto2.txt'))
    -------n--o-
    ----*-----*-
    ----*-------
    ------------
    -------n----
    -*---o------
    *-----o-*---
    -**----n----
    ----*-on----
    ------*-*---
    *------**-*-
    '''
    bestand1, bestand2 = open(bestand1, 'r'), open(bestand2, 'r')
    new = ''
    
    for r1,r2 in zip(bestand1, bestand2):
        newregel = ''
        for k1, k2 in zip(r1,r2):
            if k1 == k2:
                newregel += k1
            #vanaf hier zijn k1 en k2 niet meer gelijk
            elif k1 == '*':
                newregel += 'o'
            elif k2 == '*':
                newregel += 'n'
        new += newregel #geen extra newline meer aangezien k1 en k2 dan gelijk waren en deze al is toegevoegd
    return new.rstrip()
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()