# Rachel Shaw - 1.3 Assignment part 1 - 01/23/14
# The purpose of this program is to mimick the "bottles of beer song" using a number of bottles provided by the user. 

def main():

    #Recursive function counting bottles of beer. 
    def bottle_song(bottles):
        if bottles > 1:
            print(f'{bottles} bottles of beer on the wall, {bottles} bottles of beer.')
            print(f'Take one down, pass it around, {bottles - 1} bottles of beer on the wall')
            # For aesthetic purposes, makes output neater
            print(' ')
            bottles = bottles - 1
            bottle_song(bottles)

        # Changes sentance from plural to singular if bottles = 1
        elif bottles == 1:
            print("1 bottle of beer on the wall, 1 bottle of beer")
            print("Take one down, pass it around, 0 bottles of beer on the wall")
            print(' ')
            bottles = bottles - 1
            bottle_song(bottles)

        # Changes output if there are no bottles left on the wall
        else:
            print("Time to buy more bottles of beer")

    #Asks user for the number of bottles and sends it as an argument to the bottle song function 
    starting_bottles = int(input("Enter number of bottles"))
    bottle_song(starting_bottles)

    

main()