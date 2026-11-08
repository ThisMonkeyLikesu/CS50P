var_name = input("camelCase: ")
snake_case = ""

for c in var_name:
    if c.islower():
        snake_case += c
    else:
        snake_case += "_"
        snake_case += c.casefold()

print("snake_case:", snake_case)