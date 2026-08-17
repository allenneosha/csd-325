# Neosha Allen
# 8/16/26
# Assignment 1.3
# This program demonstrates a reverse counting of 100 bottles of beer
# on the wall, which allows a user to input how many bottles of
# beers on the wall and counts down from there.


# This part of the program manages the countdown for the bottles of beer song.
def sing_beer_song(bottles):
    
    current = bottles
    while current > 0:
        
        # this determines correct pluralization for 'bottle' use
        bottle_word = "bottle" if current == 1 else "bottles"
        next_count = current - 1
        next_bottle_word = "bottle" if next_count == 1 else "bottles"
        
        print(f"{current} {bottle_word} of beer on the wall, {current} {bottle_word} of beer.")
        if next_count > 0:
            print(f"Take one down and pass it around, {next_count} {next_bottle_word}(s) of beer on the wall.\n")
        else:
            print(f"Take one down and pass it around, 0 bottle(s) of beer on the wall!\n")
        
        current = next_count
        
    print("Time to buy more bottles of beer!")
    
    
# This is the main function of the program, asking user for input
# on how many beers are on the wall
def main():
    while True:
        user_input_of_beers = input("How many bottles of beer are on the wall? (Max 100): ")
        try:
            num_bottles = int(user_input_of_beers)
            
# This part of the program enforce constraints: numbers must be between 0 and 100
            if num_bottles < 0:
                print("Please enter a positive number.\n")
            elif num_bottles > 100:
                print("Error: You cannot start with more than 100 bottles.\n")
            else:
                sing_beer_song(num_bottles)
                break  # the break function, exits the input loop once a valid number is processed
                
        except ValueError:
            print("Sorry! That is not a valid entry. Please enter a valid number.")
main()