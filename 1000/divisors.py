import bisect

# Precompute primes up to 100000 using a Sieve
MAX = 100000
is_prime = [True] * (MAX + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(MAX**0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, MAX + 1, i):
            is_prime[j] = False

primes = [i for i, val in enumerate(is_prime) if val]

def main():
    d = int(input())
    # a + 1 * b + 1 ... = divisors
    # a + 1 * b + 1 ... = 4
    #                   = 2 * 2 , 4 * 1 
    # a = 3 | a = 1 , b = 1

    # p^3 , pq
    # 1 p p^2 p^3 | 1 p q pq 
    # p - 1 >= d | q - p >= d   
    
    # find a smallest prime number such that  
    # p - 1 >= d | q - p >= d conditions satisfied

    p_idx = bisect.bisect_left(primes, 1 + d)
    p = primes[p_idx]
    
    q_idx = bisect.bisect_left(primes, p + d)
    q = primes[q_idx]
    
    print(p * q)
    


t = int(input())
for _ in range(t):
    main()