
# gabriela ochoa-silva
def encoder(password):
    if len(password) != 8:
        return False
    new_password = ""
    for char in password:
        new_digit = int(char) + 3
        if new_digit > 9:
            new_digit = new_digit - 10
        new_password += str(new_digit)
    return new_password


# print(encoder("12345555"))
#DANA JIMENEZ
def decoder(new_password):
    decoded_password = ""
    for digit in new_password:
        decoded_digit = str((int(digit) - 3))
        decoded_password += decoded_digit
    return decoded_password.replace("-", "").replace(" ", "")



# print(decoder("45678888"))
def main():
    new_password = ""
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")
        option = input("Please enter an option: ")

        if option == "1":
            password = input("Please enter your password to encode: ")
            new_password = encoder(password)
            print("Your password has been encoded and stored!")
        elif option == "2":
            if new_password:
                print(f"The encoded password is {new_password}, and the original password is {decoder(new_password)}")
        elif option == "3":
            quit()

if __name__ == "__main__":
    main()