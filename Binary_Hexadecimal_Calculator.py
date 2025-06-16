# Binary / Hexadecimal / Decimal Calculator

# Functions -

# Format binary string
def binary_format(input):
    space = " "
    binary = ""

    # Reverse binary string
    input = input[::-1]

    # Add 0 to string to make output padded correctly
    padding = len(input) / 4
    padding = padding - int(padding)

    if padding == 0.25:
        input = input + "000"
    elif padding == 0.5:
        input = input + "00"
    elif padding == 0.75:
        input = input + "0"

    # Add spaces to string every 4 characters
    for x in range(0, len(input), 4):
        binary += input[x:x + 4] + space

    # Remove extra space
    binary = binary[:-1]
    # Reverse binary string to correct way
    binary = binary[::-1]

    return binary


# Converting -

# Binary to x

def binary_hex(input):

    pass


def binary_dec(input):

    dec = 0

    for num in input:
        dec = dec*2 + int(num)

    return dec


# Dec to x

def dec_binary(input):

    binary = bin(int(input))

    return binary[2:]


def dec_hex(input):

    pass


# Main loop

print("Binary / Hexadecimal / Decimal Calculator")

print("Type 'convert' to convert between Binary, Hexadecimal, Decimal")

# print("Type 'calculate' to perform any calculations with Binary, Hexadecimal or Decimal values")

print("Type 'help' to display instructions")

print("Type 'quit' to exit")

start = True
convert = False

while start:

    user_input = input()

    if user_input.lower() == "quit":
        exit()

    elif user_input.lower() == "help":

        print("Binary / Hexadecimal / Decimal Calculator")

        print("Type 'convert' to convert between Binary, Hexadecimal, Decimal")

        print("Type 'calculate' to perform any calculations with Binary, Hexadecimal or Decimal values")

    elif user_input.lower() == "convert":
        start = False
        convert = True

        print("Binary to Decimal = btd")

        # print("Binary to Hexadecimal = bth")

        print("Decimal to Binary = dtb")

        # print("Decimal to Hexadecimal = dth")

        # print("Hexadecimal to Binary = htb")

        # print("Hexadecimal to Decimal = htd")

        while convert:

            user_input = input("What would you like to convert?")

            if user_input.lower() == "quit":
                exit()

            elif user_input.lower() == "help":

                print("Binary to Decimal = btd")

                # print("Binary to Hexadecimal = bth")

                print("Decimal to Binary = dtb")

                # print("Decimal to Hexadecimal = dth")

                # print("Hexadecimal to Binary = htb")

                # print("Hexadecimal to Decimal = htd")

# Binary To Decimal -

            elif user_input.lower() == "btd":

                while convert:

                    user_input = input(
                        "Enter Binary value to convert to Decimal:")

                    b_input = user_input.replace(" ", "")
                    valid_input = False

                    if user_input.lower == "quit":
                        exit()

                    for num in b_input:

                        if num == "0" or num == "1":

                            valid_input = True
                            print("valid")

                        else:

                            valid_input = False

                            print(
                                f"'{user_input}' is not a valid input. Try Again")

                            break

                    if valid_input:

                        print(
                            f"'{user_input}' as a decimal value is: {binary_dec(b_input)}")

                        start == True
                        convert == False
                        break

# Binary To Hexadecimal -

            elif user_input.lower() == "bth":
                pass

# Decimal to Binary -
            elif user_input.lower() == "dtb":

                while convert:

                    print("Enter Decimal value to convert to Binary :")

                    user_input = (input())

                    print(
                        f"{user_input} as a binary value is: {binary_format(dec_binary(user_input))}")

                    convert == False

# Decimal to Hexadecimal -

            elif user_input.lower() == "dth":
                pass

# Hexadecimal to Binary -

            elif user_input.lower() == "htb":
                pass

# Hexadecimal to Decimal -

            elif user_input.lower() == "htd":
                pass

# Invalid Input -

            else:
                print(f"'{user_input}' is not a valid input. Try Again")

                print("Type 'help' to display instructions")

    # elif user_input.lower() == "calculate":
    #     start = False
    #     pass

    # elif user_input.lower() == "help":

    #     print("Binary / Hexadecimal / Decimal Calculator")

    #     print("Type 'convert' to convert between Binary, Hexadecimal, Decimal")

    #     print("Type 'calculate' to perform any calculations with Binary, Hexadecimal or Decimal values")

    #     print("Type 'help' to display instructions")

    # else:
    #     print(f"'{user_input}' is not a valid input. Try Again")
