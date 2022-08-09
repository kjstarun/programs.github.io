# to sort in ascending order

def rev(l):
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]
    return l
l = [10, 56, 67, -45, -2, 55, 78, 56, -4, 100, 200, 45]
print("The sorted array is",rev(l))
