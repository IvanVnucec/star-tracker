with open('data/catalog.dat') as f:
    #lines = f.readlines()
    lines = [f.readline() for _ in range(1000)]

positions = [(float(line[153:164]), float(line[167:177])) for line in lines]

for pos in positions:
    print(pos)