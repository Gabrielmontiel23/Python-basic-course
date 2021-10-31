def palindrome_detector(word):
    word=word.strip().replace(" ", "").upper()
    reverse_word=word[::-1]
    if word==reverse_word:
        print(" It is a polindrome 🥳👉🏻"+"'"+reverse_word.capitalize()+"'")
    else:
        print(" It isn't a palindrome 🙁👉🏻"+"'"+reverse_word.capitalize()+"'")
def run():
    print("""Welcome! 😄
This program is a palindromes detector ✍🏻.
Note 👀: A palindrome is a word or phrase that reads the same backwards and forwares, for example: 
 ✏ 'Level'➡'leveL'
 ✏ 'Dad'➡'daD'
 ✏ 'A nut for a jar of tuna'➡'anut fo raj a rof tun A'➡'a nut for a jar of tunA'
Note 👀: If you want to close the program, type '0' or 'EXIT'.
¡Let's start! ✍🏻""")
    on=True
    while on:
        word=input("Enter a word or a sentence to tell you if it's a palindrome: ")
        if word=='0' or word=="EXIT":
            on=False
            print("Bye👋🏻, see you later😊.")
        else:
            palindrome_detector(word)
if(__name__=="__main__"):
    run()
