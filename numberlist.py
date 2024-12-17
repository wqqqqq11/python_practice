numberlist = []
a = 6

while True:
    if a % 2 == 0:
        a = a // 2
    else:
        a = (a * 3) + 1

    numberlist.append(a)

    if a == 1:
        break

print(numberlist)