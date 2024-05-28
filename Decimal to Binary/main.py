def binary_to_decimal(number:int)->str:
    binary_list = []
    while number >0:
        remainder = number % 2
        number = number//2

        binary_list.append(str(remainder))
    return "".join(binary_list[::-1])

if __name__ == "__main__":
   x =  binary_to_decimal(1000)
   print(x)