bilangan=list(map(int,input("masukan sekumpulan bilangan(pisahkan dnegan koma): ").split()))
terkecil = min(bilangan, key=lambda x: x)
terbesar = max(bilangan, key=lambda x: x)

print("bilangan terbesar dari kumpulan bilangan yang di inpuut adalah: ",terbesar)
print("bilangan terkecil dari kumpulan bilangan yang di input adalah: ",terkecil)