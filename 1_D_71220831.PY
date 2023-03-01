print("==================== BARIS ARITMATIKA ====================")
bilanganawal=int(input("masukan bilangan awal: "))
selisih=int(input("masukan selisih bilangan: "))
banyaksuku=int(input("masukan banyaknya suku: "))

jumlah=0
n=1

while n<= banyaksuku:
    
    jumlah += bilanganawal
    bilanganawal+=selisih
    n+=1

print("total dari deret aritmatika tersebut adalah : ",jumlah)