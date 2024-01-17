import re
#password checker:
# At least 8 chars long
# numbers, lettes, and $%#@ symbols

checker = re.compile(r"[a-zA-z\d@#$%]{7,}\d")

while True:
    password = input("Enter your password: ")
    if checker.fullmatch(password):
        break
    print("Please ensure your password meets the requirements and try again...")
    continue
print("Success!")
