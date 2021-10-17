#input
t = round(float(input('t='))*100)
delers =[]

t_deling = t*10000
i = 1
while i<t:
    if (t_deling)%i == 0:
        delers.append(i)  
    i +=1

a = 0
b = 0
c = 0
i = 0
j= 0
while (a*b*c != t*10000):
    b = delers[i]
    a = delers[j]
    c = t-a-b
    if i == (len(delers)-1):
        i=-1
        j+=1
    i+=1

t= float(t/100)
a= float(a/100)
b= float(b/100)
c= float(c/100)
print('${:.2f} + ${:.2f} + ${:.2f} = ${:.2f} x ${:.2f} x ${:.2f} = ${:.2f}'.format(a, b, c, a, b, c, t))
