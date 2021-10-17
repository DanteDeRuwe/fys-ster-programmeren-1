def vertaal(woord, vertalingen):
    '''
    >>> vertalingen = {'hij':'zij', 'broer':'zus'}
    >>> vertaal('hij', vertalingen)
    'zij'
    >>> vertaal('HIJ', vertalingen)
    'ZIJ'
    >>> vertaal('Hij', vertalingen)
    'Zij'
    >>> vertaal('broer', vertalingen)
    'zus'
    >>> vertaal('mijn', vertalingen)
    'mijn'
    '''
    v = woord if woord.lower() not in vertalingen else vertalingen[woord.lower()]
    if woord.isupper():
        return v.upper()
    elif woord[0].isupper():
        return v.capitalize()
    else: return v
    
def geslachtsverandering(zin, vertalingen):
    '''
    >>> vertalingen = {'hij':'zij', 'broer':'zus'}
    >>> geslachtsverandering('Hij is mijn broer.', vertalingen)
    'Zij is mijn zus.'
    '''    
    woord, woordenlijst = '', []
    for k in zin + ' ': #eindspatie erbij
        if k.isalpha():
            woord += k
        else: 
            if woord:
                woordenlijst.extend((woord,k))
            else:
                woordenlijst.append(k)
            woord = ''
    for i, woord in enumerate(woordenlijst):
        woordenlijst[i] = vertaal(woord, vertalingen)
    return ''.join(woordenlijst)[:-1] #eindspatie weer weg

def geslachtsherstel(zin, vertalingen):
    '''
    >>> vertalingen = {'hij':'zij', 'broer':'zus'}
    >>> geslachtsherstel('Zij is mijn zus.', vertalingen)
    'Hij is mijn broer.'
    '''
    omgekeerd = {b: a for a, b in vertalingen.items()}
    return geslachtsverandering(zin, omgekeerd)
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()