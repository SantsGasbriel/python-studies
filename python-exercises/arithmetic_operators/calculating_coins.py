money = float(input("How much money do you have in your wallet ? R$ "))
dolar = money / 5.06
euro = money / 5.48
print(f"Whit R${money} you can buy US${round(dolar,2)}")
print(f"Whit R${money} you can buy Є${round(euro,2)}")