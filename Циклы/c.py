s = int(input())
f = int(input())
answer = ''
fanaly = False

for i in range(s, f + 1):
    if i == f:
        fanaly = True
    answer += str(i)
    if not fanaly:
        answer += ' '

print(answer)