import os
print("-----------------------------------------------------")
print("|\tSelamat Datang di Cek Diagnosa Demam Berdarah\t|")
print("-----------------------------------------------------")
nama = input("Nama\t : ")
pilihan = input("Halo, "+nama+"\nApakah anda ingin melakukan diagnosa? (y/n)")

os.system("clear")

while pilihan == "y":
    print("\nApakah anda merasakan gejala berikut ini?")
    print("1. Demam")
    print("2. Sakit kepala")
    print("3. Mual")
    print("4. Muntah")
    print("5. Nyeri belakang bolah mata")
    print("6. Kulit kemerahan")
    print("7. Nyeri otot dan Tulang sendi")
    
    diag1 = input("Jawab (y/n)")

    if diag1 == "y":
        print("\nApakah anda juga mengalami Gejala berikut ini?")
        print("1. Muncul bintik kemerahan di kulit")
        print("2. Gusi berdarah")
        print("3. Mimisan")
        diag2 = input("Jawab (y/n")
        
        if diag2 == "y":
            print("\nHi, "+nama+"Hasil awal diagnosa anda adalah: ")
            print("Anda teridentifiasi Deman berdarah, segera lakukan cek darah dan hubungi dokter")
        elif diag2 == "n":
            print("Hi, "+nama+"anda memiliki tanda terkena demam berdarah, sebaiknya lakukan cek darah dan hubungi dokter")
        else:
            print("Hi, "+nama+"Anda Sehat")

    else :
        print("Hi, "+nama+"Anda Sehat")

print("--------------------------------------------------------")
pilihan = input("Halo, "+nama+"Apakah anda ingin melakukan diagnosa ulang?(y/n) ")

if pilihan == "y":
    os.system("clear")
    print("----------------------------------------------------")
    print("|\tSelamat Datang di Cek Diagnosa Demam Berdarah\t|")
    print("----------------------------------------------------")
else:
    print("-------------------TERIMA KASIH---------------------")