import math
def driehoek(getal):
    """
    >>> driehoek(0)
    []
    >>> driehoek(1)
    [[1]]
    >>> driehoek(2)
    [[1], [1, 1]]
    >>> driehoek(3)
    [[1], [1, 1], [1, 2, 1]]
    >>> driehoek(4)
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
    >>> driehoek(5)
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    >>> driehoek(-1)
    Traceback (most recent call last):
    AssertionError: ongeldig aantal rijen
    >>> driehoek('hey')
    Traceback (most recent call last):
    AssertionError: ongeldig aantal rijen
    """
    assert isinstance(getal, int) == True and getal >= 0,"ongeldig aantal rijen"
    lijst = [[1]]
    if getal == 0: 
        return []
    else: 
        for i in range(1, getal):
            lijst.append([1])
            for j in range(len(lijst[i-1])-1):  #het aantal keer dat de we iets moeten doen is het aantal elementen in de rij erboven
                lijst[i].append(lijst[i-1][j]+lijst[i-1][j+1])  # 2 buren optellen van de lijst erboven
            lijst[i].append(1) 
    return lijst

def zeshoek(rij, kolom):
    """
    >>> zeshoek(8, 4)
    [15, 20, 35, 70, 56, 21]
    >>> zeshoek(16, 7)
    [2002, 3003, 6435, 11440, 8008, 3003]
    >>> zeshoek(3, 3)
    Traceback (most recent call last):
    AssertionError: ongeldige interne positie
    """
    assert kolom != 1 and kolom < rij , "ongeldige interne positie"
    pascal = driehoek(rij+1) #maak een pascaldriehoek
    kolom = kolom - 1 #dit puur om de indices intuitief te maken
    return [pascal[-3][kolom-1],pascal[-3][kolom],pascal[-2][kolom+1], pascal[-1][kolom+1], pascal[-1][kolom], pascal[-2][kolom-1]]

def kwadraat(rij, kolom):
    """
    >>> kwadraat(8, 4)
    '15 x 20 x 35 x 70 x 56 x 21 = 864360000 = 29400 x 29400'
    >>> kwadraat(16, 7)
    '2002 x 3003 x 6435 x 11440 x 8008 x 3003 = 10643228293383247161600 = 103166022960 x 103166022960'
    >>> kwadraat(3, 3)
    Traceback (most recent call last):
    AssertionError: ongeldige interne positie
    """
    lijst = zeshoek(rij, kolom)
    product = 1
    for element in lijst:
        product *= element
    return "{} = {} = {} x {}".format(" x ".join([str(x) for x in lijst]), product, int(math.sqrt(product)), int(math.sqrt(product)))
    
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()