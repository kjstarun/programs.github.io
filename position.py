#To find the position

def pos(a):
    for i in range(len(l)):
        if l[i] == a:
            r = i+1
            break
        else:
            r = -99999
    return r
l = [10, 56, 67, -45, -2, 55, 78, 56, -4, 100, 200, 45]
a = int(input())
print("The Position of the element",a,"is",pos(a))
