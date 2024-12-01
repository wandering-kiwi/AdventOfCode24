print(sum((lambda y: [j*y[1].count(j) for j in y[0]])((lambda x: [x[::2], x[1::2]])([int(i) for i in open("input.txt", "r").read().split()]))))
