morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--',
    '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...',
    ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
}
morse_to_letters= {value:key for (key,value) in morse_code_dict.items()}


def return_morse(text):
    string = ""
    for letter in text.upper():
        string += morse_code_dict[letter] + " "
    return string

def return_last_morse(text):
    string = ""
    for letter in text.upper():
        string += morse_code_dict[letter]
    return string

def text_to_morse():
    input_text = input("words or word\n")
    if input_text == "word":
        word = input("word:\n")
        print(return_morse(word))

    elif input_text == "words":
        words = input("Words:\n").upper()
        output = ""
        for i in range(len(words)):
            if i == len(words)-1:
                output += morse_code_dict[words[i]]
            elif words[i] == " ":
                output += "/ "
            else:
                output += morse_code_dict[words[i]] + " "
        print(output)



def morse_to_text():
    input_text = input("words or word\n")
    t = ""
    if input_text == "word":
        word = input("word:\n")
        letters = word.split(" ")
        letters = [morse_to_letters[letter] for letter in letters]
        for letter in letters:
            t += letter
        print(t)

    elif input_text == "words":
        words = input("Words:\n")
        words = words.split(" / ")
        t = ""
        for word in words:
            letters = word.split(" ")
            for letter in letters:
                t += morse_to_letters[letter]
            t += " "


        print(t)


if __name__ == "__main__":
    morse_text = input("If morse to text type morse, else if text to morse type text\n").lower()

    if morse_text == "morse":
        morse_to_text()
    else:
        text_to_morse()
















