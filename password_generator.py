import random
import string

def randomPassword():
    UPPERCASE = tuple(string.ascii_uppercase)
    LOWERCASE = tuple(string.ascii_lowercase)
    NUMS = tuple(string.digits)
    CHARS = tuple(string.punctuation)
    characters=UPPERCASE+LOWERCASE+NUMS+CHARS
    password=[]
    for i in range(15):
        random_character=random.choice(characters)
        password.append(random_character)
    password="".join(password)
    return password


def run():
    password=randomPassword()
    print("""Hello 😄👋🏻
I'm your password generator.
Your password is: {}""".format(password))


if __name__=="__main__":
    run()