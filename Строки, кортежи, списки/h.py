n = int(input())
for i in range(n):
    text = input()
    a = text.find("зайка")
    if a != -1:
        print(a + 1)
    else:
        print("Заек нет =(")