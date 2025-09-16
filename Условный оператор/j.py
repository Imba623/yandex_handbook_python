number = input()
a = int(number[2]) + int(number[1])
b = int(number[1]) + int(number[0])

if a >= b:
    answer = str(a) + str(b)
else:
    answer = str(b) + str(a)

print(answer)