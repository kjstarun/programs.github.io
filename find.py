# to find 3rd element

def findsmall(k,l):
    l.sort()
    a = l[k-1]
    return a
def findbig(k,l):
    l.sort()
    b = l[-k]
    return b
l = [10, 56, 67, -45, -2, 55, 78, 56, -4, 100, 200, 45]
k = int(input())
print("Minimum element of position",k,"is",findsmall(k,l))
print("Maximum element of position",k,"is",findbig(k,l))