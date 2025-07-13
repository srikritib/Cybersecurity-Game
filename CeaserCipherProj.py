'''
Code summary: I want to make a ceasar cipher game. I want to have a list of words and tell the user about the word choices.
Then I will ask the user if they want to play the game (Y/N), till the user hits N or the user gets the guess right, the game will loop.
The user has to guess the letter based on the coded letter and basically has to decrypt the ceaser cipher.\
'''

'''
1) First make a list containing a string of 5 words. Then have an input statement welcoming the user to the game.
2) Then print a list of answer choices of words a) word 1, b) word 2... etc.
3) The program should contain a list of numbers from 1 to 5.
4) Have a while loop that will continue till the word matches the correct word or the user presses N. (User clicks Y to play the game).
5) Within the while loop there should be a function call.
6) This function contains a for loop iterating through the number list. The number represents the amount of spaces to the right the letter
gets decoded in. (if number is 1, A becomes B in the answer choice.)
'''

def substitution_cipher():
    
    import random
    random_num = random.randint(1, 3)
    
    Answer_dict = {'A': 'lord', 'B': 'of', 'C': 'the', 'D': 'rings', 'E': 'lords', 'F': 'ring', 'G': 'Hobbits', 'H': 'Frodo', 'I': 'Gandalf'}
    
    Answer_word_list = list(Answer_dict.values())
    
    Answer_choice_list = list(Answer_dict.keys())


    print("Welcome to level 1!\n\n"
                          "QUICK!! Frodo needs to drop the ring into Mount Doom but it is encrypted by a substitution cipher. \n\n"
                          "The following answer choices are the possible keys to the cipher: \n\n")
    print(Answer_dict,"\n\n")
    print("You will be given a value that has been encrypted by a substitution cipher, you will have 3 tries to decrypt the value and find the key to help Frodo!\n")
    print("You can either type in the letter of the answer choice, or the word\n")
    print("This is your encrypted word, good luck!\n\n")

    x = 1
    z = 3

    word = random.choice(Answer_word_list)
    #ans = "Lord"
    word = word.upper()

    #Takes every word in the list and shifts the letters by one to the right. 
    result = ''
    for i in word:
        encrypted = chr(ord(i) + (random_num)) #Ascii
        result += encrypted
        result += "\n"
    print(result)


    #Takes in user's 3 guesses
    #shorten the if then statements
    while(x <= 3):
        user_q = input("Type in your guess (Type in either the associated letter or word of your choice):\n")
        user_q = user_q.upper()
        if len(user_q) == 1:
            if word == Answer_dict[user_q].upper():
                x = 3
                break
            else:
                z = z-1
                print("Wrong answer, you have", z, "guesses left!")
                x += 1
        elif len(user_q) != 1:
            if word == user_q:
                x = 3
                break
            else:
                z = z-1
                print("Wrong answer, you have", z, "guesses left!")
                x += 1

    if (x == 3):
        print("Congrats! you guessed correctly! Humanity is saved!!")
        return random_num
    else:
        print("Frodo failed to throw the ring into the volcano, Sauron has the ring now, prepare for ultimate doom...")
        return random_num



shifting = substitution_cipher()
'''
#continuation of the first game
def caesar_cipher(random_num):
    
    print("Welcome to level 2!\n\n")
    print("Sauron is still coming after the ring even after Frodo threw it in Mount Doom!\n\n")
    print("You need to come up with an encryption key on the ring to make sure Sauron can't crack it!\n")
    print("The good news is you can use the same pattern of letter shifting from level 1 to encrypt a phrase of your choice.\n\n")

    attempts = 3
    
    while True: 
        try:
            user_pick = int(input("First type in the number of letters the encoded word from level 1 has been shifted away from your answer."))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            
    while (attempts > 0):
        
        if user_pick == random_num:
            print("Correct number!")
            break
        
        else:
            attempts -= 1
            if (attempts > 0):
                print(f" WRONG, you have {attempts} attempts left")
                user_pick = int(input())
            else:
                print("You have failed...Sauron has the ring now...prepare for doom!")
    
    phrase = input("Now pick any phrase and type it in, this will serve as your key")
    print(f"\n Now ")
            
    

caesar_cipher(shifting)
'''