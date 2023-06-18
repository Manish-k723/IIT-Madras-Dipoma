
def prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def Goldbach(n):
    gold = []
    for i in range(1, (n//2)+1):
        if prime(i):
            if prime(n-i):
                gold.append((i,n-i))
    return gold    

n=int(input())
print(sorted(Goldbach(n)))