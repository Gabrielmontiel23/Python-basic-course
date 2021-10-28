def currency_converter_pesos(currency,dollar_value):
    pesos=float(input("How many {} do you have?: $".format(currency)))
    dollars=round(pesos/dollar_value, 2)
    print("💲{} dollars".format(dollars))
def currency_converter_US(currency,peso_value):
    dollars=float(input("How many US dollars do you have?: $"))
    pesos=round(dollars/peso_value, 2)
    print("💲{} {}".format(pesos, currency))
print("""Welcome 😄❕
This program is a currency converter 💸💰💵
Choose the currency you want to convert:
1-Colombian pesos to US dollars
2-US dollars to Colombian pesos
3-Argentine pesos to US dollars
4-US dollars to Argentine pesos
5-Mexican pesos to US dollars
6-US dollars to Mexican pesos
7-Exit""")
on=True
while on:
    option=input("Type the number of the option: ")
    if option == "1":
        currency_converter_pesos("Colombian pesos", 3814)
    elif option == "2":
        currency_converter_US("Colombian pesos", 0.0002621919)
    elif option == "3":
        currency_converter_pesos("Argentine pesos", 96)
    elif option == "4":
        currency_converter_US("Argentine pesos", 0.010416)
    elif option == "5":
        currency_converter_pesos("Mexican pesos", 20)
    elif option == "6":
        currency_converter_US("Mexican pesos", 0.05)
    elif option == "7":
        on=False
    else:
        print("*ERROR* You must type a number from 1 to 7 depending on the option.")
print("Bye👋🏻, see you later😊.")