text = input()
if len(text) % 2 == 0:
    a = len(text) // 2
    text1 = text[:a]
    text2 = text[a:]
    if text1 == text2[::-1]:
        print('YES')
    else:
        print('NO')
else:
    a = len(text) // 2
    text1 = text[:a]
    text2 = text[a + 1:]
    if text1 == text2[::-1]:
        print('YES')
    else:
        print('NO')