f = int(input())
answer = 1
if f == 0 or f == 1:
    print(1)
else:
    for i in range(2, f + 1):
        answer *= i
    print(answer)