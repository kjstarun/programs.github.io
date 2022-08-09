# to find 3rd element

def findsmall(k,l):
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]
    a = []
    for i in range(k):
        a = a + [l[i]]
    return a
def findbig(k,l):
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]
    b = []
    for i in range(1,k+1):
        b = b + [l[-i]]
    return b
l = [10, 56, 67, -45, -2, 55, 78, 56, -4, 100, 200, 45]
k = int(input())
print("Minimum element of position",k,"is",findsmall(k,l))
print("Maximum element of position",k,"is",findbig(k,l))
