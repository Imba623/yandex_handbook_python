text = input()
while text != "":
    comment = text.find("#")
    if comment == -1:
        print(text)
    elif comment != 0:
        print(text[:comment])
    text = input()
