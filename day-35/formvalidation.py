
'''
import re
fullname = input("Enter the name:")
pattern = r'^[A-Za-z]{2,25}([A-Za-z]{2,25})+$'

res = re.fullmatch(pattern,fullname)
print("valid full name" if res else "invalid full name")
'''

import re
email = input("Enter the email:")
pattern = r'^[a-zA-Z0-9._]+@[a-zA-Z0-9._]+\[a-zA-Z]{2,}$'

res = re.fullmatch(pattern,email)
print("valid email" if res else "invalid email")

import re
phonenumber = input("Enter the phonenumber:")
pattern = r'^(?:\+91|0)?[6-9]\d{9}$'

res = re.fullmatch(pattern,phonenumber)
print("valid phonenumber" if res else "invalid phonenumber")

import re
password= input("Enter the password: ")
pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}'

res = re.fullmatch(pattern,password)
print("valid password" if res else "invalid password")
