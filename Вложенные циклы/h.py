max_sum = 0
max_name = 0
n = int(input())
for i in range(n):
    name = input()
    number = input()
    number_sum = 0
    for y in number:
        number_sum += int(y)
    if max_sum <= number_sum:
        max_name = name
        max_sum = number_sum
print(max_name)
