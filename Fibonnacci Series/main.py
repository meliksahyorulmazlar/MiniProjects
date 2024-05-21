
def fib(n:int):
    #using lists
    fib_list:list = [0,1]
    if n<3:
        print(fib_list)
    else:
        for i in range(1,n-1):
            fib_list.append(fib_list[i]+fib_list[i-1])
        print(fib_list)

def recursive_fib(n:int):
    if n ==1:
        return 0
    elif n == 2:
        return 1
    else:
        return recursive_fib(n-2)+recursive_fib(n-1)


def sub_fib(n:int):
    if n == 1:
        return 0
    elif n <= 3:
        return 1
    else:
        a = 1
        b = 1
        for i in range(n-3):
            c = b
            b = a+b
            a = c
        print(b)





if __name__ == "__main__":
    fib(100)
    sub_fib(100)
    
