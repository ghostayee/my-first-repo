phone_number = input("Enter your phone number: ")
if phone_number.startswith("07") and len(phone_number) == 10:
    print(f"+254{phone_number[1:]}")
elif phone_number.startswith("7") and len(phone_number) == 9:
    print(f"+254{phone_number}")
elif phone_number.startswith("254") and len(phone_number) == 12:
    print(f"+{phone_number}")
elif phone_number.startswith("01") and len(phone_number) == 10:
    print(f"+254{phone_number[1:]}")
elif phone_number.startswith("+254") and len(phone_number) == 13:
    print("phone_number")
else:
    print("Not a valid number")