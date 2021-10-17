import csv
import math


def coordinaten(bestand):
    '''
    >>> coords = coordinaten('luchthavens.csv')
    >>> len(coords)
    9187
    >>> type(coords)
    <class 'dict'>
    >>> coords['BRU']
    (50.902222, 4.485833)
    >>> coords['CDG']
    (49.016667, 2.55)
    >>> coords['DCA']
    (38.851944, -77.037778)
    >>> coords['LAX']
    (33.9425, -118.407222)
    '''
    c = csv.reader(open('luchthavens.csv', 'r', encoding="ISO-8859-1"))
    return {rij[0]: (float(rij[5]), float(rij[6])) for rij in c}


def haversine(co1, co2):
    '''
    >>> haversine((50.902222, 4.485833), (49.016667, 2.55)) # BRU <-> CDG
    251.2480027355068
    >>> haversine((38.851944, -77.037778), (33.9425, -118.407222)) # DCA <-> LAX
    3710.8262543589817
    '''
    b1, l1 = co1
    b2, l2 = co2
    b1, l1, b2, l2 = math.radians(b1), math.radians(
        l1), math.radians(b2), math.radians(l2)
    a = (math.sin((b2-b1)/2))**2 + math.cos(b1) * \
        math.cos(b2) * (math.sin((l2-l1)/2))**2
    c = math.atan(math.sqrt(a/(1-a)))
    return 2*c*6371


def afstandVanafLuchthaven(luchthaven, coords):
    '''
    luchthaven is de drielettercode van de luchthaven
    output is een dictionary met steeds <luchthavencode>:<afstand tot gegeven luchthaven>
    '''
    return {key: haversine(coords[luchthaven], b) for key, b in coords.items()}


def algoritme(a, b, coords, actieradius=1000):
    '''
    >>> coords = coordinaten('luchthavens.csv')
    >>> algoritme('DCA', 'LAX', coords, actieradius=2000)
    'DDC'
    >>> algoritme('DCA', 'LAX', coords, actieradius=1000)
    'MTO'
    >>> algoritme('HLC', 'LAX', coords, actieradius=1000)
    'BFG'
    '''
    da = afstandVanafLuchthaven(a, coords)  # codes:afstanden voor a
    assert min(da.values()) <= actieradius, 'geen mogelijke route'
    luchthavens_in_ar = [x for x in da.keys() if da[x] <= actieradius]
    luchthavens_in_ar_afstanden_tot_b = [
        haversine(coords[e], coords[b]) for e in luchthavens_in_ar]
    # neem de minimale afstand tot b, zoek de index ervan op in de lijst, en zoek die index op in de corresponderende namenlijst
    return luchthavens_in_ar[luchthavens_in_ar_afstanden_tot_b.index(min(luchthavens_in_ar_afstanden_tot_b))]


def vliegplan(vertrek, aankomst, coords, actieradius=1000):
    '''
    >>> coords = coordinaten('luchthavens.csv')
    >>> vliegplan('DCA', 'LAX', coords)
    ['DCA', 'MTO', 'HLC', 'BFG', 'LAX']
    >>> vliegplan('DCA', 'LAX', coords, actieradius=2000)
    ['DCA', 'DDC', 'LAX']
    >>> vliegplan('DCA', 'LAX', coords, actieradius=4000)
    ['DCA', 'LAX']
    >>> vliegplan('BRU', 'CDG', coords)
    ['BRU', 'CDG']
    >>> vliegplan('BRU', 'CDG', coords, actieradius=50)
    Traceback (most recent call last):
    AssertionError: geen mogelijke route
    '''

    outputlijst = [vertrek]
    while outputlijst[-1] != aankomst:
        assert algoritme(outputlijst[-1], aankomst, coords,
                         actieradius) not in set(outputlijst), 'geen mogelijke route'
        outputlijst.append(
            algoritme(outputlijst[-1], aankomst, coords, actieradius))
    return outputlijst


coords = coordinaten('luchthavens.csv')
print(vliegplan('BRU', 'LAX', coords, 1000))
