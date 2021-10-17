def ontbrekende_parameter(d,s):
    '''
    >>> ontbrekende_parameter({'F':1.2, 'D':0.6, 'H':2, 'B':4}, 'FDVBH')
    'V'
    >>> ontbrekende_parameter({'F':1.2, 'D':0.6, 'H':2, 'X':4}, 'FDVBH')
    Traceback (most recent call last):
    AssertionError: ongeldige parameters
    >>> ontbrekende_parameter({'F':1.2, 'D':0.6, 'H':2}, 'FDVBH')
    Traceback (most recent call last):
    AssertionError: ongeldige parameters
    '''
    ontbr = [x for x in s if x not in d]
    assert len(ontbr) == 1, 'ongeldige parameters'
    return ontbr[0]

def jongleren(d):
    '''
    >>> jongleren({'F':1.2, 'D':0.6, 'H':2, 'B':4}) == {'F': 1.2, 'D': 0.6, 'B': 4, 'V': 0.3, 'H': 2}
    True
    >>> jongleren({'D': 0.6, 'B': 4, 'V': 0.3, 'H': 2}) == {'D': 0.6, 'V': 0.3, 'F': 1.2, 'H': 2, 'B': 4}
    True
    >>> jongleren({'F':1.2, 'D':0.6, 'H':2, 'X':4})
    Traceback (most recent call last):
    AssertionError: ongeldige parameters
    '''
    for key in d:
        d[key] = float(d[key])                          #omzetten naar floats
    ontbr = ontbrekende_parameter(d, 'FDVBH')           #ontbrekende param bepalen
    (F,D,V,B,H) = tuple(d.get(x,1) for x in 'FDVBH')    #parameters zijn hun waarde uit de dictionary, behalve als hij niet in de dictionary zit, dan is het gewoon 1 (we hebben deze waarde toch niet meer nodig)
    func = {                    
        'B' : H*(F+D) / (V+D),
        'H' : B*(V+D) / (F+D),
        'F' : (B*(V+D)/H) - D,                          #functies
        'V' : (H*(F+D)/B) - D,
        'D' : (B*V-H*F) / (H-B),
    }
    
    d[ontbr] = round(func[ontbr],2)                     # maak een dict entry aan met de waarde uit de functies, afgerond op 2 cijfers
    return d

def jongleur(**kwargs):
    '''
    >>> jongleur(F=1.2, D=0.6, H=2, B=4) == {'F': 1.2, 'D': 0.6, 'B': 4, 'V': 0.3, 'H': 2}
    True
    >>> jongleur(D=0.6, B=4, V=0.3, H=2) == {'D': 0.6, 'V': 0.3, 'F': 1.2, 'H': 2, 'B': 4}
    True
    >>> jongleur(F=1.2, D=0.6, H=2, X=4)
    Traceback (most recent call last):
    AssertionError: ongeldige parameters
    '''
    d = {}
    for key in kwargs:
        d[key] = kwargs[key]        #maak een dict van de kwargs
    return jongleren(d)
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()