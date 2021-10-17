import random

def trekken(getrokken = None):
    if not getrokken: #None vervangen
        getrokken = []
    kaart = ''
    while kaart in getrokken or not kaart: #not kaart zorgt ervoor dat de while maar 1x wordt uitgevoerd als de kaart niet in getrokken zit
        cijferlijst = [str(getal) for getal in range(2, 10)] + ['X', 'A', 'J','K', 'Q']
        suitslijst = ['D', 'C', 'H', 'S']
        kaart = random.choice(cijferlijst) + random.choice(suitslijst)
    return kaart

def leggen(rijen = 5, kolommen = 5):
    r = rijen
    k = kolommen
    assert r*k <= 52 and r>0 and k>0, 'ongeldig rooster'
    rlijst = []
    getrokken = []
    for _ in range(r): #r rijen aanmaken
        klijst = [] #voor elke rij beginnen met een lege lijst voor de kolommen
        for _ in range(k): #k kolommen 
            kaart = trekken(getrokken)
            klijst.append(kaart)
            getrokken.append(kaart)
        rlijst.append(klijst) 
    return rlijst

def aanvullen(rooster):
    r = len(rooster)
    k = len(rooster[0])
    assert (r+1)*(k+1) <= 52 and r>0 and k>0, 'ongeldig rooster'
    
    #alle getrokken kaarten in 1 lijst zetten
    getrokken = []
    for i,_ in enumerate(rooster):
        getrokken.extend(rooster[i])
    
    #voeg aan elke rij een kolom toe
    for rij in rooster:
        kaart = trekken(getrokken)
        rij.append(kaart)
        getrokken.append(kaart)
    
    #voeg nog 1 rij toe met k+1 kolommen
    laatsterij = []
    for _ in range(k+1):
        kaart = trekken(getrokken)
        laatsterij.append(kaart)
        getrokken.append(kaart)
    
    #upgrade het rooster, maar return niets
    rooster.append(laatsterij)
            
def aanduiden(rooster):
    r = len(rooster)
    k = len(rooster[0])
    return (random.randint(0,r-1), random.randint(0,k-1))
        
        
        
        
        