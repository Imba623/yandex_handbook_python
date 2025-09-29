len_text = int(input())
n = int(input())
for i in range(n):
    text = input()
    if len(text) > len_text:
        print(text[0:len_text - 3] + "...")
    else:
        print(text)
