g = int(input())

if g % 400 == 0:
    print('YES')
elif g % 4 == 0 and g % 100 != 0:
    print('YES')
else:
    print('NO')