vowels = "AaEeIiOoUu"
word = input("Input: ")
result = ""

for c in word:
    if vowels.find(c) == -1:
        result += c

print("Output:", result)