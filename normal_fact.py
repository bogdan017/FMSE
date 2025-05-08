import random
from math import gcd

def find_period_classic(a, N):
    r = 1
    while pow(a, r, N) != 1:
        r += 1
        if r > N:
            return None
    return r

def shor_classic(N):
    if N % 2 == 0:
        return 2, N // 2

    for _ in range(10):
        a = random.randint(2, N - 1)
        d = gcd(a, N)
        if d > 1:
            return d, N // d

        r = find_period_classic(a, N)
        if r is None or r % 2 != 0:
            continue

        x = pow(a, r // 2, N)
        if x == N - 1 or x == 1:
            continue

        factor1 = gcd(x + 1, N)
        factor2 = gcd(x - 1, N)
        if 1 < factor1 < N and 1 < factor2 < N:
            return factor1, factor2

    return None, None

N = 153243
f1, f2 = shor_classic(N)
if f1 and f2:
    print(f"Factorii lui {N} sunt {f1} si {f2}")
else:
    print(f"Factorii lui {N} nu au fost gasiti in incercările date.")