#invoer voor n opvragen
n = int(input())

#de beginwaarde van een variabele vastleggen
max_hoogte_int = 0

#vraag n keer een input op
for i in range(n): #we houden i bij want als i = 0 is de uitvoer speciaal, nl. 'gelijkvloers'
    gebouw_str = input()
    hoogte_int = int(input())
    #als een gebouw hoger is dan de hoogste die we al zijn tegengekomen
    if hoogte_int > max_hoogte_int:
        #zichtbaarheid van het gebouw begint bij het vorige hoogste gebouw
        vorige_max_hoogte = max_hoogte_int
        #nieuwe max hoogte is de hoogte van dit gebouw
        max_hoogte_int = hoogte_int
        #print de uitvoer, rekening houdende met 'het gelijkvloers'
        print('{} is zichtbaar van {} tot {} meter.'.format(gebouw_str, 'het gelijkvloers' if i == 0 else str(vorige_max_hoogte) + ' meter', hoogte_int))
