# to find minimum and maximum

def mini(l):
    a = 0
    for i in range(len(l)):
        if l[i] < a:
            a = l[i]
    return a
def maxi(l):
    b = 0
    for i in range(len(l)):
        if l[i] > b:
            b = l[i]
    return b
l = [10, 56, 67, -45, -2, 55, 78, 56, -4, 100, 200, 45]
print("The minimum element in the array is",mini(l))
print("The maximum element in the array is",maxi(l))
