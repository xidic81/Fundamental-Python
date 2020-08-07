# KONSTRUKSI DASAR PYTHON
# SEQUENTIAL = eksekusi berurutan
print('Hello World')
print('by Sidik')
print('tanggal 04 Agustus 2020')
print('*' * 10)

# PERCABANGAN = Eksekusi Terpilih
ingin_ganteng = True
if ingin_ganteng:
    print('belajar konsisten')
else:
    print('malas')

# PERULANGAN
jumlah_pemain = 7
for index_pemain in range(1, jumlah_pemain + 3):  # jumlah_perulangan = 7 - 1 = 6
    print(f'Ayo pemain #{index_pemain}')

print('-' * 20)

jumlah_haji = 10
for index_haji in range(1, 11):
    print(f'semoga haji mabrur {index_haji}')
