website = "http://www.sadikturan.com"
kursAdi = "Python Dersleri: Sıfırdan İleri Seviye Python Programlama."

sonuc = len(website)
sonuc = len(kursAdi)

sonuc = website[7:10]

karakterSayisi = len(website)
sonuc = website[karakterSayisi-3:karakterSayisi]

sonuc = kursAdi[0:15]
sonuc = kursAdi[:15]
sonuc = kursAdi[-15:]

sonuc = kursAdi[::-1]



s = 'Hello world'
s = s[0:6] + 'W' + s[-4:]
print(s)


print('abc ' * 3)

name, surname, age, job = 'ismail','Dedeç', 20, 'öğrenci' 


sonuc = "Benim adım " + name + " " + surname + ",Yaşım " + str(age) + " ve mesleğim " + job + "."
sonuc = "Benim adım {0} {1},Yaşım {2} ve mesleğim {3}".format(name,surname,age,job)
sonuc = f"Benim adım {name} {surname},Yaşım {age} ve mesleğim {job}."

print(sonuc)

