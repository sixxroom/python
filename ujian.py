nama = 'Riadh Raihan'
kelas = '1IA16'
npm = '51424199'

print(f"Nama saya {nama}")
print(f"saya dari kelas {kelas}")
print(f"dan npm saya {npm}")


def show_menu_home():
    print("""
=============================    
SELAMAT DATANG DI FOODIEAAP
=============================
1. Lihat menu
2. Cek Ketersediaan
3. order 
4. Cetak pesanan
5. Exit    
""")

def lihat_produk(saldo):
    print('\nList Produk : ')
    print('1. burger : Rp.25000 /pcs')
    print('2. kebab : Rp.15000 /pcs')
    print('3. pizza : Rp.50000 /pcs')
    print('\n')
    print(f'saldo anda : {saldo}')

def cek_ketersediaan(burger, kebab, pizza):
    print('\nList Ketersediaan : ')
    print(f'1. burger : {burger}')
    print(f'2. kebab : {kebab}')
    print(f'3. pizza : {pizza}')

def beli(saldo, burger, kebab, pizza):
    lihat_produk(saldo)
    cek_ketersediaan(burger, kebab, pizza )
    pilihan = input('Pilih Yang akan dibeli : ')
    if pilihan == '1':
        saldo
        jenis = 'burger'
        harga = 25000
        jumlah = int(input('Berapa pcs burger yang ingin anda beli: '))
        total = jumlah * harga
        pembelian = saldo - total
        if burger < jumlah:
            print('Maaf stoknya tidak ada')
        else:
            if total > saldo:
                print('Maaf, saldo anda tidak cukup')
            else:
                print(f'Berhasil membeli {jenis} seharga {total} ')
                print(f'Saldo saat ini : {pembelian}')
                try :
                    with open('struk.txt','a') as struk:                        
                        struk.write('==========================\n')
                        struk.write('STRUK PEMBELIAN\n')
                        struk.write('==========================\n')
                        struk.write(f'nama barang : {jenis} \n')
                        struk.write(f'Harga Satuan : {harga} \n')
                        struk.write(f'total : {total} \n')
                        struk.write(f'Saldo Anda : {saldo} \n')
                        struk.write(f'Kembalian : {pembelian} \n')
                        struk.write('=' *40)
                        struk.write('\n')
                        struk.write('terimakasih telah membeli ditempat kami')
                except Exception as e:
                    print(e)
                                            
    elif pilihan == '2':
        saldo
        jenis = 'kebab'
        harga = 15000
        jumlah = int(input('Berapa pcs kebab yang ingin anda beli: '))
        total = jumlah * harga
        pembelian = saldo - total
        if kebab < jumlah:
            print('Maaf stoknya tidak ada')
        else:
            if total > saldo:
                print('Maaf, saldo anda tidak cukup')
            else:
                print(f'Berhasil membeli {jenis} seharga {total} ')
                print(f'Saldo saat ini : {pembelian}')
                try :
                    with open('struk.txt','a') as struk:                        
                        struk.write('==========================\n')
                        struk.write('STRUK PEMBELIAN\n')
                        struk.write('==========================\n')
                        struk.write(f'nama barang : {jenis} \n')
                        struk.write(f'Harga Satuan : {harga} \n')
                        struk.write(f'total : {total} \n')
                        struk.write(f'Saldo Anda : {saldo} \n')
                        struk.write(f'Kembalian : {pembelian} \n')
                        struk.write('=' *40)
                        struk.write('\n')
                        struk.write('terimakasih telah membeli ditempat kami')
                except Exception as e:
                    print(e)
                    
    elif pilihan == '3':
        saldo
        jenis = 'pizza'
        harga = 50000
        jumlah = int(input('Berapa pcs pizza yang akan anda beli: '))
        total = jumlah * harga
        pembelian = saldo - total
        if pizza < jumlah:
            print('Maaf stoknya tidak ada')
        else:
            if total > saldo:
                print('Maaf, saldo anda tidak cukup')
            else:
                print(f'Berhasil membeli {jenis} seharga {total} ')
                print(f'Saldo saat ini : {pembelian}')
                try :
                    with open('struk.txt','a') as struk:                        
                        struk.write('==========================\n')
                        struk.write('STRUK PEMBELIAN\n')
                        struk.write('==========================\n')
                        struk.write(f'nama barang : {jenis} \n')
                        struk.write(f'Harga Satuan : {harga} \n')
                        struk.write(f'total : {total} \n')
                        struk.write(f'Saldo Anda : {saldo} \n')
                        struk.write(f'Kembalian : {pembelian} \n')
                        struk.write('=' *40 )
                        struk.write('\n')
                        struk.write('terimakasih telah membeli ditempat kami')
                except Exception as e:
                    print(e)            
    else:
        print('Eror')

def cetak_struk():
    try:
        with open('struk.txt','r') as saw:
            lihat = saw.read()
            print(lihat)
    except Exception as e:
        print(e)

def main():
    saldo = 100000
    burger = 5
    kebab = 6
    pizza = 10
    

    while True:
        
        show_menu_home()
        inputan = input('Pilih menu (1-5) : ')
        if inputan == '1':
            lihat_produk(saldo)
        elif inputan == '2':
            cek_ketersediaan(burger, kebab, pizza)
        elif inputan == '3':
            beli(saldo, burger, kebab, pizza)
        elif inputan == '4':
            cetak_struk()
        elif inputan == '5':
            break
        else :
            print('Inputan error')
            
if __name__ == '__main__':
    main()