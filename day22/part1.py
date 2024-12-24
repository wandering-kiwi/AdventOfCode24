def evolve(n):
    s=n
    d_lst = [s%10]
    d_diff_lst = []
    for i in range(2000):#
        s = ((64*s)^s)%16777216
        s = ((s//32^s))%16777216
        s = ((2048*s)^s)%16777216
        d_diff_lst.append(s%10 - d_lst[-1])
        d_lst.append(s%10)
    print(d_diff_lst[-40])
    print(d_diff_lst[])
    print(d_lst[-37])
    return d_lst, d_diff_lst


# print(sum(list(map(lambda x: evolve(int(x)), open('input.txt', 'r')))))
evolve(1)