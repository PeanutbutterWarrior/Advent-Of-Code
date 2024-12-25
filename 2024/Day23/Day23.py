import sys
from collections import defaultdict
from copy import copy

def BronKerbosch(P, X, *R):
    if len(P) == 0 and len(X) == 0:
        global max_clique
        if len(R) > len(max_clique):
            max_clique  = R
        return
    for v in copy(P):
        BronKerbosch(P & comps[v], X & comps[v], *R, v)
        P.remove(v)
        X.add(v)

with open(sys.argv[1], "r") as file:
    data = file.read().strip()

comps = defaultdict(set)

for line in data.split("\n"):
    a, b = line.split("-")
    comps[a].add(b)
    comps[b].add(a)

seen = set()
for letter in 'abcdefghijklmnopqrstuvwxyz':
    first = "t" + letter
    connected = comps[first]
    for other in connected:
        combined = comps[other] & connected
        for final in combined:
            seen.add(tuple(sorted((first, other, final))))
print(len(seen))

max_clique = set()
BronKerbosch(set(comps.keys()), set())
print(",".join(sorted(max_clique)))