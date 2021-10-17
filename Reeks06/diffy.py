def volgende(reeks):
    """
    >>> volgende([32, 9, 14, 3])
    (23, 5, 11, 29)
    >>> volgende((1, 2, 1, 2, 1, 0))
    (1, 1, 1, 1, 1, 1)
    >>> volgende((1, 2, 1, 2, 1, 1))
    (1, 1, 1, 1, 0, 0)
    """
    reeks = list(reeks)
    kopie = reeks
    x = [abs(reeks[i]-kopie[(i+1)%len(kopie)]) for i,_ in enumerate(reeks)]
    return tuple(x)

def ducci(reeks):
    """
    >>> ducci([32, 9, 14, 3])
    ((32, 9, 14, 3), (23, 5, 11, 29), (18, 6, 18, 6), (12, 12, 12, 12), (0, 0, 0, 0))
    >>> ducci((1, 2, 1, 2, 1, 0))
    ((1, 2, 1, 2, 1, 0), (1, 1, 1, 1, 1, 1), (0, 0, 0, 0, 0, 0))
    >>> ducci((1, 2, 1, 2, 1, 1))
    ((1, 2, 1, 2, 1, 1), (1, 1, 1, 1, 0, 0), (0, 0, 0, 1, 0, 1), (0, 0, 1, 1, 1, 1), (0, 1, 0, 0, 0, 1), (1, 1, 0, 0, 1, 1), (0, 1, 0, 1, 0, 0), (1, 1, 1, 1, 0, 0))
    """
    outputlijst = [tuple(reeks)]
    while len(outputlijst) == len(set(outputlijst)) and set(outputlijst[-1]) != {0}: # telkens wanneer er geen dubbels zijn en als er geen tuple is met enkel nullen
        outputlijst.append(volgende(outputlijst[-1]))
    return tuple(outputlijst)

def periode(reeks):
    """ 
    >>> periode([32, 9, 14, 3])
    0
    >>> periode((1, 2, 1, 2, 1, 0))
    0
    >>> periode((1, 2, 1, 2, 1, 1))
    6
    """
    reeks = ducci(reeks)
    return len(reeks) - 1 - reeks.index(reeks[-1])
    
    '''  OUDE CODE
    d = list(ducci(reeks))
    if set(d[-1]) == {0}:       #als laatste tuple allemaal nullen is: 0
        return 0
    else:
        test = set()    #lege verz
        periode = 0
        for i, _ in enumerate(d):
            if d[-(i+1)] in test:   #loop de tuples af van achter naar voor in de lijst
                return periode      #als het nog eens voorkomt: geef de periode
            else: 
                test.add(d[-(i+1)]) #als de tuple nog niet is voorgekomen, voeg hem toe aan de verz en verhoog de periode
                periode += 1'''
            
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()