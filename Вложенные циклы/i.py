n = int(input())
max_numbers = ''
for i in range(n):
    number = input()
    max_number = 0
    for y in number:
        y_int = int(y)
        if max_number < y_int:
            max_number = y_int
    max_numbers += str(max_number)
print(max_numbers)
