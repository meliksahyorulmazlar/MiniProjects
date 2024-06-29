def hexadecimal_to_binary(text:str)->int:
    dictionary = {'0':0,1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13,'E': 14, 'F': 15}
    hex_list = list(text.upper())[::-1]
    decimal = 0
    for i in range(len(hex_list)):
        amount = dictionary[hex_list[i]]
        decimal += amount* pow(16,i)
    return decimal

if __name__ == "__main__":
    x = hexadecimal_to_binary("1A3")
    print(x)
