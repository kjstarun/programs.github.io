def door(n):
    if n % 3 == 0 and n % 5 == 0:
        print("Hello Tarun")
    elif n % 3 == 0:
        print("Hello")
    elif n % 5 == 0:
        print("Tarun")
    else:
        print("Inavlid Input")
n = int(input())
door(n)