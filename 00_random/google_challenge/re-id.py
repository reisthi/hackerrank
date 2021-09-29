""" Regenerate IDS
    - A random number from 0 - 10000 is picked from a hat.
    - This random number will be the index of a string.
    - The string consists of prime numbers
    - Original Id would be an index + 5 of a list of all prime numbers from 0-1000.

"""


def solution(i):
    long_string = create_long_string_of_primes(i)
    return long_string[(i + 1):(i + 6)]


def create_long_string_of_primes(i):
    long_string = str()
    counter = 1
    while len(long_string) <= i + 6:  # make sure to include the next 5 digits
        if is_prime(counter):
            long_string += str(counter)
        counter += 1
    return long_string


def is_prime(n):
    result = True
    for i in range(2, n):
        if n % i == 0:
            result = False
            break
    return result
