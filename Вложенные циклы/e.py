n = int(input())
count_z = 0
flag = True
for i in range(n):
    while (text := input()) != "ВСЁ":
        if text == "зайка" and flag:
            count_z += 1
            flag = False
    flag = True
print(count_z)
