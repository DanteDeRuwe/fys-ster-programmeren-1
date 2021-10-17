class ZIP:
    '''
    >>> zip = ZIP('codes.txt')

    >>> zip.symbool2bitstring('i')
    '1000'
    >>> zip.symbool2bitstring('e')
    '000'
    >>> zip.symbool2bitstring('T')
    Traceback (most recent call last):
    AssertionError: onbekend symbool "T"
    
    >>> zip.bitstring2symbool('1000')
    'i'
    >>> zip.bitstring2symbool('000')
    'e'
    >>> zip.bitstring2symbool('01')
    Traceback (most recent call last):
    AssertionError: ongeldige bitstring
        
    >>> zip.comprimeer('internet')
    '1000001001100001100000100000110'
    >>> len(zip.comprimeer('internet'))
    31
    >>> zip.comprimeer('internet explorer')
    '1000001001100001100000100000110111000100101001111001001101100000011000'
    >>> zip.comprimeer('mozilla firefox')
    Traceback (most recent call last):
    AssertionError: onbekend symbool "z"
    
    >>> zip.decomprimeer('1000001001100001100000100000110')
    'internet'
    >>> zip.decomprimeer('1000001001100001100000100000110111000100101001111001001101100000011000')
    'internet explorer'
    >>> zip.decomprimeer('10000010011000011000001000001101')
    Traceback (most recent call last):
    AssertionError: ongeldige bitstring
    >>> zip.decomprimeer('10000010011000011000000000110')
    Traceback (most recent call last):
    AssertionError: ongeldige bitstring
    '''
    def __init__(self, bestand):
        bestand = open(bestand, 'r')
        codes = [ r.rstrip().split('\t') for r in bestand]
        
        #2 dictionaries maken
        self.symboolnaarbitstring = {codes[i][0]:codes[i][1] for i, _ in enumerate(codes)}
        self.bitstringnaarsymbool = {v:k for k,v in self.symboolnaarbitstring.items()}
    
    def symbool2bitstring(self, symbool):
        assert symbool in self.symboolnaarbitstring, 'onbekend symbool "{}"'.format(symbool)
        return self.symboolnaarbitstring[symbool]
    
    def bitstring2symbool(self, bitstring):
        assert bitstring in self.bitstringnaarsymbool, 'ongeldige bitstring'
        return self.bitstringnaarsymbool[bitstring]
    
    def comprimeer(self, woord):
        outputstring = ''
        for letter in woord:
            outputstring += self.symbool2bitstring(letter)
        
        return outputstring
    
    def decomprimeer(self, bitstring):
    
        bitstringlijst = []
        bitstringcopy = str(bitstring)
        
        
        while bitstring:                     
    
            if bitstringcopy in self.bitstringnaarsymbool:      #als hij in de dict zit, dan is het een geldige
                bitstringlijst.append(bitstringcopy)                     #steek hem dan in de lijst
                bitstring = bitstring[len(bitstringcopy):]              #haal hem weg uit de bitstring
                bitstringcopy = str(bitstring)                          #maak terug een kopie van de hele bitstring
            
            else:                                               #zit hij er niet in
                bitstringcopy = bitstringcopy[:-1]                                #haal het laatste karakter weg en probeer opnieuw
                assert len(bitstringcopy) > 2, 'ongeldige bitstring' #als de bitstringkopie kleiner wordt dan 2, zijn er bits teveel
        outputstring = ''
        for bit in bitstringlijst:
            outputstring += self.bitstring2symbool(bit)
        
        return outputstring

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())