slogan = input()
p = int(input())
s = int(input())
gecodeerd = str(slogan[p])

for i in range(1, len(slogan)):
    pos = p + s*i
    if pos >= len(slogan) or pos <= len(slogan):
        pos %= len(slogan)
    gecodeerd += str(slogan[pos])

print(gecodeerd)
    
    