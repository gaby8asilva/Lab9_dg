
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



# print(decoder("45678888"))
def main():
    encoded = ""
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")
        option = input("Please enter an option: ")

        if option == "1":
            password = input("Please enter your password to encode:")
            encoded = encoder(password)
            print("Your password has been encoded and stored!")
        elif option == "2":
            if encoded:
                print(f"The encoded password is {encoded}, and the original password is {decoder(encoded)}")
        elif option == "3":
            quit()

if __name__ == "__main__":
    main()