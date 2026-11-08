greeting = input("Greeting: ").split()[0]

if greeting.lower().find("hello") != -1:
    print("$0")
elif greeting.lower()[0] == "h" and greeting.lower().find("hello") == -1:
    print("$20")
else:
    print("$100")