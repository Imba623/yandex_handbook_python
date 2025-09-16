a = input()
b = input()
c = input()

if a < c and a < b:
    print(a)
elif c < a and c < b:
    print(c)
elif b < a and b < c:
    print(b)