N = int(input())                        # 4 or 1
n = list(map(int, input().split()))     # 3 1 2 1 or 1

counters = [1]*100000

for i in n:
    counters[i] += 1

colors = max(counters)
rooms_change = 0

for i in n:
    if counters[i] != colors:  
        rooms_change += 1

print(rooms_change)  
