def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    has_digit = 0
    if s.isalnum() != True:
        return False
    if (len(s) < 2) or (len(s) > 6):
        return False
    if s[0:2].isalpha() != True:
        return False
    for c in s:
        if (c.isdigit()) and (has_digit == 0):
            if int(c) == 0:
                return False
            has_digit = 1
        if (c.isalpha()) and (has_digit == 1):
            return False
    return True
main()