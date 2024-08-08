class BaseConvertor:
    def __init__(self,decimal_number:int,base:int):
        self.number = decimal_number
        self.base = base
        self.convert_to_base()

    def convert_to_base(self):
        if self.base == 0:
            print("Base 0 is not a viable or defined numeral system")
            return None
        elif self.base == 1:
            print(f"Bits: {[1]*self.number}\nBase:1\nNumber:{self.number}")
        elif self.base >= 2:
            bits = []
            number = self.number

            while self.number != 0:
                remainder = self.number % self.base
                self.number = self.number // self.base

                bits.append(str(remainder))

            result = [int(bit)for bit in bits[::-1]]
            print(f"Bits:{result}\nBase:{self.base}\nNumber:{number}")
            total = 0
            length = len(result)
            for i in range(length):
                if result[length - i - 1] != "i":
                    total += pow(self.base, i) * result[length - i - 1]
            if total == number:
                print("Operation successful")
        elif self.base == -1:
            print("Base -1 is not a viable or defined numeral system")
        elif self.base < -1:
            bits = []
            number = self.number

            while self.number != 0:
                remainder = self.number % self.base
                self.number = self.number // self.base
                if remainder < 0:
                    remainder += -(self.base)
                    self.number += 1

                bits.append(str(remainder))

            result = [int(bit) for bit in bits[::-1]]
            print(f"Bits:{result}\nBase:{self.base}\nNumber:{number}")

            #This set of code will check if the bit conversion was successful
            total = 0
            length = len(result)
            for i in range(length):
                if result[length - i - 1] != "i":
                    total += pow(self.base, i) * result[length - i - 1]
            if total == number:
                print("Operation successful")
                
if __name__ == "__main__":
    BaseConvertor(decimal_number=500,base=-22)


