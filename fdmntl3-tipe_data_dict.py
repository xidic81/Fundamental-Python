"""
Tipe data dictionary sekedar menghubungkan antara KEY dan VALUE
KVP = Key Value Pair
Dictionary = Kamus
"""

kamus_sun_eng = {'leumpang': 'walk', 'lumpat': 'run', 'luncat': 'jump', 'leleus': 'exhausted'}

print(kamus_sun_eng)
print(kamus_sun_eng['lumpat'])
print(kamus_sun_eng['luncat'])
print(kamus_sun_eng['leleus'])

print('\nData ini dikirimkan oleh server Grab untuk memberikan info di sekitar user')
data_grab = {
    'tanggal': '2020-08-07',
    'driver_list': [
        {'Nama': 'Eki', 'Jarak': '50m'},
        {'Nama': 'Randy', 'Jarak': '100m'},
        {'Nama': 'Cena', 'Jarak': '200m'},
        {'Nama': 'Undertaker', 'Jarak': '1Km'}
    ]
}
print(data_grab)
print(f"\nDriver disekitarmu {data_grab['driver_list']}")
print(f"Driver #1 {data_grab['driver_list'][0]}")
print(f"Driver #3 {data_grab['driver_list'][2]}")
print(f"Driver terdekat adalah {data_grab['driver_list'][0]['Nama']} jaraknya {data_grab['driver_list'][0]['Jarak']}")
