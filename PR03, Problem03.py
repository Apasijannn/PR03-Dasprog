s = input()

if 1 < len(s) <= 100000:
    batu =[]
    rugi = 0
    hancur = 0
    for  i in s:
        kerugian = 1000 * ord(i)
        if batu and batu [-1] == i:
            rugi += kerugian * 2
            hancur += 1
            batu.pop()
        else: 
            batu.append(i)
        
sisa_batu = len(batu)      

if hancur != 0:
    print(f'Di gudang tersisa {sisa_batu} batu')  
    print(f'Total Kerugian: {rugi} Dolar Imbu')
elif hancur == 0:
    print(f'Di gudang tersisa {sisa_batu} batu')       
    print(f'Wah, Jotaro Joemama tidak jadi dipecat')
