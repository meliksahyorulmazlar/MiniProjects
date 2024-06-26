#code to count the first number of prime in the first n

def count_primes(n:int)->None:
    if n<2:
        return 0
    prime_list = [True] *n
    prime_list[0] = False
    prime_list[1] = False


    for i in range(2,int(n**0.5)+1):
        for j in range(i*i,n,i):
            prime_list[j] = False
    print(sum(prime_list))





if __name__ == "__main__":
    n = int(input("Enter n"))
    count_primes(n)







