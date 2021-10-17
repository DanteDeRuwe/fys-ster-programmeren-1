def ouroboros(woord_str):
    """
    controleert of het woord dat wordt ingegeven een ouroboros is
    
    >>> ouroboros('agaragar')
    True
    >>> ouroboros('sensuousness')
    True
    >>> ouroboros('verdrevene')
    True
    >>> ouroboros('legovogel')
    False
    """
    #het woord wordt dubbel geschreven
    controle_str = woord_str * 2
    #maak hiervan een omgekeerde string, maar zonder de eerste en laatste letter (uitsluiten palindroom)
    controle_str = controle_str[-2:0:-1]
    #verwijder vooraan letters tot de controlestring begint met je originele woord
    while not controle_str.startswith(woord_str):
        controle_str = controle_str[1:]
        #als in de controlestring het woord niet meer kan gevonden worden is het meteen fout
        if len(controle_str) < len(woord_str):
            return False
    #als we uit de while loop geraken, is het woord gevonden
    return True

def tsuchinoko(zin):
    """
    onderzoekt de 'tsuchinoko' van een woord of zin
    
    >>> tsuchinoko('Archetypical')
    5
    >>> tsuchinoko('RESTAURATEURS')
    0
    >>> tsuchinoko('recherche')
    3
    >>> tsuchinoko('A bad egg hit KLM wipers two ways.')
    16
    """
    #beginwaarden van variabelen vastleggen
    pos = 0
    tsuchinoko_count = 0
    
    #overloop elk karakter
    for karakter in zin:
        #als het karakter een letter is
        if karakter.isalpha() and not karakter.isspace():
            #als de positie in het alfabet gelijk is aan de positie in de zin (met a = 0, b = 1 etc)
            if ord(karakter.lower())-ord('a') == pos:
                # tel 1 bij de counter
                tsuchinoko_count += 1
            #verhoog de positie
            pos += 1
    return tsuchinoko_count

def amphisbaena(woord):
    """
    controleert of het woord dat wordt ingegeven een amphisbaena is
    
    >>> amphisbaena('RESTAURATEURS')
    True
    >>> amphisbaena('Archetypical')
    False
    >>> amphisbaena('recherche')
    True
    """
    #maak het woord lowercase
    woord = woord.lower()
    #maak 2 lijsten van de 2 slices die elk de helft van het woord zijn
    letterlijst_1 = list(woord[:len(woord) // 2])
    letterlijst_2 = list(woord[len(woord)-1:len(woord) - (len(woord) // 2 + 1):-1])
    #sorteer de lijsten
    letterlijst_1.sort()
    letterlijst_2.sort()
    #geef een boolean terug
    return letterlijst_1 == letterlijst_2
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()