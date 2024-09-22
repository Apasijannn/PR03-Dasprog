batas = 78498
prima = []

count = 0  
for i in range(2, batas):
    primaa = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            primaa = False  
            break
    if primaa:
        prima.append(i) 
        count += 1  
    
    if count == batas:  
        break

T = int(input())

output = []  

for k in range(T):
    A, B = map(int, input().split())
    output.append(f"Test Case #{k+1} :")
    for i in range(A-1, B):
        output.append(str(prima[i]))

print("\n".join(output))


