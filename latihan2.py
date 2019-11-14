print("Program menampilkan bilangan terbesar dari")

a=1
max=0
while a !=0:
    if a > max:
        max = a
    a = int(input("Masukkan bilangan:"))
    if a == 0:
        break
print("Bilangan terbesar adalah:", max)
