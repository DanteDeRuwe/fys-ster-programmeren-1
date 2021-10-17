# gegeven wordt 2 coordinaten van een schaakspel
#het programma bepaalt of een paardensprong van a naar b mogelijk is


#input
pos_1 = input()
pos_2 = input()

#input splitten
letter_pos_1 = pos_1[0]
cijfer_pos_1 = int(pos_1[1])
letter_pos_2 = pos_2[0]
cijfer_pos_2 = int(pos_2[1])

#letters naar cijfers
letter_naar_cijfers_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
letter_pos_1_naar_cijfer = int(letter_naar_cijfers_dict[letter_pos_1])
letter_pos_2_naar_cijfer = int(letter_naar_cijfers_dict[letter_pos_2])

# coordinatenkoppels testen
if      ((letter_pos_1_naar_cijfer == letter_pos_2_naar_cijfer +2) or (letter_pos_1_naar_cijfer == letter_pos_2_naar_cijfer -2)) and ((cijfer_pos_1 == cijfer_pos_2 +1) or  (cijfer_pos_1 == cijfer_pos_2 -1)):
    
    kunnen = 'can'

elif      ((letter_pos_1_naar_cijfer == letter_pos_2_naar_cijfer +1) or (letter_pos_1_naar_cijfer == letter_pos_2_naar_cijfer -1)) and ((cijfer_pos_1 == cijfer_pos_2 +2) or (cijfer_pos_1 == cijfer_pos_2 -2)):
    
    kunnen = 'can'
    
else: kunnen = 'cannot'


print('a knight', kunnen, 'jump from', pos_1, 'to', pos_2)