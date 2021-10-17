def paren(element):
    '''
    >>> paren('Neon')
    ('Ne', 'Eo', 'On')
    >>> paren('Rutherfordium')
    ('Ru', 'Ut', 'Th', 'He', 'Er', 'Rf', 'Fo', 'Or', 'Rd', 'Di', 'Iu', 'Um')
    '''
    #opbouwen van een tuple en returnen
    return tuple(e.upper() + element[i+1].lower() for i, e in enumerate(element[:-1]))

def eerste(reeks, container):
    '''
    >>> eerste(['Ne', 'Eo', 'On'], {'Ne', 'On'})
    'Eo'
    >>> eerste(('Ne', 'Eo', 'On'), {'Ne', 'On', 'Eo'})
    '''
    #geef de eerste die niet in de container zit
    for r in reeks:
        if r not in container:
            return r

def toekennen(bestand, onmogelijk=None):
    '''
    >>> symbool = toekennen('elementen.txt', onmogelijk='???')
    >>> symbool['Neon']
    'Ne'
    >>> symbool['Rubidium']
    'Ru'
    >>> symbool['Ruthenium']
    'Ut'
    >>> symbool['Rutherfordium']
    'Rf'
    >>> symbool['Tin']
    '???'
    '''
    d = {} #een lege dict maken om op te bouwen
    al_toegekend = set() #een lege verz voor de toegekende symbolen
    bestand = open(bestand, 'r')
    
    for element in bestand:
        element = element.rstrip() #newlines en spaties weg aan de rechterkant
        symbool = eerste(paren(element), al_toegekend)
        if symbool: #als de functie 'eerste' niet None geeft
            al_toegekend.add(symbool)
            d[element] = symbool
        else:
            d[element] = onmogelijk
            
    return d


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
    