import math

def eindwoord(zin):
    '''
    >>> eindwoord("Lo ferm voler qu'el cor m'intra")
    'intra'
    >>> eindwoord("no'm pot ges becs escoissendre ni ongla")
    'ongla'
    >>> eindwoord("de lauzengier qui pert per mal dir s'arma;")
    'arma'
    '''
    woord = ''
    for karakter in zin[::-1]:
        if karakter.isalpha():
            woord+= karakter
        elif woord and not karakter.isalpha():
            return woord[::-1]

def stanzas(bestand):
    '''
    >>> stanzas('sestina0.txt')
    [['intra', 'ongla', 'arma', 'verja', 'oncle', 'cambra'], ['cambra', 'intra', 'oncle', 'ongla', 'verja', 'arma'], ['arma', 'cambra', 'verja', 'intra', 'ongla', 'oncle'], ['oncle', 'arma', 'ongla', 'cambra', 'intra', 'verja'], ['verja', 'oncle', 'intra', 'arma', 'cambra', 'ongla'], ['ongla', 'verja', 'cambra', 'oncle', 'arma', 'intra'], ['oncle', 'arma', 'intra']]
    >>> stanzas('sestina1.txt')
    [['enters', 'nail', 'soul', 'rod', 'uncle', 'room'], ['room', 'enters', 'uncle', 'nail', 'rod', 'soul'], ['soul', 'room', 'rod', 'enters', 'nail', 'uncle'], ['uncle', 'soul', 'nail', 'room', 'enters', 'rod'], ['rod', 'uncle', 'enters', 'soul', 'room', 'nail'], ['nail', 'rod', 'room', 'uncle', 'soul', 'enters'], ['nail', 'soul', 'enters']]
    >>> stanzas('sestina2.txt')
    [['woe', 'sound', 'cryes', 'part', 'sleepe', 'augment'], ['augment', 'woe', 'sound', 'cryes', 'part', 'sleepe'], ['sleepe', 'augment', 'woe', 'sound', 'cryes', 'part'], ['part', 'sleepe', 'augment', 'woe', 'sound', 'cryes'], ['cryes', 'part', 'sleepe', 'augment', 'woe', 'sound'], ['sound', 'cryes', 'part', 'sleepe', 'augment', 'woe'], ['sound', 'part', 'augment']]
    '''
    bestand = open(bestand, 'r')
    lijst, deellijst = [], []
    for regel in bestand:
        if eindwoord(regel):
            deellijst.append(eindwoord(regel).lower())
        else:
            if deellijst:
                lijst.append(deellijst)
            deellijst = []
    lijst.append(deellijst)
    return lijst

def permutatie(lijst, patroon=None):
    '''
    >>> permutatie(['rose', 'love', 'heart', 'sang', 'rhyme', 'woe'])
    ['woe', 'rose', 'rhyme', 'love', 'sang', 'heart']
    >>> permutatie(['woe', 'rose', 'rhyme', 'love', 'sang', 'heart'])
    ['heart', 'woe', 'sang', 'rose', 'love', 'rhyme']
    >>> permutatie(['rose', 'love', 'heart', 'sang', 'rhyme'])
    ['rhyme', 'rose', 'sang', 'love', 'heart']
    >>> permutatie(['rose', 'love', 'heart', 'sang', 'rhyme', 'woe'], [6, 1, 5, 2, 4, 3])
    ['woe', 'rose', 'rhyme', 'love', 'sang', 'heart']
    >>> permutatie(['rose', 'love', 'heart', 'sang', 'rhyme', 'woe'], [6, 5, 4, 3, 2, 1])
    ['woe', 'rhyme', 'sang', 'heart', 'love', 'rose']
    >>> permutatie(['rose', 'love', 'heart', 'sang', 'rhyme', 'woe'], [6, 1, 5, 3, 4, 3])
    Traceback (most recent call last):
    AssertionError: ongeldige permutatie
    '''
    #als er geen patroon is meegegeven --> canoniek
    if not patroon:
        n = len(lijst)
        patroon = [i+1 for i,_ in enumerate(lijst)]
        pat1 = patroon[:n//2] 
        pat2 = patroon[n//2:][::-1]
        
        newpatroon = []
        for p1,p2 in zip(pat1,pat2): #voeg steeds paren toe
            newpatroon.extend( (p2, p1) )
            
        #als n oneven is is er nog 1 p2 niet toegevoegd    
        if n%2 == 0: 
            patroon = newpatroon
        else:
            patroon = newpatroon +[pat2[-1]]
            
    else:       
        assert set(patroon) == set(i+1 for i,_ in enumerate(lijst)), 'ongeldige permutatie'  
    
    new = []
    for p in patroon:
        new.append(lijst[p-1])
    return new

def sestina(bestand, patroon=None):
    '''
    >>> sestina('sestina0.txt')
    True
    >>> sestina('sestina0.txt', [6, 1, 5, 2, 4, 3])
    True
    >>> sestina('sestina12.txt')
    True
    >>> sestina('sestina2.txt')
    False
    >>> sestina('sestina2.txt', [6, 1, 2, 3, 4, 5])
    True
    '''
    stanz = stanzas(bestand)
    
    
    #als er een envoi is
    if len(stanz[-1]) == math.floor(len(stanz[0])/2):
        controle = True
        for i, s in enumerate(stanz[:-1]):
            #             vorige controle       n regels,            n stanzas,     permutatie van deze is de volgende, permutatie van laatste is terug eerste (modulo)           
            controle = all( (controle, len(stanz[0]) == len(s) , len(s) == len(stanz[:-1]) , permutatie(s, patroon) == stanz[:-1][(i+1)%len(stanz[:-1])]) )
        for e in stanz[-1]:
            #woorden envoi ook woorden stanza EN alle voorgaande
            controle = all( (controle, e in stanz[:-1][0]) )
        return controle
    
    
    #als er geen envoi is
    else:
        controle = True
        for i, s in enumerate(stanz[:-1]):
            #             vorige controle       n regels,            n stanzas,     permutatie van deze is de volgende, permutatie van laatste is terug eerste (modulo)           
            controle = all( (controle, len(stanz[0]) == len(s) , len(s) == len(stanz) , permutatie(s, patroon) == stanz[(i+1)%len(stanz)]) )
        return controle
    
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()