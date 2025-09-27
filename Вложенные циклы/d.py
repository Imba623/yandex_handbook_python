count = int(input())
result = 0
for i in range(count):
    text = input()
    for i in text:
        result += int(i)
print(result)