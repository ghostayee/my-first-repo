valid_mail = input("Enter your email: ")
if '@' in valid_mail and '.' in valid_mail:
    print(valid_mail)
elif valid_mail.endswith("@gmail.com"):
    print(valid_mail)
else:
    print("Enter a valid email")
