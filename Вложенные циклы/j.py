count = int(input())
print("А Б В")
for a in range(1, count):
    for b in range(1, count):
        for c in range(1, count):
            if a + b + c == count:
                print(a, b, c)
