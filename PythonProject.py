# MAIN MENU
mobil = {
    '101\t\t Toyota Avanza\t\t\t' : 450000,
    '102\t\t Toyota Fortuner\t\t' : 850000,
    '103\t\t Mitsubishi Pajero Sport\t': 1000000,
    '104\t\t Mitsubishi Xpander\t\t' : 950000,
    '105\t\t Honda Jazz\t\t\t' : 650000,
    '106\t\t Honda Civic\t\t\t' : 650000,
    '107\t\t Toyota Hiace\t\t\t' : 1300000,
    '108\t\t Elf Long\t\t\t' : 1500000
}

avanza = {
    'Hitam\t' : 2,
    'Silver\t' : 1
}
fortuner = {
    'Hitam\t' : 1,
    'Silver\t' : 1,
    'Putih\t' : 1
}
pajero = {
    'Putih\t' : 2
}
xpander = {
    'Putih\t' : 3
}
jazz = {
    'Merah\t' : 3,
    'Kuning\t' : 1,
    'Putih\t' : 2
}
civic = {
    'Hitam\t' : 3,
    'Silver\t' : 2
}
hiace = {
    'Silver\t' : 5,
    'Putih\t' : 5
}
elf = {
    'Putih\t' : 7
}

def avz() :
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('\nBerikut adalah warna dan stok TOYOTA AVANZA yang tersedia.')
    print('\nWARNA', '\t    STOK')
    for key,val in avanza.items():
        print('{}     {}' .format(key,val))

def frt() :
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('\nBerikut adalah warna dan stok TOYOTA FORTUNER yang tersedia.')
    print('\nWARNA', '\t    STOK')
    for key,val in fortuner.items():
        print('{}     {}' .format(key,val))

def pjr() :
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('\nBerikut adalah warna dan stok MITSUBISHI PAJERO SPORT yang tersedia.')
    print('\nWARNA', '\t    STOK')
    for key,val in pajero.items():
        print('{}     {}' .format(key,val))

def xpd() :
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('\nBerikut adalah warna dan stok MITSUBISHI XPANDER yang tersedia.')
    print('\nWARNA', '\t    STOK')
    for key,val in xpander.items():
        print('{}     {}' .format(key,val))

def jzz() :
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('\nBerikut adalah warna dan stok HONDA JAZZ yang tersedia.')
    print('\nWARNA', '\t    STOK')
    for key,val in jazz.items():
        print('{}     {}' .format(key,val))

def cvc():
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('\nBerikut adalah warna dan stok HONDA CIVIC yang tersedia.')
    print('\nWARNA', '\t    STOK')
    for key,val in civic.items():
        print('{}     {}' .format(key,val))

def hce() :
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('\nBerikut adalah warna dan stok TOYOTA HIACE yang tersedia.')
    print('\nWARNA', '\t    STOK')
    for key,val in hiace.items():
        print('{}     {}' .format(key,val))

def lfl() :
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('\nBerikut adalah warna dan stok ELF LONG yang tersedia.')
    print('\nWARNA', '\t    STOK')
    for key,val in elf.items():
        print('{}     {}' .format(key,val))

#2

def info():
    while(True):
        print('\nUntuk mengetahui informasi tentang warna mobil dan jumlah stok yang tersedia, masukkan kode mobil sesuai daftar di atas.')
        pilihan = input('KODE: ').upper()
        if (pilihan == '101'):
            avz()
            break
        elif (pilihan == '102'):
            frt()
            break
        elif (pilihan == '103'):
            pjr()
            break
        elif (pilihan == '104'):
            xpd()
            break
        elif (pilihan == '105'):
            jzz()
            break
        elif (pilihan == '106'):
            cvc()
            break
        elif (pilihan == '107'):
            hce()
            break
        elif (pilihan == '108'):
            lfl()
            break
        else:
            print('\nKode yang anda masukkan tidak terdapat pada daftar.')

#3

def pesan():
    while(True):
        inputpesan = input('\nMasukkan: \n"Y" untuk memesan armada ini. \n"N" untuk melihat armada yang lain. \nY/N: ').upper()
        if (inputpesan == 'Y'):
            print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print('\nMasukkan data anda untuk proses pemesanan!')
            nama = input('Nama lengkap: ').capitalize()
            hp = input('No. Handphone: ')
            jumlah = input('Jumlah armada yang dipesan: ')
            warna = input('Warna armada yang dipesan: ').capitalize()
            lamasewa = input('Lama hari penyewaan: ')
            catatan = input('Masukkan catatan tambahan (jika diperlukan): ').capitalize()
            dictcust = {
                'Nama\t\t' : '{}' .format(nama),
                'Nomer HP\t': '{}' .format(hp),
                'Jumlah\t\t' : '{}' .format(jumlah),
                'Warna\t\t' : '{}' .format(warna),
                'Lama sewa\t' : '{}' .format(lamasewa),
                'Catatan\t\t' : '{}' .format(catatan)
            }

            def koreksi():
                print('\nPeriksa kembali data Anda. Pastikan data yang Anda masukkan benar!')
                for key,val in dictcust.items():
                    print('{} : {}' .format(key,val))
            koreksi()
            while(True):
                print('\nMasukkan "Y" jika data anda sudah benar.\nMasukkan "U" jika Anda hendak mengganti data.\nMasukkan "D" untuk menghapus catatan.')
                update = input('Y/U/D: ').upper()
                if (update == 'Y'):
                    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                    print('Data berhasil disimpan!\nTim "HEPPI RENT CAR" akan segera menghubungi anda untuk proses pembayaran, dll.')
                    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                    daftar()
                elif (update == 'U'):
                    inputupdate = input('\nSilahkan tuliskan data yang hendak anda ubah dengan cara berikut:\n1 = Nama \n2 = Nomor HP \n3 = Jumlah \n4 = Warna \n5 = Lama sewa \nMasukkan nomor bagian yang akan diganti: ').lower()
                    updatecust = input('Masukkan kata/angka pengganti: ').capitalize()
                    if (inputupdate == '1'):
                        dictcust['Nama\t\t'] = '{}' .format(updatecust)
                        koreksi()
                    elif (inputupdate == '2'):
                        dictcust['Nomer HP\t'] = '{}' .format(updatecust)
                        koreksi()
                    elif (inputupdate == '3'):
                        dictcust['Jumlah\t\t'] = '{}' .format(updatecust)
                        koreksi()
                    elif (inputupdate == '4'):
                        dictcust['Warna\t\t'] = '{}' .format(updatecust)
                        koreksi()
                    elif (inputupdate == '5'):
                        dictcust['Lama sewa\t'] = '{}' .format(updatecust)
                        koreksi()
                    else:
                        print('Perintah yang Anda masukkan salah!')
                elif (update == 'D'):
                    del dictcust['Catatan\t\t']
                    koreksi()
                else :
                    print('Perintah yang Anda masukkan salah!')
        elif (inputpesan == 'N'):
            dictmobil()
            info()
        else:
            print('\nPesan yang Anda masukkan salah.')

#1

inputNama = input('Selamat Datang di "HEPPI RENT CAR"! Silahkan masukkan nama Anda: ').capitalize()

print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

print('\nHai {}, kami memiliki beberapa jenis mobil yang dapat kamu sewa dengan harga yang bersahabat.' .format(inputNama))

def dictmobil():
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('\nHai {}, berikut adalah daftar mobil yang tersedia beserta harga sewa per hari (maksimal 24 jam).\n' .format(inputNama))
    print('KODE','\t\t       NAMA MOBIL', '\t\t HARGA SEWA')
    for key,val in mobil.items():
        print ('{}  {}' .format(key,val))

def daftar():
    while(True):
        inputKatalog = input('\nSilahkan masukkan:\n"Y" untuk melihat beberapa jenis mobil yang siap menemani perjalananmu.\n "N" untuk membatalkan.\nY/N: ').upper()
        if (inputKatalog == 'Y'):
            dictmobil()
            info()
            pesan()
        elif (inputKatalog == 'N'):
            print('\nTerima kasih telah mengunjungi "HEPPI RENT CAR", kami tunggu kehadiran Anda berikutnya. ^_^')
            break
        else:
            print('\nPesan yang Anda masukkan salah.')
daftar()