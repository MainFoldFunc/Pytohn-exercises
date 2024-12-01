import time
def sito_eratostenesa(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]: 
            for multiple in range(i * i, n + 1, i):
                is_prime[multiple] = False

    primes = [i for i, prime in enumerate(is_prime) if prime]
    return primes
start_time = time.time()
print(sito_eratostenesa(100000000))
end_time = time.time()
print(f"The time to run this function was: {end_time - start_time}")