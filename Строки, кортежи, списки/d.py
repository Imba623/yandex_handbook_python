while (text := input()) != "":
    if text[-1] == '@' and text[-2] == '@' and text[-3] == '@':
        pass
    elif text[0] == '#' and text[1] == '#':
        print(text[2:])
    else:
        print(text)
