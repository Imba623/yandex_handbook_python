a = int(input())
b = int(input())
c = a
d = b
while b:
    a, b = b, a % b

print(d * c // a)
