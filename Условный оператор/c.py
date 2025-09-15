p = int(input())
v = int(input())
t = int(input())

m = max(p, v, t)

if m == p:
    print('Петя')
elif m == v:
    print('Вася')
elif m == t:
    print('Толя')