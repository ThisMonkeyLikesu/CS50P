def main():
    phrase = input("What do you want to say? ")
    phrase = convert(phrase)
    print(phrase)


def convert(phrase:str)->str:
    return phrase.replace(":)", "🙂").replace(":(", "🙁")


main()