# not actually attempted yet
puzzle_in=[line.split() for line in open('input.txt', 'r')]
wires = dict((i[0][:-1], int(i[1])) for i in puzzle_in[:90])
gates = puzzle_in[91:]
while gates:
    for gate in gates:
        try:
            match gate[1]:
                case 'AND':
                    wires[gate[-1]] = wires[gate[0]] & wires[gate[2]]
                case 'OR':
                    wires[gate[-1]] = wires[gate[0]] | wires[gate[2]]
                case 'XOR':
                    wires[gate[-1]] = wires[gate[0]] ^ wires[gate[2]]
            gates.remove(gate)
        except:
            pass
print(int(''.join(map(lambda y: str(wires[y]), sorted(filter(lambda x: x[0]=='z', wires))))[::-1], 2))