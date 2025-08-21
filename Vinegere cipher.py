'''
def vigenere_cipher():
    print("Hello, welcome to the last level of the game, level 3!\n")
    print("This level has a vigenere cipher, where encryption relies on a mathamatical formula.\n")
    print("Remember the words you got after decrypting the substitution cipher (level 1) and the transposition cipher (level 2)?\n")
    print("Now the ring was successfully dropped into Mount Doom, but in order to keep it fully safe from Sauron, you need to encrypt a value so nobody else can get access to the volcano...\n\n")
    
    print("Now you will see a column of letters and numbers below this message. For this cipher, the mathamatical formula associates letters with numbers (A = 0, B = 1...Z = 25)\n\n")
    for i in range(26):
        letter = chr(ord('A') + i)
        print(f"{letter} = {i}")
    
    print("\n\nYou will need the two words you found in the previous levels, using the guide above, turn the 2 words into numbers (for example: if your word was cat, then the number you write down is 2019)\n")
    
    word_1 = 'ball'
    word_2 = 'cat'
    
    user_input_num = (int(input("write your number here for your first word: "))).strip()
    
    for i in word_1:
        lett = chr(ord(i) + i)
        print(f"{letter} = {i}")
 '''       
        
def vigenere_cipher():
    print("Hello, welcome to the last level of the game, level 3!\n")
    print("This level has a Vigenère cipher, where encryption relies on a mathematical formula.\n")
    print("Remember the words you got after decrypting the substitution cipher (level 1) and the transposition cipher (level 2)?\n")
    print("Now the ring was successfully dropped into Mount Doom, but in order to keep it fully safe from Sauron, you need to encrypt a value so nobody else can get access to the volcano...\n\n")
    
    print("Now you will see a column of letters and numbers below this message. For this cipher, the mathematical formula associates letters with numbers (A = 0, B = 1...Z = 25)\n\n")
    
    for i in range(26):
        letter = chr(ord('A') + i)
        print(f"{letter} = {i}")
    
    print("\n\nYou will need the two words you found in the previous levels. Using the guide above, turn the 2 words into numbers.")
    print("For example: if your word was 'cat', then the numbers would be: 2 0 19\n")
    
    word_1 = 'ball'
    word_2 = 'cat'
    
    
    # Convert words to uppercase and map letters to numbers (A=0, ..., Z=25)
    def word_to_numbers(word):
        for x in word_1:
            
        return [ord(c.upper()) - ord('A') for c in word if c.isalpha()]
    '''
    print(f"Word 1: {word_1} =>", word_to_numbers(word_1))
    print(f"Word 2: {word_2} =>", word_to_numbers(word_2))
    '''
    # Optional: ask the user to type their version and verify
    user_input = input("\nNow try typing the numeric version of your first word (separated by spaces, e.g., 1 0 11 11 for 'ball'): ").strip()
    user_list = [int(x) for x in user_input.split()]
    
    correct_list = word_to_numbers(word_1)
    if user_list == correct_list:
        print("✅ Correct!")
    else:
        print("❌ Not quite. Try checking your math again.")
    
    
    
    
    




vigenere_cipher()