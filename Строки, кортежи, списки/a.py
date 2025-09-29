count = 0
n = int(input())
for i in range(n):
    text = input().lower()
    if text[0] == "а" or text[0] == "б" or text[0] == "в":
        count += 1

if count == n:
    print("YES")
else:
    print("NO")