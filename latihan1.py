n = int(input("Masukkan nilai N:"))

from random import random
a = random()

jumlah = n+1
start = 1
stop = jumlah
step = 1
for i in range(start, stop, step):
    print("data ke:", i,"=>",(a))
print("Selesai")
