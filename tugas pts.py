x = input("apakah anda ingin melakukan fibonacci? (y/n)")
ctr = 1
a = 1
b = 1
if x == "y":
    N = int(input("Masukan angka fibonacci: "))
    if ctr <=N:
        print(a)
    for i in range(N):
        c = a + b
        a = b
        b = c
        ctr = ctr + 1
        print(c)
else:
    print("stop")