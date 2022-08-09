# to reverse array

def rev(l):
    r = []
    s = []
    for i in range(1,len(l)+1):
        r = r + [l[-i]]
    return r
l = [10, 56, 67, -45, -2, 55, 78, 56, -4, 100, 200, 45]
print("The reversed array is",rev(l))
