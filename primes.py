"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes<=0: 
        raise ValueError("Value entered must be greater than 0")
    list = []
    primes = 0 
    next = 2
    while primes < number_of_primes:
        if is_prime(next):
            list.append(next)
            primes += 1
        next += 1
    return list




def is_prime(val):
    if val==2: 
        return True
    if val%2==0:
        return False

    for i in range(3,int((val-1)/2)):
        if val%i == 0: 
            return False
        
    return True 