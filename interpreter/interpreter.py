x, y, z = input("Expresion: ").split()

if y == "+":
    print(float(x) + float(z))
elif y == "-":
    print(float(x) - float(z))
elif y == "*":
    print(float(x) * float(z))
elif y == "/":
    if int(z) != 0:
        print(float(x) / float(z))
    else:
        print("Devision by zero.")