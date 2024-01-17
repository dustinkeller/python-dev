import re

email_checker = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

string = "dustin.w.keller@gmail.com"

print(email_checker.fullmatch(string))