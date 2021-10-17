temp = input()
zomers = 0
tropisch = 0
tekst = 'geen hittegolf'

while temp != 'stop':
    temp = float(temp)
    if temp >= 25:
        zomers += 1
        if temp >= 30:
            tropisch += 1
        if zomers >= 5 and tropisch >= 3:
            tekst = 'hittegolf'
    else:
        zomers = 0
        tropisch = 0
    temp = input()

    
print(tekst)
