#input
t = round(float(input('t='))*100)
priemfactoren =[]

t_deling = t*10000
i = 2
while t_deling != 1:
    while (t_deling)%i != 0: 
        i +=1                                           
    t_deling = t_deling/i
    priemfactoren.append(i)

priemfactoren = list(set(priemfactoren))
print(priemfactoren)

a = 0
b = 0
c = 0
i = 0
j= 1
while (a*b*c != t*10000):
    a = priemfactoren[i] * j
    if i == (len(priemfactoren)-1):
        i=0
        j+=1
    if a> (t//2)+1:
        a =1
        b+= min(priemfactoren)
        i = 0
        j= 1
    c = t-a-b
    i+=1

t= float(t/100)
a= float(a/100)
b= float(b/100)
c= float(c/100)
print('${:.2f} + ${:.2f} + ${:.2f} = ${:.2f} x ${:.2f} x ${:.2f} = ${:.2f}'.format(a, b, c, a, b, c, t))


