# from datetime import datetime

"""
Notes to the Mentor and/or Reviewer:
  1 - No validations, for the time being.
  2 - Approach based on my interest in to go a little deeper in the practice
  3 - Approach based on Interest in to practice the conversion of concepts into programming language
  4 - I've decided to not use extenal tools (eg. itertools, numpy) to practice the 'raw'  python a little bit more
  5 - I've created all functions except for the 'flatten2gen' (source provided)
  6 - In the future this program could be converted in a class
  7 - Source for the explanation of the Prime Decomposition algorithm: https://qr.ae/pNgGII (Graeme McRae's answer)
  8 - The test results (commented at the bottom of this program) showed that the brute force work tends to work better for numbers below approx 800.
"""

# Loads a list of prime numbers from the 1st (2) to the 1000th (7919)
primes_file = open('./primes-1st-1000th.csv', 'r')
primes_line = primes_file.readline().split(',')
primes = [int(p) for p in primes_line]


# Defines the function to decompose a number into prime factors
def prime_decomposition(n):
    divisors = []
    next_prime = 0
    num = n
    while num != 1:
        if num % primes[next_prime] == 0:
            divisors.append(primes[next_prime])
            num /= primes[next_prime]
            continue
        next_prime += 1
    # Creates a dictionary with the format { <prime>: <exponent> }
    dct = {n: divisors.count(n) for n in divisors}
    if len(dct) == 1:
        dct.setdefault(1, 2)
    # print("prime_decomposition:", dct)
    return dct


# Generates a list of the ranges for each exponent
def exponent_decomposition(dct):
    res = [list(range(dct[d] + 1)) for d in dct]
    # print("exponent_decomposition", res)
    return res


# Flattens a list
# Source: https://stackoverflow.com/a/3172940/2457251
# I need to study this function
def flat2gen(lst):
    for item in lst:
        if isinstance(item, list):
            for sublist in item: yield sublist
        else:
            yield item


# Returns a list of all the possible combinations between the items in two lists
def comb2(l1, l2=False):
    if not l2:
        return [l1]
    res = []
    for i in l1:
        for j in l2:
            elem = [i, j]
            flat_elem = list(flat2gen(elem))
            res.append(flat_elem)
    return res


# Returns a list of all the possible combinations between  the items in N lists
# Depends on the 'comb2' function
def comball(lst):
    if len(lst) == 1:
        return lst
    l1 = lst[0]
    l2 = lst[1]
    res = comb2(l1, l2)
    for idx in range(2, len(lst)):
        res = comb2(res, lst[idx])
    return res


# Generates a list with the factors of a given number 'n'
def number_factors(n):
    # Decomposes the original number into primes
    pd = prime_decomposition(n)

    # Creates lists with expanded exponents (ranges)
    ed = exponent_decomposition(pd)

    # Generates all valid combinations of exponents
    exponent_lists = comball(ed)

    # Calculates factors based on each possible combination of exponents
    base = list(pd.keys())
    factors = []
    for exponent_list in exponent_lists:
        factor = 1
        for b, exponent in zip(base, exponent_list):
            factor *= b ** exponent
        factors.append(factor)

    # Removes duplicates and sorts the list
    factors = list(dict.fromkeys(factors))
    factors.sort()
    return factors


# Original function from the exercise
def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """
    return number_factors(num)



"""
PERFORMANCE TESTS
def brute_force(num):
    res = []
    for i in range(1, num + 1):
        if num % i == 0:
            res.append(i)
    res.sort()
    return res


nbr = 15678
rng = 4
print("factors:", find_factors(nbr))


def test_pd():
    for n in range(rng):
        t1 = datetime.now()
        for i in range(0, 100000):
            find_factors(nbr)
        print(n, datetime.now() - t1)


def test_bf():
    for n in range(0, rng):
        t1 = datetime.now()
        for i in range(0, 100000):
            brute_force(nbr)
        print(n, datetime.now() - t1)


print("Prime Decomposition")
test_pd()

print("Brute Force")
test_bf()
"""
