def palindrome_detector(word):
    word=word.strip().replace(" ", "").upper()
    reverse_word=word[::-1]
    if word==reverse_word:
        print(" It is a polindrome π₯³ππ»"+"'"+reverse_word.capitalize()+"'")
    else:
        print(" It isn't a palindrome πππ»"+"'"+reverse_word.capitalize()+"'")
def run():
    print("""Welcome! π
This program is a palindromes detector βπ».
Note π: A palindrome is a word or phrase that reads the same backwards and forwares, for example: 
 β 'Level'β‘'leveL'
 β 'Dad'β‘'daD'
 β 'A nut for a jar of tuna'β‘'anut fo raj a rof tun A'β‘'a nut for a jar of tunA'
Note π: If you want to close the program, type '0' or 'EXIT'.
Β‘Let's start! βπ»""")
    on=True
    while on:
        word=input("Enter a word or a sentence to tell you if it's a palindrome: ")
        if word=='0' or word=="EXIT":
            on=False
            print("Byeππ», see you laterπ.")
        else:
            palindrome_detector(word)
if(__name__=="__main__"):
    run()
