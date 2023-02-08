print("=============== KASIR ===============")

hb = int(input("Harga Barang : ")) 
mb = input("Apakah Anda Akan Membeli Barang Lagi? [ya/tidak] : ")

if mb == "ya" :
    while True:
        hb1 =int(input("harga barang : ")) 
        mb1 =(input("Apakah Anda Akan Membeli Barang Lagi? [ya/tidak] : "))
        if mb1 == "ya":
            continue
        elif mb1 == "tidak":
            break
        else:
            break


elif mb == "tidak":
    print("Total Pembelian",)
else:
    print("Error")

        