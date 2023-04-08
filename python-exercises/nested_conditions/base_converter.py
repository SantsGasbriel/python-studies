number = int(input("\033[1mEnter a number: "))
print('''\033[1mChoose one of the conversion options:
[1] Convert to binary.
[2] Converter to octal.
[3] Converter to hexadecimal.''')
option = int(input("\33[1mYour option: "))
if option == 1:
    print(f"\33[1m{number} converted to binary is {bin(number)[2:]}.")
elif option == 2:
    print(f"\33[1m{number} converted to octal is {oct(number)[2:]}.")
elif option == 3:
    print(f"\33[1m{number} converted to hexadecimal is {hex(number)[2:]}.")
else:
    print("\33[1mInvalid option!Try again!")