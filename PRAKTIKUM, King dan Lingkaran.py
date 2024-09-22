x1, y1 = map(int, input().split())
xs, ys = map(int, input().split())
xf, yf = map(int, input().split())

awal = ((xf - xs) + (yf - ys))**2
akhir = ((xf - x1) + (yf - y1))**2

if akhir > awal:
    print("Yes")
else:
    print("No")