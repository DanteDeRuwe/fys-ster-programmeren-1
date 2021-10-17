def isKlinker(letter):
    
    if letter.lower() in ('a', 'e', 'i', 'o', 'u'):
        klinker = True
    else:
        klinker = False
    return klinker

woord = input('woord')
klinkergroep = ''
output = ''
for i, letter in enumerate(woord):
    if isKlinker(letter):
        klinkergroep += letter
    if not isKlinker(letter) or i == (len(woord)-1):
        if len(klinkergroep) > 0:
            if klinkergroep[0].isupper():
                output += 'Ab'+ (klinkergroep[0]).lower() + klinkergroep[1:]
            else:
                output += 'ab' + klinkergroep
        if i != (len(woord)-1):
            output += letter
        klinkergroep = ''
print(output)