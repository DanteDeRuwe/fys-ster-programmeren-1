def isGeldig(symbool, element, lengte=None):
    '''
    >>> isGeldig('Zer', 'Zeddemorium')
    True
    >>> isGeldig('Zer', 'Zeddemorium', 2)
    False
    >>> isGeldig('di', 'Zeddemorium')
    False
    '''
    #Checken van criterium 1
    if not symbool[0].isupper() or (len(symbool) != 1 and not symbool[1:].islower()):
        return False
    
    #Checken van criterium 2 

    element = element.lower()
    
    for s in symbool.lower(): #overloop de letters in het symbool
        index = element.find(s)
        if index == -1: #als find heeft gefaald (geeft dan -1 terug)
            return False
        element = element[index+1:] #verkort de string iedere keer na de gevonden letter
 
    #evt checken van criterium 3
    return len(symbool) == lengte if lengte else True


def symbolen(element):
    '''
    >>> symbolen('Iron') == {'Ir', 'Io', 'In', 'Ro', 'Rn', 'On'}
    True
    >>> symbolen('Neon') =={'Eo', 'Nn', 'No', 'En', 'Ne', 'On'}
    True
    '''
    v = set()
    #neem een letter in het element(behalve de laatste)
    for i, e in enumerate(element[:-1]): 
        #overloop de rest van de letters na die letter
        for e2 in element[i+1:]:
            #voeg steeds een combinatie toe aan de verzameling
            v.add(e.upper() + e2.lower())
    return v

def voorkeur(element, laatste=False):
    '''
    >>> voorkeur('Iron')
    'In'
    >>> voorkeur('Iron', laatste=True)
    'Ro'
    >>> voorkeur('Neon')
    'En'
    >>> voorkeur('Neon', True)
    'On'
    '''
    #maak een alfabetisch gesorteerde lijst met mogelijke symbolen
    symbolen_list = sorted(list(symbolen(element)))
    
    #kies de eerste of de laatste
    return symbolen_list[-1] if laatste else symbolen_list[0]

if __name__ == '__main__':
    import doctest
    doctest.testmod()