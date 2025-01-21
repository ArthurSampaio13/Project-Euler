def factor(num):
    n = 2
    factors = []
    
    while n ** 2 <= num:
        if num % n == 0:
            factors.append(n)
            num //= n
        else:
            n += 1
            
    if num > 1:
        factors.append(num)
        
    return factors

print(factor(600851475143))