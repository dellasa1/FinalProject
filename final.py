import random

score = 0
playing = True
while playing:
    flip = input("Enter 'heads' or 'tails': ")
    coin = random.randint(1, 2)
    print(coin)
    if flip == 'heads':
        if coin == 1:
            print("That's correct!")
            score+=1
        if coin == 2:
            print("That's incorrect!")
            playing = False
    if flip == 'tails':
        if coin == 1:
            print("That's incorrect!")
            playing = False
        if coin == 2:
            print("That's correct!")
            score+=1
print('Your score is ', score)
