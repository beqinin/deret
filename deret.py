n = int(input("Berapa jumlah karakter yang akan dimasukkan? "))


arr = []
for _ in range(0,n):
  arr.append(input("Masukkan karakter apapun, boleh juga kata: "))


karakter_yang_dicari = input("Karakter apa yang kamu cari dari deret diatas? ")
jumlah_kemunculan = arr.count(karakter_yang_dicari)


print(f"Karakter {karakter_yang_dicari} muncul {jumlah_kemunculan} kali")