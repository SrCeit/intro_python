import itertools

line = '-' * 49
print(line)
print("|    Nº   | isdigit | isdecimal | isnumeric | chr")
print(line)

for x in itertools.chain(range(1000), range(4969, 4978), range(8304, 11000)):
    char = chr(x)
    if(char.isdigit() or char.isdecimal() or char.isnumeric()):
        print('| {0:^6} | {1:^7} | {2:^9} | {3:^10} | {4:3} '.format( #{0:>6} indica el ancho y alinea a la derecha, < a la izquierda y ^ centra
            x,
            'T' if char.isdigit() else 'F',
            'T' if char.isdecimal() else 'F',
            'T' if char.isnumeric() else 'F',
            char
        )
    )

