import unittest

def fibonacci(n):
    if type(n) != int or n < 0:
        return("Error")
    if n <= 1:
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))

if __name__ == "__main__":
    
    #Programa principal
    while(True):

        print("\n")
        NroTerm = input("Fibonacci de: ")
        print("\n")
        
        try:
            print(fibonacci(int(NroTerm)))
        except:
            print(fibonacci(NroTerm))
