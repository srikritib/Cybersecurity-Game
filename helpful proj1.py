#prints b, works with A
'''
letter = 'abc'
result = ''
for i in letter:
    dos = chr(ord(i) + 1)
    result += dos
print(result)


'''
'''
import random

# Step 1: Setup
answer_list = ['Lord', 'of', 'the', 'rings']
answer_choices = {
    'A': 'Lord',
    'B': 'of',
    'C': 'the',
    'D': 'rings'
}
number_list = [1, 2, 3, 4, 5]  # Caesar shift values

def encrypt_word(word, shift):
    encrypted = ''
    for char in word:
        if char.isalpha():
            encrypted += chr((ord(char.lower()) - 97 + shift) % 26 + 97)
        else:
            encrypted += char
    return encrypted

# Step 2: Introduction
print("Welcome to Mount Doom!!! (or not a good welcome).\n"
      "QUICK!! Frodo needs to drop the ring into the volcano but it's encrypted!\n")
print("The following answer choices are the possible keys to the Caesar cipher:\n")

for key, value in answer_choices.items():
    print(f"{key}) {value}")
print("\nYou will be given a value that has been encrypted with a Caesar cipher.")
print("You have 3 tries to decrypt it and guess the correct word to help Frodo!\n")

# Step 3: Pick random word and shift
original_word = random.choice(answer_list)
shift_value = random.choice(number_list)
encrypted_word = encrypt_word(original_word, shift_value)

print(f"\n🔒 Encrypted word: {encrypted_word.upper()} (Shifted by {shift_value} letters)")

# Step 4: Game Loop
guesses_left = 3
while guesses_left > 0:
    user_input = input("\nYour guess (type letter A/B/C/D or the word): ").strip().capitalize()

    # Check both letter and word match
    if user_input.upper() in answer_choices:
        guess = answer_choices[user_input.upper()]
    else:
        guess = user_input

    if guess.lower() == original_word.lower():
        print("🎉 Congrats! You guessed correctly! Humanity is saved!!")
        break
    else:
        guesses_left -= 1
        if guesses_left > 0:
            print(f"❌ Wrong answer! You have {guesses_left} guesses left.")
        else:
            print(f"💀 Frodo failed... The correct answer was '{original_word}'. Sauron has the ring now.")




'''
def caesar_cipher(random_num):
    print("Welcome to Level 2!\n")
    print("You must recall the Caesar shift used in Level 1 to encrypt the ring's message!\n")

    attempts = 3

    while attempts > 0:
        try:
            user_pick = int(input("Enter the Caesar shift number used from Level 1: "))
        except ValueError:
            print("❌ Invalid input. Please enter a number.")
            continue  # doesn't consume an attempt

        if user_pick == random_num:
            print("✅ Yes! You've remembered the shift. The ring is encrypted and safe.")
            return
        else:
            attempts -= 1
            if attempts > 0:
                print(f"❌ WRONG — you have {attempts} attempts left.\n")

    print("💀 You have failed... Sauron has the ring now... prepare for doom!")
