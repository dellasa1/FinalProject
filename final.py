import random
flip = input("Enter 'heads' or 'tails': ")

coin = random.randint(1, 2)
print(coin)

if flip == 'heads':
    if coin == 1:
        print("That's correct!")
    if coin == 2:
        print("That's incorrect!")
if flip == 'tails':
    if coin == 1:
        print("That's incorrect!")
    if coin == 2:
        print("That's correct!")
