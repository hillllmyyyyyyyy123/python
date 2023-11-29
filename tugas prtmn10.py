num_input = input("masukan tiga nomor digit: ")
user_numbers = [int(num) for num in num_input.split()]
daftar_angka = [[323, 546, 879],
                [456, 787, 675],
                [123, 234, 321],
                [768, 556, 468],]
for idx, angka in enumerate(daftar_angka):
    if user_numbers == angka:
        print(f"nomor anda ada dalam daftar pada posisi {idx + 1}.")
        break
else:
    print("itu tidak ada dalam daftar")