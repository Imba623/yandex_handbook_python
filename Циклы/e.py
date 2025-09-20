count = 0

while (prise := float(input())) != 0:
    if prise >= 500:
        count += prise - prise / 100 * 10
    else:
        count += prise

print(count)