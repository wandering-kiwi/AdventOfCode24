print(sum((lambda y: [abs(y[1][j]- y[0][j]) for j in range(len(y[0]))])((lambda x: [sorted(x[::2]), sorted(x[1::2])])([int(i) for i in open("input.txt", "r").read().split()]))))
