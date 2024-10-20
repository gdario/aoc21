with open('input1.txt', 'r') as fh:
    lines = [line.strip() for line in fh]

# Reduction: while either is true (return boolean)
# Any pair nested inside 4 pairs? -> leftmost such pair explodes.
# Any number >= 010? Leftmost such number splits.

# ---------- Explode ----------
# To explode a pair, the pair's left value is added to the first
# regular number to the left of the exploding pair (if any), and the
# pair's right value is added to the first regular number to the right
# of the exploding pair (if any). Exploding pairs will always consist
# of two regular numbers. Then, the entire exploding pair is replaced
# with the regular number 0.

# ---------- Split ----------
# To split a regular number, replace it with a pair; the left element
# of the pair should be the regular number divided by two and rounded
# down, while the right element of the pair should be the regular
# number divided by two and rounded up. For example, 10 becomes [5,5],
# 11 becomes [5,6], 12 becomes [6,6], and so on.

# ---------- Magnitude ----------
# The magnitude of a pair is 3 times the magnitude of its left element
# plus 2 times the magnitude of its right element. The magnitude of a
# regular number is just that number. Magnitude calculations are recursive.

# Question: possible to calculate the magnitude without going back to a tree?

# Use assertion on the example cases. For example, for explode
# l1 = flatten('[[[[[9,8],1],2],3],4]')
# l2 = flatten('[[[0,9],2],3],4]')
# assert explode(l1) == l2
