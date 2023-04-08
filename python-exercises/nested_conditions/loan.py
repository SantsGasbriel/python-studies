value = float(input("\033[1mHouse value: "))
wage = int(input("\033[1mBuyer's salary: "))
financing = int(input("\033[1mHow many years of financing: "))
installment_value = (value) / (financing * 12 )
print(f"\033[1mTo pay off a house of {value} in {financing} years the installment will be {round(installment_value,2)}.")
if installment_value > (30 * wage) / 100:
    print("\033[1mLoan denied!")
else:
    print("\033[1mLoan can be granted!")