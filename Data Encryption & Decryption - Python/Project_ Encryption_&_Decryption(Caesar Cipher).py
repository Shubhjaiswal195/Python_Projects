alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encryption(plaintext, shiftkey):
    
    cipher_text = ""
    for char in plaintext:

        if (char in alphabets):

            position = alphabets.index(char)
            new_position = (position + shiftkey)%26
            cipher_text += alphabets[new_position]
        else:

            cipher_text += char 
    
    print(f"The text after Encryption:  {cipher_text} \n")



def decryption(ciphertext, shiftkey):
    
    plain_text = ""
    for char in ciphertext:

        if (char in alphabets):

            position = alphabets.index(char)
            new_position = (position - shiftkey)%26
            plain_text += alphabets[new_position]
        else:

            plain_text += char 
    
    print(f"The text after decryption:  {plain_text} \n")




conversion = True 

while conversion:
 
    choice = input("Type 'encrypt' for Encryption and 'decrypt' for Decryption : \n").lower()
    text = input("Enter the message : \n").lower()
    shift_key = int(input("Enter the Shift Key :\n"))
    

    if (choice == "encrypt"):

        encryption(text, shift_key)

    elif (choice == "decrypt"):

        decryption(text, shift_key)

    
    End = input("Type 'yes' to Continue & 'no' of Exit : \n")

    if (End == "no"):
        conversion = False
print("Have a nice day! Bye !! \n")