y = 0
x = 0

while (where := input()) != "СТОП":
    way = int(input())
    if where == "СЕВЕР":
        y += way
    elif where == "ЮГ":
        y -= way
    elif where == "ВОСТОК":
        x += way
    elif where == "ЗАПАД":
        x -= way


print(y)
print(x)