def vullen(letters):
    '''
    >>> zak = vullen('IAMDIETINGIEATQUINCEJELLYLOTSOFGROUNDMAIZEGIVESVARIETYICOOKRHUBARBANDSODAWEEPANEWORPUTONEXTRAFLESH__')
    >>> zak == {'U': 4, '_': 2, 'C': 2, 'K': 1, 'D': 4, 'T': 6, 'Q': 1, 'V': 2, 'A': 9, 'F': 2, 'O': 8, 'J': 1, 'I': 9, 'N': 6, 'P': 2, 'S': 4, 'M': 2, 'W': 2, 'E': 12, 'Z': 1, 'G': 3, 'Y': 2, 'B': 2, 'L': 4, 'R': 6, 'X': 1, 'H': 2}
    True
    '''
    d = {}
    for l in letters:
        if l not in d:
            d[l] = 0
        d[l] += 1
    return d
def omschrijving(zak):
    '''
    >>> zak = {'U': 4, '_': 2, 'C': 2, 'K': 1, 'D': 4, 'T': 6, 'Q': 1, 'V': 2, 'A': 9, 'F': 2, 'O': 8, 'J': 1, 'I': 9, 'N': 6, 'P': 2, 'S': 4, 'M': 2, 'W': 2, 'E': 12, 'Z': 1, 'G': 3, 'Y': 2, 'B': 2, 'L': 4, 'R': 6, 'X': 1, 'H': 2}
    >>> omschrijving(zak) == {1: {'Q', 'Z', 'X', 'K', 'J'}, 2: {'F', '_', 'P', 'C', 'M', 'W', 'Y', 'B', 'V', 'H'}, 3: {'G'}, 4: {'U', 'D', 'L', 'S'}, 6: {'N', 'R', 'T'}, 8: {'O'}, 9: {'I', 'A'}, 12: {'E'}}
    True
    '''
    d = {}
    for l, c in zak.items():    #letter-cijferparen onderzoeken
        if c not in d:          #zit het cijfer nog niet in de dict
            d[c] = set(l)       #voeg het toe met value een dictionary met de letter
        else: d[c].add(l)       #als het er wel inzit: voeg aan de aanwezige dict nog een letter toe
    return d

def wegnemen(letters, zak):
    '''
    >>> zak = {'U': 4, '_': 2, 'C': 2, 'K': 1, 'D': 4, 'T': 6, 'Q': 1, 'V': 2, 'A': 9, 'F': 2, 'O': 8, 'J': 1, 'I': 9, 'N': 6, 'P': 2, 'S': 4, 'M': 2, 'W': 2, 'E': 12, 'Z': 1, 'G': 3, 'Y': 2, 'B': 2, 'L': 4, 'R': 6, 'X': 1, 'H': 2}
    >>> wegnemen('AEERTYOXMCNB_S', zak)
    >>> omschrijving(zak) == {1: {'J', '_', 'C', 'K', 'M', 'Z', 'Y', 'B', 'Q'}, 2: {'W', 'P', 'V', 'F', 'H'}, 3: {'S', 'G'}, 4: {'U', 'D', 'L'}, 5: {'N', 'R', 'T'}, 7: {'O'}, 8: {'A'}, 9: {'I'}, 10: {'E'}}
    True
    '''
    for l in letters:
        assert l in zak, 'niet alle letters zitten in het zakje'
        if zak[l] > 1:
            zak[l] -= 1
        else: del zak[l]
            
if __name__ == '__main__':
    import doctest
    doctest.testmod()