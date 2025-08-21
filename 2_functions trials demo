import random

def Ceasar_cipher():
    # Mapping of choices
    choice_map = {
        'A': 'Lord',
        'B': 'of',
        'C': 'the',
        'D': 'rings'
    }

    # List of actual words (in upper for comparison)
    Answer_list = list(choice_map.values())
    Answer_list_upper = [word.upper() for word in Answer_list]

    print("Welcome to Mount Doom!!! (or not a good welcome).\n"
          "QUICK!! Frodo needs to drop the ring into the volcano but it's encrypted.\n"
          "The following answer choices are the possible keys to the Caesar cipher:\n")

    # Print the options
    for letter, word in choice_map.items():
        print(f"{letter}) {word}", end="  ")
    print("\n")

    print("You will be given a value that has been encrypted by a Caesar cipher.")
    print("You have 3 tries to decrypt the value and find the key to help Frodo!\n")
    print("You can either type in the **letter** of the answer choice, or the **word** itself.\n")
    print("This is your encrypted word, good luck!\n")

    # Randomly choose a word and encrypt it with Caesar shift of +1
    correct_word = random.choice(Answer_list).upper()
    encrypted = ''
    for ch in correct_word:
        encrypted += chr((ord(ch) - 65 + 1) % 26 + 65) + "\n"  # Caesar +1
    print(encrypted)

    # 3 chances
    attempts = 3
    while attempts > 0:
        user_input = input("Type your guess (letter or word):\n").strip().upper()

        # If letter choice, convert to word
        if user_input in choice_map:
            guess_word = choice_map[user_input].upper()
        elif user_input in Answer_list_upper:
            guess_word = user_input
        else:
            print("Invalid input. Please enter a valid letter (A–D) or word from the list.")
            continue

        if guess_word == correct_word:
            print("\n🔥 Congrats! You guessed correctly! Humanity is saved!! 🔥")
            return
        else:
            attempts -= 1
            print(f"Wrong answer, you have {attempts} guesses left!\n")

    print("\n💀 Frodo failed to throw the ring into the volcano... Sauron has the ring now.")

# Run the game
Ceasar_cipher()
