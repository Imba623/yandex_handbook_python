count = 0

while (s := input()) != 'Приехали!':
    if 'зайка' in s:
        count += 1
print(count)