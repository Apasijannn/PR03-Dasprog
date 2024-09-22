U = int(input())
K = int(input())
M = int(input())
Raja = 100

HP_sisa = U-((M//2*2)+( K//2*5)*5+(Raja*10))  

if HP_sisa >= 0:
    print(f'Yey! Ucup Menang! HP tersisa: {HP_sisa:.0f}')
else:
    print('Yah! Ucup Meninggoy')    