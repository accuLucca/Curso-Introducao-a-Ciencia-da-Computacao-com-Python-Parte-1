def maior_primo(x):
    i = 0
    while x - i > 1:
        if isprime(x-i) == 1:
            return (x-i)
        else:
            i += 1
def isprime(n):
    if n <= 0:
        return 0
    else:
        i = 1
        while n - i > 1:
            if n % (n - i) == 0:
                return 0
            i += 1
            if n - i == 1:
                return 1