a = []
import math
for i in range(2,1001):
    is_prime=True
    for j in range(2,int(math.sqrt(i))+1):
        if (i%j == 0):
            is_prime = False
            
    if is_prime:
        a.append(i)
        
print(a)            
print(int(1.7))

n = 1874
def count_num(n):
    counter = 0
    remainder = n
    while remainder > 0:
        remainder = remainder//10
        counter += 1
    return counter

print(count_num(123132))