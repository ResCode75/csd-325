
def main():

    def bottle_song(bottles):
        if bottles > 1:
            print(f'{bottles} bottles of beer on the wall, {bottles} bottles of beer.')
            print(f'Take one down, pass it around, {bottles - 1} bottles of beer on the wall')
            print(' ')
            bottles = bottles - 1
            bottle_song(bottles)

        elif bottles == 1:
            print("1 bottle of beer on the wall, 1 bottle of beer")
            print("Take one down, pass it around, 0 bottles of beer on the wall")
            print(' ')
            bottles = bottles - 1
            bottle_song(bottles)

        else:
            print("Time to buy more bottles of beer")

    starting_bottles = int(input("Enter number of bottles"))
    bottle_song(starting_bottles)

    

main()