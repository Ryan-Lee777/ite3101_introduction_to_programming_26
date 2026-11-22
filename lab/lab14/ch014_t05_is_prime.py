def is_prime(x:int):
    for n in range(2,x - 1):
        if x % n == 0:
            return False
            