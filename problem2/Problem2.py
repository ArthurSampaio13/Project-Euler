termo_1, termo_2 = 1, 1
total = 0

while termo_1 <= 4_000_000:
    if termo_1 % 2 == 0:
        total += termo_1
    termo_1, termo_2 = termo_2, termo_1 + termo_2  
    
print(total)
