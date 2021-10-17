def serienummer(nummer):
    '''
    >>> serienummer(834783)
    '00834783'
    >>> serienummer('47839')
    '00047839'
    >>> serienummer(834783244839184)
    '834783244839184'
    >>> serienummer('4783926132432*')
    Traceback (most recent call last):
    AssertionError: ongeldig serienummer
    '''
    
    nummer = str(nummer).zfill(8)
    assert str(nummer).isdigit() and nummer != 8*'0', 'ongeldig serienummer'
    return nummer

def standvastig(nummer):
    '''
    >>> standvastig(44444444)
    True
    >>> standvastig('44544444')
    False
    >>> standvastig('444444444444')
    True
    '''
    nummer = serienummer(nummer)
    return nummer == len(nummer)*nummer[0]

def radar(nummer):
    '''
    >>> radar(1133110)
    True
    >>> radar('83289439')
    False
    '''
    nummer = serienummer(nummer)
    l = len(nummer) // 2
    return nummer[:l] == nummer[-1:-(l+1):-1] and not standvastig(nummer)

def repeater(nummer):
    '''
    >>> repeater(20012001)
    True
    >>> repeater('83289439')
    False
    '''
    nummer = serienummer(nummer)
    l = len(nummer) // 2
    return nummer[:l] == nummer[l:] and not standvastig(nummer)

def radarrepeater(nummer):
    '''
    >>> radarrepeater('12211221')
    True
    >>> radarrepeater('83289439')
    False
    '''
    return radar(nummer) and repeater(nummer)

def numismatist(lijst, soort = standvastig):
    '''
    >>> numismatist([33333333, 1133110, '77777777', '12211221'])
    [33333333, '77777777']
    >>> numismatist([33333333, 1133110, '77777777', '12211221'], radar)
    [1133110, '12211221']
    >>> numismatist([33333333, 1133110, '77777777', '12211221'], soort=repeater)
    ['12211221']
    '''
    return [nummer for nummer in lijst if soort(nummer)]

if __name__ == '__main__':
    import doctest
    doctest.testmod()