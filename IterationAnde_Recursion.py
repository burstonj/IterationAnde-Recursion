def factorial_recursive(num):#intersting but effective way to write the fatorial code
    if num == 0 or num == 1:
        return 1 #stops loop
    else:
        return num * factorial_recursive(num - 1)

def factorial_iterative(num):
    fact = 1
    for number in range(2, num+1):
        fact = number * fact
    return fact
 
def main(): #there is a shorter way to write the code shown in the Zoom meeting, but I like seeing how this code is "manually" run.
    print ("Factorial results using an interative function")
    print("0! =", factorial_iterative(0))
    print("5! =", factorial_iterative(5))
    print("10! =", factorial_iterative(10))
    print("25! =", factorial_iterative(25))
    print("50! =", factorial_iterative(50))
    print("100! =", factorial_iterative(100))
    print ("Factorial results using a recursive function")
    print("0! =", factorial_recursive(0))
    print("5! =", factorial_recursive(5))
    print("10! =", factorial_recursive(10))
    print("25! =", factorial_recursive(25))
    print("50! =", factorial_recursive(50))
    print("100! =", factorial_recursive(100))

if __name__ == "__main__":
    main()

