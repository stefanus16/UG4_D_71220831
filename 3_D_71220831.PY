masukan=input("masukan sebuah kalimat: ")

def carikata(masukan):
    carikata=masukan.split()
    katapanjang=carikata(0)

    for kata in carikata:
        if len(kata) > len(katapanjang):
            katapanjang = kata
carikata(masukan)