def binary_to_decimal(text:str)->int:
    bits = list(text)[::-1]
    decimal = 0
    for i in range(len(bits)):
        if bits[i] == "1":
            decimal += pow(2,i)
    return decimal



if __name__ == "__main__":
    binary_to_decimal()












