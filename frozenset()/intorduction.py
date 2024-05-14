"""
Frozen set is just an immutable version of a Python set object. While elements of a set can be modified at any time,
elements of the frozen set remain the same after creation.

But like sets, it is not ordered.

The frozenset() function returns an immutable frozenset. If no parameters are passed, it returns an empty frozenset.

However, you won't be able to access values using the keys from a frozenset, as they are not stored in any particular order.

"""

vowels = ('a', 'e', 'i', 'o', 'u')

fzset = frozenset(vowels)
print(fzset)

empty_fzset = frozenset()
print(empty_fzset)

fzset.add('v')
