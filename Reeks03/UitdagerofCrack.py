ronden = int(input())
score_u = 0
score_c = 0

for _ in range(ronden):
    opl = input()
    uitdager = input()
    crack = input()
    
    if opl == uitdager:
        score_u += 1
        if crack == 'juist':
            score_c += 1
    else: 
        if crack == 'fout':
            score_c += 1
            
if score_u > score_c or score_c < ronden/2:   
    print('uitdager wint met {} punten tegen {}'.format(score_u, score_c))
elif score_u < score_c:
    print('crack wint met {} punten tegen {}'.format(score_c, score_u))
else: print('ex aequo: beide deelnemers hebben {} punten'.format(score_c))

    