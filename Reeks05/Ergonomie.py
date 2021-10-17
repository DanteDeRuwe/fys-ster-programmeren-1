def positie(letter):
    
    """
    >>> rij, kolom = positie('K')
    >>> rij
    0
    >>> kolom
    10
    >>> rij, kolom = positie('q')
    >>> rij
    1
    >>> kolom
    3
    """
    
    letter = letter.upper()
    letter_naar_getal = ord(letter) - ord('A')
    if letter_naar_getal <= 12:
        kolom = letter_naar_getal
        rij = 0
    else:
        kolom = letter_naar_getal - 13
        rij = 1
    return (rij, kolom)

def verschuiving(letter1, letter2):
    
    """ 
    >>> verschuiving('K', 'q')
    8
    >>> verschuiving('f', 'e')
    1
    """
    
    hor = abs(positie(letter1)[1] - positie(letter2)[1])
    ver = abs(positie(letter1)[0] - positie(letter2)[0])
    verpl = hor + ver
    
    return verpl

def ergonomie(woord):
    
    """
    >>> ergonomie('EERST')
    3
    >>> ergonomie('VAZAL')
    46
    >>> ergonomie('feestsfeer')
    8
    >>> ergonomie('vakdiploma')
    83
    >>> ergonomie('verantwoordelijkheidsgebieden')
    90
    >>> ergonomie('chloorfluorkoolstofverbinding')
    146
    """
    ergon = 0
    for i in range(len(woord)-1):
        ergon += verschuiving(woord[i], woord[i+1])
    return ergon
    

if __name__ == '__main__':
    import doctest
    doctest.testmod()