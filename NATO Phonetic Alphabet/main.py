import pandas


def convert():
    nato_csv:pandas.DataFrame = pandas.read_csv("nato_phonetic_alphabet.csv")
    alphabet:dict = {row["letter"]:row["code"] for (index,row) in nato_csv.iterrows()}
    words = input("Convert your message into the NATO Phonetic alphabet")
    new_message = []
    for char in words.upper():
        if char in alphabet:
            new_message.append(alphabet[char])
        else:
            new_message.append(char)
    print(new_message)

if __name__ == "__main__":
    convert()

