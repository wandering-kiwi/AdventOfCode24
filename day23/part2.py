connections = [set(line.strip().split('-')) for line in open('input.txt', 'r')]
commons = [list(filter(lambda x: any(x&pair) and not x==pair, connections)) for pair in connections]
triplets = []
for i in range(len(commons)):
    for j in commons[i]:
        flipped = list(map(lambda y: y^connections[i], commons[i]))
        if j in flipped and any(k[0]=='t' for k in j):
            triplet = j|connections[i]
            if not triplet in triplets:
                triplets.append(triplet)
print(len(triplets))