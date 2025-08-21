number = ord('A')
print(number)


'''
Code summary: I want to make a ceasar cipher game. I want to have a list of words and tell the user about the word choices.
Then I will ask the user if they want to play the game (Y/N), till the user hits N or the user gets the guess right, the game will loop.
The user has to guess the letter based on the coded letter and basically has to decrypt the ceaser cipher.\
'''

'''
1) Main function not working
2) Write proper instructions
3) Vinigere function
4) Comment code 
5) Afteer Vinigere function work on front end.

Thursday: Vinigere function
Friday: Vinigere function, if time then see if you can replace transposition code with other code
Saturday: Decide what to do with main function and how program should run, write proper instructions, comment code 
'''
'''
print("Welcome to level 1!\n\n"
                          "QUICK!! Frodo needs to drop the ring into Mount Doom but it is encrypted by a substitution cipher. \n\n"
                          "The following answer choices are the possible keys to the cipher: \n\n")
    print(Answer_dict,"\n\n")
    print("You will be given a value that has been encrypted by a substitution cipher, you will have 3 tries to decrypt the value and find the key to help Frodo!\n")
    print("You can either type in the letter of the answer choice, or the word\n")
    print("This is your encrypted word, good luck!\n\n")


    
#NEW CODE

'''
# Call the function

#Level 3
def vigenere_cipher():
    



def main():

    print("Welcome to Mount Doom!!\n Quick! Frodo needs help! He has to drop The One Ring into the volcano but it is blocked by three ciphers...\n\n")
    print("The first two ciphers are called a substitution cipher, and a transposition cipher.")

    while True:
        user_num = int(input("Please pick number 1 or 2. 1 is for the subsitution cipher game, and 2 is for the transposition cipher game. If you want to exit, type 8: "))

        if user_num == 1:
            result = substitution_cipher()  # Call function and store result
            print(f"Substitution cipher result: {result}")
            break  # Exit after running the game
        
        elif user_num == 2:
            result = transposition_cipher()  # Call function and store result  
            print(f"Transposition cipher result: {result}")
            break  # Exit after running the game
        
        elif user_num == 8:
            print("Goodbye!")
            break

        else:
            print("Invalid, type a valid number please")

main()



#shifting = substitution_cipher()


#level = transposition_cipher()
#print(level)
'''