gro = {}

while True:
    try:
        item = input().strip().upper()

    except EOFError:
        break

    if item in gro:
        gro[item] += 1
    else:
        gro[item] = 1

si = sorted(gro.keys())

for item in si:
    print(f"{gro[item]} {item}")
