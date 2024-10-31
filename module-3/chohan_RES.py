#Rachel Shaw - 3.2 assignment - 10/31/2024
# The purpose of this project is to model a brownfireld project by altering existing code mimicking the traditional Japanese game "Chohan"

# Original Program by Al Sweigart: https://nostarch.com/big-book-small-python-projects
    
# Changes made:
    # Changed input prompt from ">" to "RES:"
    # implemented a 10 dollar bonus if the player rolls a 7 or a 2
    # Increased house fee from 10% to 12%
    
import random, sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}

print('''Cho-Han, by Al Sweigart al@inventwithpython.com

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.

There is a 10 mon bonus if you roll a 7 or a 2!
''')


purse = 5000
while True:  # Main game loop.
    # Place your bet:
    print('You have', purse, 'mon. How much do you bet? (or QUIT)')
    while True:
        pot = input("RES:")
        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You do not have enough to make that bet.')
        else:
            # This is a valid bet.
            pot = int(pot)  # Convert pot to an integer.
            break  # Exit the loop once a valid bet is placed.

    # Roll the dice.
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the')
    print('dice and asks for your bet.')
    print()
    print('    CHO (even) or HAN (odd)?')

    # Let the player bet cho or han:
    while True:
        bet = input("RES:").upper()
        if bet != 'CHO' and bet != 'HAN':
            print('Please enter either "CHO" or "HAN".')
            continue
        else:
            break

    # Reveal the dice results:
    print('The dealer lifts the cup to reveal:')
    print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('    ', dice1, '-', dice2)
    

    # Determine whether player gets the 10 mon bonus
    if (dice1 + dice2 == 7) or (dice1 + dice2 == 2):
        print("You got the 10 mon bonus!")
        # add 10 mon bonus to purse 
        purse = purse + 10
    else:
        print("You didn't hit the bonus, but lets see if you won!")
    

    # Determine if the player won:
    rollIsEven = (dice1 + dice2) % 2 == 0
    if rollIsEven:
        correctBet = 'CHO'
    else:
        correctBet = 'HAN'
    playerWon = bet == correctBet

    # Display the bet results:
    if playerWon:
        print('You won! You take', pot, 'mon.')
        purse = purse + pot  # Add the pot from player's purse.
        #CHANGE: changed house fee from 10% to 12%
        print('The house collects a', pot * .12, 'mon fee.')
        purse = purse - (pot * .12)  # The house fee is 10%.
    else:
        purse = purse - pot  # Subtract the pot from player's purse.
        print('You lost!')

    # Check if the player has run out of money:
    if purse == 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        sys.exit()
