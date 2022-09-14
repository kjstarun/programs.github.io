def asc(l):
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]
    return l
def duplicate(l):
    asc(l)
    r = []
    for i in l:
        if i not in r:
            r = r + [i]
    return r
l = [-10,1,-9,2,3,2,1,3,3,1,-10]
print("The unique elements are",duplicate(l))
