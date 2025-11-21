import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

# def coin_toss():
#     result=random.randint(0,1)
#     return result

# def random_emoji():
#     emojis=["😀","🙂","😐","😐","😟","😍","😎","😶","😴","😠"]
#     return random.choice(emojis)
