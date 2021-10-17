# PRESIDENTEN

import datetime

def datumNaarDatetime(datum):
    '''
    >>> datumNaarDatetime('02/06/1998')
    datetime.date(1998, 6, 2)
    '''
    datum = datum.split('/')
    return datetime.date(int(datum[2]), int(datum[1]), int(datum[0]))

def staatshoofden(bestand):
    '''
    >>> presidenten = staatshoofden('vs_presidenten.txt')
    >>> presidenten['George Washington']
    (datetime.date(1732, 2, 22), datetime.date(1789, 4, 30), datetime.date(1797, 3, 4), datetime.date(1799, 12, 14))
    >>> presidenten['Barack Obama']
    (datetime.date(1961, 8, 4), datetime.date(2009, 1, 20), datetime.date(2017, 1, 20), None)
    >>> presidenten['Donald Trump']
    (datetime.date(1946, 6, 14), datetime.date(2017, 1, 20), None, None)
    '''
    bestand = open(bestand, 'r')
    d = {}
    for r in bestand:
        r = r.split('\t')
        #creeer een dictionary, als er geen datum staat, zet dan None
        d[r[0]] = tuple(datumNaarDatetime(r[i]) if r[i].strip() else None for i in range(1, 5))
    return d

def pensioen(naam, presidenten):
    '''
    >>> presidenten = staatshoofden('vs_presidenten.txt')
    >>> pensioen('Herbert Hoover', presidenten)
    11553
    >>> pensioen('James K. Polk', presidenten)
    103
    >>> pensioen('Bill Clinton', presidenten)
    5849
    >>> pensioen('Abraham Lincoln', presidenten)
    0
    >>> pensioen('Donald Trump', presidenten)
    0
    >>> pensioen('Donald Duck', presidenten)
    Traceback (most recent call last):
    AssertionError: onbekend staatshoofd
    '''
    assert naam in presidenten, 'onbekend staatshoofd'
    info = presidenten[naam]
    
    #bepaal begin en eind van het pensioen
    begin = info[2]
    eind = info[3] if info[3] else datetime.date.today()
    
    #geef het verschil terug, behalve als het pensioen nog niet is begonnen
    return (eind-begin).days if begin else 0

def levend(presidenten, voormalig=False, referentie=datetime.date.today()):
    '''
    >>> presidenten = staatshoofden('vs_presidenten.txt')
    >>> levend(presidenten) == {'Donald Trump', 'Jimmy Carter', 'George H. W. Bush', 'Bill Clinton', 'Barack Obama', 'George W. Bush'}
    True
    >>> levend(presidenten, voormalig=True) == {'George H. W. Bush', 'George W. Bush', 'Jimmy Carter', 'Bill Clinton', 'Barack Obama'}
    True
    >>> levend(presidenten, voormalig=True, referentie=datetime.date(2016, 12, 31)) == {'George W. Bush', 'George H. W. Bush', 'Bill Clinton', 'Jimmy Carter'}
    True
    >>> levend(presidenten, voormalig=True, referentie=datetime.date(1861, 12, 31)) == {'Martin Van Buren', 'Franklin Pierce', 'Millard Fillmore', 'James Buchanan', 'John Tyler'}
    True
    >>> levend(presidenten, voormalig=True, referentie=datetime.date(1994, 3, 26)) == {'Jimmy Carter', 'Ronald Reagan', 'Gerald Ford', 'Richard Nixon', 'George H. W. Bush'}
    True
    >>> levend(presidenten, voormalig=True, referentie=datetime.date(2003, 10, 12)) == {'Gerald Ford', 'Jimmy Carter', 'George H. W. Bush', 'Bill Clinton', 'Ronald Reagan'}
    True
    '''
    s = set()
    
    for president, info in presidenten.items():
        #geen sterfdatum of een sterfdatum na de referentie EN een geboortedatum voor de referentie
        if (not info[3] or info[3] > referentie) and info[0] < referentie: 
            #check voormaligheid
            if not voormalig:
                s.add(president)
            elif info[2] and info[2] < referentie: #einde ambtstermijn checken
                s.add(president)
    return s
            
if __name__ == '__main__':
    import doctest
    print(doctest.testmod())