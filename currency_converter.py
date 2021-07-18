print("Welcome!\nThis program is a currency converter.")
print("Choose the currency you want to convert:\n 1. Colombian pesos to US dollars\n 2. US dollars to Colombian pesos")
menu=float(input("Type '1' or '2': "))
if menu == 1:
    colombian_pesos=float(input("How many Colombian pesos do you have?: $"))
    dollars=round(colombian_pesos/3815.33,2)
    print("${} dollars".format(dollars))
else:
    dollars=float(input("How many US dollars do you have?: $"))
    colombian_pesos=round(dollars/0.0002621,2)
    print("${} pesos".format(colombian_pesos))