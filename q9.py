password = input("Enter a password: ")

has_upper_letter = False
has_lower_letter= False
has_digit_letter = False

if len(password) >= 8:

    for char in password:
        if char.isupper():
            has_upper_letter = True
        elif char.islower():
            has_lower_letter = True
        elif char.isdigit():
            has_digit_letter = True


if has_upper_letter and has_lower_letter and has_digit_letter:
    print("Valid password")
else:
    print("Invalid password")
