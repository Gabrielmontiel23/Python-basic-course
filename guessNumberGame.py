import random
def lives(life):
    print("lives: "+"๐"*life)
def guess_number(number):
    pass
def run():
    print("""Welcome!๐น๐ฎ 
This is a game where you must to guess the number that your computer chooses, you have just 5 lives so take care ๐.
     ๐ด
     ๐ก
     ๐ข
ยกLet's start!""")
    random_number=random.randint(1, 100)
    life=5
    number=int(input("Choose a number from 1 to 100: "))
    on=True
    while on:
        if number<random_number and life>0:
            lives(life)
            number=int(input("Choose a bigger number: "))
            life-=1
        elif number>random_number and life>0:
            lives(life)
            number=int(input("Choose a smaller number: "))
            life-=1
        elif number==random_number and life>=0:
            print("You Win! ๐#1๐๐ฅณ")
            on=False
        else:
            print("""You lost ๐ 
the number was '{}'
don't worry, try again, you can win ๐ช๐ป""".format(random_number))
            on=False
if __name__=="__main__":
    run() 