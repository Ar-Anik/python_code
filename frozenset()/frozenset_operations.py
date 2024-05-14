# Two sets are said to be disjoint sets if they have no element in common.

a = frozenset([1, 2, 3, 4])
b = frozenset([3, 4, 5, 6])
c = frozenset([5, 6])

d = a.copy()
print(d)

print(a.union(b))

print(a.intersection(b))

print(a.symmetric_difference(b))

print(a.isdisjoint(c))

print(c.issubset(b))

print(b.issuperset(c))
