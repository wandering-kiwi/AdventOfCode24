plots = {n: {'area':0, 'peri':0} for n in 'OX'}
in_lst = [line.strip() for line in open('input.txt', 'r')]
for y, i in enumerate(in_lst):
    for x, j in enumerate(i):
        plots[j]['area'] += 1
        if y==0 or y==len(in_lst)-1:
            plots[j]['peri']+=1
            # print(j, plots[j]['peri'], x, y, 1)
        if x==0 or x==len(i)-1:
            plots[j]['peri']+=1
            # print(j, plots[j]['peri'], x, y, 2)
        try:
            right = i[x+1]
            if right != j:
                plots[j]['peri']+=1
                plots[right]['peri']+=1
                # print(j, plots[j]['peri'], x, y, 3)
        except:
            pass
        try:
            below = in_lst[y+1][x]
            if below != j:
                plots[j]['peri']+=1
                plots[below]['peri']+=1
                # print(j, plots[j]['peri'], x, y, 4)
        except:
            pass
print(plots)
print(sum([plots[k]['area']*plots[k]['peri'] for k in plots]))