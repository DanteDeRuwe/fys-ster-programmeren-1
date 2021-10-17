#input
n = int(input())

#initiele waarden
lowercase = 0
uppercase = 0
foute_cijfers = 0

for i in range(n):
    regel = input()     #n regels opvragen
    output = ''         # bij elke nieuwe regel strings resetten
    string = ''
    for karakter in regel:
        if karakter.islower():      #als kleine letter
            lowercase += 1          #count
            string += karakter      #breid string uit
        elif karakter.isupper():        #als hoofdletter
            uppercase += 1              #count
            string += karakter          #breid string uit
        elif karakter.isdigit():            #als getal
            if int(karakter) < 5:           #als cijfer < 5 dan is het fout
                foute_cijfers += 1          #count
            string += karakter              #bereid de string uit
        else:                                                                           #als spatie of ander teken
            if ((lowercase != 0) and (uppercase != 0)) or (foute_cijfers != 0):         #als de string niet ok is
                string = (len(string))*'.'                                                  #vervang door puntjes
            output += string + '.'      # als de string ok is, definieer output als de string plus 1 puntje (de spatie)
            string = ''                                                                 #reset strings en counters
            lowercase = 0
            uppercase = 0
            foute_cijfers = 0
    if ((lowercase != 0) and (uppercase != 0)) or (foute_cijfers != 0):                 #als op einde regel string niet ok is
        string = (len(string))*'.'                                                          #vervang door puntjes
    output += string                                                                    #voeg toe aan output
    print(output)