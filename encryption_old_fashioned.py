alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]

cipher = []
decrypted = []
alphabet_length = len(alphabet) -1

while_true = True

while while_true:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    text_list = list(text)
    print(text_list)
    if direction == 'encode':
        for user_letter in text_list:
        # print(user_letter) 
            if user_letter in alphabet:
                index = alphabet.index(user_letter)
                encrypted_letter = alphabet[index + shift]
                cipher.append(encrypted_letter)
            elif user_letter == " ":
                cipher.append(user_letter)
        str_cipher = ''.join(cipher)
        print(f"The following text will be encrypted: {text}.")
        print(f"The encoded text is: {str_cipher}.")  
    
    if direction == "decode":
        for user_letter in text_list:
        # print(user_letter) 
            if user_letter in alphabet:
                index = alphabet.index(user_letter)
                encrypted_letter = alphabet[index - shift]
                decrypted.append(encrypted_letter)
            elif user_letter == " ":
                decrypted.append(user_letter)
        str_decrypted =''.join(decrypted)
        print(f"The following text will be decrypted: {text}.")
        print(f"The decrypted text is: {str_decrypted}.")    
  
      
    repeat = input("Would you like to encode or decode something else? Please enter Yes or No: ").lower()
    
    
    if repeat == "no":
        while_true = False
    else:
        continue