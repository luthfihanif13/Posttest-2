#Membuat Biodata sederhana
#list

from typing import List


print("Biodata sederhana menggunakan bahasa pemrograman python ")

nama = input(str("Nama :"))
kelas = input(str("kelas : ")) 
nim = int(input("Nim saya adalah : "))
umur = float(input("Sekarang berumur : "))
tunjangan = float(input("Tunjangan senilai : "))
#list
cita_cita = ["Software engineer", "System analyst", "IT consultant"]


print("Halo %s" % nama)
print("Kelas : %s" % kelas)
print("Nim : %d" % nim)
print("Umur : %d" % umur)
print("Tunjangan = %f" % tunjangan)
print("bercita-cita sebagai : " +cita_cita[0])
print("Aamiin")