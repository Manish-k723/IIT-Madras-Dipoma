def find_Min_Difference(L,P):
    L.sort()
    diff = float('inf')
    for i in range(len(L)-P+1):
        difference = L[i+P-1]-L[i]
        if difference<diff:
            diff = L[i+P-1]-L[i]
    return diff
        
L=eval(input().strip())
P=int(input())
print(find_Min_Difference(L,P))