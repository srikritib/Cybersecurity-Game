

import random

#Level 1
def substitution_cipher():
    print("\n\nWelcome to the subsitution cipher game. In this game you will get a bunch of letters that don't make up a word.\n")
    print("The encrypted word you will see is actually the result of a real word being shifted down multiple letters of the alphabet\n (for example, if the word was cat, and each word was shifted by 2 letters, then the encrypted word will be ecv).\n")
    print("Your job is to figure out the actual word from a list of words by seeing how many letters the actual word has shifted.")
    
    #import random
    random_num = random.randint(1, 3)
    
    Answer_dict = {'A': 'lord', 'B': 'Frodo', 'C': 'Gandalf', 'D': 'rings', 'E': 'lords', 'F': 'ring', 'G': 'Hobbits', 'H': 'Frodo', 'I': 'Gandalf'} 
    print(Answer_dict)
    Answer_word_list = list(Answer_dict.values())
    
    Answer_choice_list = list(Answer_dict.keys())

    x = 1
    z = 3

    wording = random.choice(Answer_word_list)
    wording = wording.upper()

    #Takes every word in the list and shifts the letters by one to the right. 
    result = ''
    for i in wording:
        encrypted = chr(ord(i) + (random_num)) #Ascii
        result += encrypted
    
    print("\n\nThe word you will see now is the encrypted word:\n")
    print(result)
    print("\n\n") 

    #Takes in user's 3 guesses
    #shorten the if then statements
    while(x <= 3):
        user_q = input("Try to guess the actual word from the answer choices, you can choose either the answer choice (A, B, etc) or the word (Lord, Frodo, etc):")
        user_q = user_q.upper()
        if len(user_q) == 1:
            if wording == Answer_dict[user_q].upper():
                x = 3
                break
            else:
                z = z-1
                print("Wrong answer, you have", z, "guesses left!")
                x += 1

        elif len(user_q) != 1:
            if wording == user_q:
                x = 3
                break
            else:
                z = z-1
                print("Wrong answer, you have", z, "guesses left!")
                x += 1

    if (x == 3):
        print("Congrats! you guessed correctly! Now move onto the Transposition cipher!!") 
    else:
        print("Frodo failed to throw the ring into the volcano, Sauron has the ring now, prepare for ultimate doom...")



#Level 2
def transposition_cipher():
    print("\n\nWelcome to the transposition cipher game. In this game you will get a bunch of letters that don't make up a word.\n")
    print("The encrypted word you will see is actually the result of a real word being scrambled with some letters that don't belong to the word to try to throw you off.\n")
    print("Your job is to figure out the actual word from a list of words given.")

    guess_num = 0

    words_list = ['Aragorn', 'Samwise', 'Pippin', 'Sauron'] 
    print("These are your word choices:\n")
    print(words_list)
    key = [4, 2, 3, 1]

    word = random.choice(words_list)
    word = word.upper()
    encr = ''

    def temporary_function(subword):
        temp_encrypted = [''] * len(key)
        for i in range(len(subword)):
            temp_encrypted[key[i] - 1] = subword[i]
        return ''.join(temp_encrypted)

    # Encryption
    if len(word) <= len(key):
        encr = temporary_function(word)
    else:
        for i in range(0, len(word), len(key)):
            chunk = word[i:i + len(key)]
            if len(chunk) < len(key):
                chunk = chunk.ljust(len(key), 'X')
            encr += temporary_function(chunk)

    encrypted = encr.upper()
    print("This is your encrypted word (scrambled word):\n", encrypted)

    # Guessing logic
    while guess_num < 3:
        user_guess = input("Enter your decryption guess based on the answer choices: ").upper()
        if user_guess == word:
            print("Correct!")
            break
        else:
            guess_num += 1
            print(f"Wrong. You have {3 - guess_num} attempts left.")
    
    if user_guess != word:
        print(f"💀 Game Over! The correct word was: {word}")


def main():
    print("Welcome to Mount Doom!!\n Quick! Frodo needs help! He has to drop The One Ring into the volcano but it is blocked by 2 ciphers...\n\n")

    while True:
        user_input = input("Please pick number 1 or 2. 1 = Substitution cipher, 2 = Transposition cipher. Type 8 to exit: ")

        if user_input == "1":
            substitution_cipher() 
        elif user_input == "2":
            transposition_cipher()
        elif user_input == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid input, please type 1, 2, or 8.")


main()









