stones = dict((i, 1) for i in [line for line in open('input.txt', 'r')][0].split())
for count in range(100000):
    print(count)
    temp_dict = {}
    for stone, reps in stones.items():
        temp_lst = []
        if stone=='0':
            temp_lst.append('1')
        elif len(stone)%2==0:
            temp_lst.append(stone[:len(stone)//2])
            temp_lst.append(str(int(stone[len(stone)//2:])))
        else:
           temp_lst.append(str(int(stone)*2024))
        
        for j in temp_lst:
            if j in temp_dict:
                temp_dict[j] += reps
            else:
                temp_dict[j] = reps
    stones = temp_dict
print(sum(n for n in stones.values()))



