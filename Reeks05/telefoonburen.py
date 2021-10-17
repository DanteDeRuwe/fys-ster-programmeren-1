def cijfers(nummer):
    """
    >>> cijfers('0472/91.39.17')
    '0472913917'
    >>> cijfers('++32 (0)9 264 4779')
    '32092644779'
    """
    output = ''
    for karakter in nummer:
        if karakter.isdigit():
            output += karakter
        
    return output

def vervangen(layout, nummer):
    """
    >>> vervangen('0472/91.39.17', 1234567890)
    '1234/56.78.90'
    >>> vervangen('++32 (0)9 264 4779', 123456789)
    '++00 (1)2 345 6789'
    """
    layout = list(layout)
    nummer = str(nummer)
    layposlijst = []
    for i, element in enumerate(layout):
        if element.isdigit():
            layposlijst.append(i) #lijst met alle posities in de layout waar cijfers staan
    verschil = len(nummer) - len(layposlijst)
    if verschil < 0:
        nummer = abs(verschil) * '0' + nummer
    for j, pos in enumerate(layposlijst):
        layout[pos] = nummer[j]
    return ''.join(layout)     
    
def bovenbuur(nummer):
    """
    >>> bovenbuur('0472/91.39.17')
    '0472/91.39.18'
    >>> bovenbuur('++32 (0)9 264 4779')
    '++32 (0)9 264 4780'
    """
    boven = vervangen(nummer, (int(cijfers(nummer))+1))
    return boven

def onderbuur(nummer):
    """
    >>> onderbuur('0472/91.39.17')
    '0472/91.39.16'
    >>> onderbuur('++32 (0)9 264 4779')
    '++32 (0)9 264 4778'
    """
    onder = vervangen(nummer, (int(cijfers(nummer))-1))
    return onder

if __name__ == '__main__':
    import doctest
    doctest.testmod()