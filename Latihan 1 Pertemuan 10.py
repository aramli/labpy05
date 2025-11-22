# Latihan 1
print('Membuat Dictionary baru')
Kontak ={}
Kontak = {'Ari':'081267888','Dina':'087677776'}
print('Kontak = ',Kontak)
print()
print('Tampilkan Kontak Ari')
print(Kontak['Ari'])
print()

#Menambahkan kontak Baru'
Kontak['Riko']='087654544'
#Rubah kontak Dina dengan Nomor Baru'
Kontak['Dina'] = '088999776'

print('Tampilkan semua nama (keys)')
print(Kontak.keys())
print()
print('Tampilkan semua nomor (value)')
print(Kontak.values())
print()
print('Tampilkan semua nama dan nomor dari dictionary')
print(Kontak.items())
print()
del Kontak['Dina']
print('Hapus Kontak Dina')
print(Kontak.items())

