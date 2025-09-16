p = int(input())
v = int(input())
t = int(input())

#
if p > v > t:
    print('''1. Петя
2. Вася
3. Толя
''')

elif p > t > v:
    print('''1. Петя
2. Толя
3. Вася
''')

elif t > v > p:
    print('''1. Толя
2. Вася
3. Петя
''')

elif t > p > v:
    print('''1. Толя
2. Петя
3. Вася
''')

elif v > p > t:
    print('''1. Вася
2. Петя
3. Толя
''')

elif v > t > p:
    print('''1. Вася
2. Толя
3. Петя
''')