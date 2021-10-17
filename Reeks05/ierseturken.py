def isKlinker(letter):
    """
    >>> isKlinker('a')
    True
    >>> isKlinker('c')
    False
    >>> isKlinker('E')
    True
    """
    
    if letter.lower() in ('a', 'e', 'i', 'o', 'u'):
        klinker = True
    else:
        klinker = False
    return klinker

def codeer(woord):
    """
    >>> codeer('Fabiano')
    'Fabababianabo'
    >>> codeer('CIA-agent')
    'CAbiA-abagabent'
    """
    klinkergroep = ''
    output = ''
    for i, letter in enumerate(woord): #overloop alle letters in een woord en hou de indices bij
        if isKlinker(letter):   #als de letter een klinker is, voeg het toe aan een groepje
            klinkergroep += letter
        if not isKlinker(letter) or i == (len(woord)-1):    #vanaf het geen klinker is of we zijn aan het einde van het woord
            if len(klinkergroep) > 0:   #als er klinkers zijn
                if klinkergroep[0].isupper():   #als klinkergroep begint met hoofdletter
                    output += 'Ab'+ (klinkergroep[0]).lower() + klinkergroep[1:]
                else: #kleine letter
                    output += 'ab' + klinkergroep
            if not isKlinker(letter): #als letter TOCH een klinker was, doordat het de laatste letter vh woord is, hoef je deze niet nog eens extra aan output toe te voegen
                output += letter 
            klinkergroep = ''
    return output
    
def decodeer(woord):
    """
    >>> decodeer('Fabababianabo')
    'Fabiano'
    >>> decodeer('CAbiA-abagabent')
    'CIA-agent'
    """
    output = ''
    i = 0
    while i in range(len(woord)-1): #overloopt elke index van de letters vh woord
        tweeletters = woord[i] + woord[i+1] #telkens per 2 checken
        
        if tweeletters == 'Ab' and isKlinker(woord[i+2]):
            output += woord[i+2].upper()
            i += 3  #zorgt ervoor dat de 'ab' wordt overgeslagen
        elif tweeletters == 'ab' and isKlinker(woord[i+2]):
            output += woord[i+2].lower()
            i += 3    #zorgt ervoor dat de 'ab' wordt overgeslagen
        else: #als de 2 letters niks met 'ab' te maken hebben of als op ab geen klinker volgt
            output += woord[i] #eerste letter bij output
            i += 1
        if i == len(woord)-1:
            output += woord[i]
    return output

