def evolve(n):
    s=n
    for i in range(2000):#
        s = ((64*s)^s)%16777216
        s = ((s//32^s))%16777216
        s = ((2048*s)^s)%16777216
    return s


print(sum(list(map(lambda x: evolve(int(x)), open('input.txt', 'r')))))