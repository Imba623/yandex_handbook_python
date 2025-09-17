s = int(input())
f = int(input())
step = 1
if s > f:
    step = -1
    f -= 2
if s == f + 1 or s == f - 1:
    print(s, f)
else:
    f += 1
    answer = ''
    fanaly = False

    for i in range(s, f, step):
        if i == f - 1 and step == 1 or i == f + 1 and step == -1:
            fanaly = True
        answer += str(i)
        if not fanaly:
            answer += ' '

    print(answer)