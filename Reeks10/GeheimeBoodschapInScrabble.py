from copy import deepcopy
class Zak:
    '''
    >>> zak = Zak('IAMDIETINGIEATQUINCEJELLYLOTSOFGROUNDMAIZEGIVESVARIETYICOOKRHUBARBANDSODAWEEPANEWORPUTONEXTRAFLESH__')
    >>> zak.inhoud == {'U': 4, '_': 2, 'C': 2, 'K': 1, 'D': 4, 'T': 6, 'Q': 1, 'V': 2, 'A': 9, 'F': 2, 'O': 8, 'J': 1, 'I': 9, 'N': 6, 'P': 2, 'S': 4, 'M': 2, 'W': 2, 'E': 12, 'Z': 1, 'G': 3, 'Y': 2, 'B': 2, 'L': 4, 'R': 6, 'X': 1, 'H': 2}
    True
    >>> print(zak)
    1: JKQXZ
    2: BCFHMPVWY_
    3: G
    4: DLSU
    6: NRT
    8: O
    9: AI
    12: E
    >>> zak
    Zak('AAAAAAAAABBCCDDDDEEEEEEEEEEEEFFGGGHHIIIIIIIIIJKLLLLMMNNNNNNOOOOOOOOPPQRRRRRRSSSSTTTTTTUUUUVVWWXYYZ__')
    >>> zak.wegnemen('AEERTYOXMCNB_S')
    >>> print(zak)
    1: BCJKMQYZ_
    2: FHPVW
    3: GS
    4: DLU
    5: NRT
    7: O
    8: A
    9: I
    10: E
    >>> zak
    Zak('AAAAAAAABCDDDDEEEEEEEEEEFFGGGHHIIIIIIIIIJKLLLLMNNNNNOOOOOOOPPQRRRRRSSSTTTTTUUUUVVWWYZ_')
    >>> zak.wegnemen('AXXEXNRTBFHPVW')
    Traceback (most recent call last):
    AssertionError: niet alle letters zitten in het zakje
    >>> print(zak)
    1: BCJKMQYZ_
    2: FHPVW
    3: GS
    4: DLU
    5: NRT
    7: O
    8: A
    9: I
    10: E
    >>> zak
    Zak('AAAAAAAABCDDDDEEEEEEEEEEFFGGGHHIIIIIIIIIJKLLLLMNNNNNOOOOOOOPPQRRRRRSSSTTTTTUUUUVVWWYZ_')
    '''
    def __init__(self, letters):
        d = {}
        for l in letters:
            if l not in d:
                d[l] = 0
            d[l] += 1
        self.inhoud = d
    
    def __str__(self):
        zak = deepcopy(self.inhoud)
        d = {}
        for l, c in zak.items():    #letter-cijferparen onderzoeken
            if c not in d:          #zit het cijfer nog niet in de dict
                d[c] = [l]          #voeg het toe met value een lijst met de letter
            else: d[c].append(l)    #als het er wel inzit: voeg aan de aanwezige lijst nog een letter toe
        
        for key in d.keys():        #values sorteren in alfabetische volgorde
            d[key] = sorted(d[key])
            
        return '\n'.join( ['{}: {}'.format(k, ''.join(v)) for k, v in d.items()] ) #maak een lijst met key: value, de values zijn de gejoinede lijsten. join deze lijst aan elkaar door newlines.
         
    def __repr__(self):
        d = self.inhoud
        return "Zak('{}')".format(''.join(sorted([str(k)*v for k,v in d.items()]))) #neem een key uit de inhoud, doe deze maal het aantal keer hij voorkomt (de value), maak er een lijst mee en sorteer die. Joinen geeft dan de output
    
    def wegnemen(self, letters):
        zak = deepcopy(self.inhoud)
        for l in letters:
            assert l in zak, 'niet alle letters zitten in het zakje'
            if zak[l] > 1:
                zak[l] -= 1
            else: del zak[l]
        self.inhoud = zak

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())