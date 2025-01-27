def caeser_cipher_encrypt(text, shift):
    encrypted_text=""
    for char in text:
        if char.isalpha():
            shift_amount=shift%26
            if char.islower():
                start=ord('a')#ascii value
            elif char.isupper:
                start=ord('A')
            '''
            shift_amount = 27 % 26,  shift_amount = 1,   A shift of 27 is equivalent to a shift of 1
            if char is 'C' and start is ord('A') (65),
            then ord('C') - 65 gives 2.
            This means 'C' is the 3rd letter in the alphabet
            ord(char) - start: Computes the zero-based index of the character.
            + shift_amount: Applies the shift to this index.
            % 26: Ensures the result wraps around within the range of 0 to 25. This handles the circular nature of the alphabet
            (e.g., shifting past 'Z' wraps around to 'A').
            '''
            new_char=chr(start+(ord(char)-start+shift_amount)%26)
            encrypted_text+=new_char
        else:
            encrypted_text+=char
    return encrypted_text

def caeser_cipher_decrypt(text, shift):
    return caeser_cipher_encrypt(text, -shift)

def main():
    input_text=input("enter the text to be encrypted:")
    shift=int(input("enter the shift value:"))

    encrypted_text=caeser_cipher_encrypt(input_text, shift)
    decrypted_text=caeser_cipher_decrypt(encrypted_text, shift)

    print("\nInput text: ",input_text)
    print("Encrypted text: ",encrypted_text)
    print("Decrypted text: ",decrypted_text)

if __name__=="__main__":
    main()
