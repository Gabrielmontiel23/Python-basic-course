def primariety(number):
    number=int(number)
    counter=0
    for i in range(1, number+1):
        if (i==1 or i==number) and number!=1:
            continue
        if number%i==0:
            counter+=1
            break
    if counter==0:
        print(" It is a prime number 🥳")
    else:
        print(" It isn't a prime number 🙁")
def run():
    print("""Welcome! 😄
This program is a prime number detector 🔢
Note 👀: A prime number is a natural number greater than 1 that has only two distinct positive divisors: itself and 1, for example:
    ✏ 2
    ✏ 3
    ✏ 37
    ✏ 17
Note 👀: If you want to close the program, type '0' or 'EXIT'.
¡Let's start! ✍🏻""")
    on=True
    while on:
        number=input("Type a number to tell you if it's a prime number: ")
        if number=='0' or number=="EXIT":
            on=False
            print("Bye👋🏻, see you later😊.")
        else:
            primariety(number)  
if __name__=="__main__":
    run()
