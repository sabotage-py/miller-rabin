import sys
import random


def miller_rabin(n, t=100):
    r, s = n - 1, 0
    while r % 2 == 0:
        s += 1
        r //= 2
    # n-1 = r * 2^s 
    for _ in range(t):
        a = random.randrange(2, n-1)  # random int from [2,...,n-2]
        strong_witness = True
        y = pow(a, r, n)  #a^r mod n
        if y == 1 or y == n - 1:
            strong_witness = False
        j = 1
        while j <= s - 1 and strong_witness:
            y = (y ** 2) % n
            # now, y is a^{2^j * r} mod n
            if y == n - 1:
                strong_witness = False
            elif y == 1:
                # let x = a^{2^{j-1} * r}, then note that y = x^2 (mod n)
                # so, we have x^2 = 1 (mod n)
                # but we know that x != 1 or -1 (mod n)
                # whence we get, from fact 3.18, that n is composite. 
                return False
            j += 1
        if strong_witness: 
            return False
            # a is a strong witness (to compositeness) for n
    return True


def isPrime(n):
    if n < 2: return False
    elif n <= 3: return True
    elif n % 2 == 0: return False
    # now that we know n is an odd, positive integer > 3...
    # ...let the party begin.
    return miller_rabin(n)


if __name__ == '__main__':
    args = sys.argv[1:]
    n = int(args[0])
    isitprime = isPrime(n)
    if isitprime:
        print("Yes,", n, "is a Prime")
    else:
        print("No", n, "is composite")
