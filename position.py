#To find the position

def pos(a):
    for i in l:
        if i == a:
            r = l.index(i)
    return r + 1
l = [10, 56, 67, -45, -2, 55, 78, 56, -4, 100, 200, 45]
a = int(input())
print(pos(a))