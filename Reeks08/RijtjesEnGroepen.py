
def groep(reeks):
    '''
    >>> groep(['4R', '4B', '4G', '4Z'])
    True
    >>> groep({'6B', '7B', '8B', '9B', '10B'})
    False
    >>> groep(('11R', '2B', '7G', '2B', '9Z'))
    False
    '''
    if len(set(reeks)) != len(reeks) or len(reeks) < 3:
        return False
    reeks = list(reeks)
    eerstecijfer = reeks[0][:-1]
    for e in reeks:
        if e[:-1] != eerstecijfer:
            return False
    return True

def rijtje(reeks):
    '''
    >>> rijtje(['4R', '4B', '4G', '4Z'])
    False
    >>> rijtje({'6B', '7B', '8B', '9B', '10B'})
    True
    >>> rijtje(('11R', '2B', '7G', '2B', '9Z'))
    False
    '''
    if len(set(reeks)) != len(reeks) or len(reeks) < 3:
        return False
    reeks = list(reeks)
    eerstekleur = reeks[0][-1]
    for e in reeks:
        if e[-1] != eerstekleur:
            return False
    cijferlijst = [int(e[:-1]) for e in reeks]
    cijferlijst.sort()
    if [cijferlijst[0]+i for i,_ in enumerate(cijferlijst)] != cijferlijst:
        return False
    return True

if __name__ == '__main__':
    import doctest
    doctest.testmod()
        
            
            
            