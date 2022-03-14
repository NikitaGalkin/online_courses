from itertools import takewhile
import itertools

def is_prime(number):
    counter = 0
    for i in range(1, number + 1):
        if (number % i == 0):
            counter += 1
    if counter == 2:
        return True
    return False

def primes():
    current_num = 2

    while (current_num > 0):
        if (is_prime(current_num)):
            yield current_num
        current_num += 1

print(list(itertools.takewhile(lambda x : x <= 31, primes())))