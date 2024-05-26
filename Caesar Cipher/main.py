#Caesar Cipher


class CaesarCipher:
    def __init__(self):
        self.alphabet_lower:list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z']
        self.alphabet_upper:list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    def encrypt(self,text:str,shift:int)->None:
        new_letters:list = []
        for char in text:
            if char in self.alphabet_lower:
                position = (self.alphabet_lower.index(char) +shift) % 26
                new_letters.append(self.alphabet_lower[position])
            elif char in self.alphabet_upper:
                position = (self.alphabet_upper.index(char) +shift) % 26
                new_letters.append(self.alphabet_upper[position])
            else:
                new_letters.append(char)
        print("".join(new_letters))

    def decrypt(self,text:str,shift:int)->None:
        new_letters:list = []
        for char in text:
            if char in self.alphabet_lower:
                position = (self.alphabet_lower.index(char) -shift) % 26
                new_letters.append(self.alphabet_lower[position])
            elif char in self.alphabet_upper:
                position = (self.alphabet_upper.index(char) -shift) % 26
                new_letters.append(self.alphabet_upper[position])
            else:
                new_letters.append(char)
        print("".join(new_letters))

    """
    the decrypt method is the same thing as self.encrypt(text,-shift)
    """

if __name__ == "__main__":
    caesar = CaesarCipher()
    user_text:str = input('What text would you like to encrypt or decrypt with the caesar cipher?')
    user_shift:int = int(input("What is the shift amount?"))
    type:str = input("Do you want to encrypt or decrypt")
    if type.lower() == "decrypt":
        caesar.decrypt(user_text,user_shift)
    else:
        caesar.encrypt(user_text, user_shift)



