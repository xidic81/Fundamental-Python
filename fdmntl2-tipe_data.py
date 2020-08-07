print('\033[1m' + 'TIPE DATA SKALAR/SEDERHANA:' + '\033[0m')
pemain1 = 'Fabregas'
pemain2 = 'Toure'
pemain3 = 'Ronaldo'
pemain4 = 'Shevchenko'

print('- ' + pemain1)
print('- ' + pemain2)
print('- ' + pemain3)
print('- ' + pemain4)
print(' ')

print('\033[1m' + 'Tipe Data List/Daftar/Array' + '\033[0m')
pemain = ['Fabregas', 'Toure', 'Ronaldo', 'Shevchenko']
print(pemain)
pemain.append('Pogba')
print(pemain)

print('\nSapa Pemain ke-3')
print(f'Yo men {pemain[2]}!')
print('\nSapa Pemain ke-5')
print(f'Yo men {pemain[4]}!')
print('\nSapa Semua Pemain:')
for i, p in enumerate(pemain, start=1):
    print(str(i) + '. ' + f'Yo mens {p}!')
