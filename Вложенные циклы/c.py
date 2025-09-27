max_number = int(input())
row = 1 
col = 1  
number = 1 
while number <= max_number:
    while col <= row and number <= max_number:
        print(number, end=' ')  
        col += 1  
        number += 1  
    print()
    row += 1
    col = 1
