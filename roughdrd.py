'''
def Caesar_cipher():
    
    
    Answer_dict = {'A': 'Lord', 'B': 'of', 'C': 'the', 'D': 'rings'}
    
    Answer_word_list = list(Answer_dict.keys())
    for i in Answer_word_list:
        print(Answer_dict[i])

    
Caesar_cipher()

word = 'abc'

print(len(word))
'''

'''
phrase = 'abc'
new = 'a b c'
print(len(phrase))
print(len(new))
newline = new.split()
newphrase = phrase.split()
print(newphrase)
print(len(newphrase))
'''

'''
def transposition_cipher(random_num):
    
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
    print(f"\n Now add each letter of your phrase by the number you found earlier (for example, if the number was 1, and the plaintext letter is a, then the encrypted value you find will be b), what you are making is called a caesar cipher")

    phrase_list = phrase.split()
    encr_phrase = ''
    if (len(phrase_list) == 1):
        for i in phrase_list:
            encr_phrase = chr(ord(i) + (random_num))
    encr_phrase = 
            
    

caesar_cipher(shifting)
'''
'''
plz = 'happy'
temp_list = []

for i in plz:
    temp_list.append(str(i) + "\n")

print(temp_list)
'''
'''
listing = '123'

print(listing[:1])
print(listing[1:5])
'''

def columnar_transposition_cipher(word, key):
    import math

    # Pad word to fill a full matrix
    key_len = len(key)
    num_rows = math.ceil(len(word) / key_len)
    padded_len = num_rows * key_len
    word = word.ljust(padded_len, 'X')

    # Fill matrix row-wise
    matrix = [list(word[i:i+key_len]) for i in range(0, len(word), key_len)]

    # Create dictionary to map key position to column index
    key_order = {k: i for i, k in enumerate(sorted(key))}
    
    # Read columns in key order
    ciphertext = ''
    for k in key:
        col_idx = key.index(k)
        for row in matrix:
            ciphertext += row[col_idx]

    return ciphertext


print('newchange')
print ('newchange1')
