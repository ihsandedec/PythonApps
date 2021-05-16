isimler = ['Ada','Yiğit','Hasan','Beril']
yaslar = [1998, 2000, 1998, 1987]

# 1-  "Cenk" ismini listenin sonuna ekledim
isimler.append('Cenk')

# 2-  "Sena" değerini listenin başına ekledim
isimler.insert(0,"Sena")
isimler.insert(-1,"Sena")
isimler.insert(len(isimler),"Sena")

# 3-  "Yiğit" ismini listeden sildim
# isimler.remove("Yiğit")
isimler.pop()
isimler.pop(0)

# 4-  "Yiğit" isminin indeksi nedir ?
index = isimler.index('Yiğit')
isimler.pop(index)
print(index)

# 5-  "Beril" listenin bir elemanı mıdır ?
sonuc = "Beril" in isimler
print(sonuc)

# 6-  Liste elemanlarını ters çevirdim
isimler.reverse()
yaslar.reverse()

# 7-  Liste elemanlarını alfabetik olarak sıraladım
isimler.sort()

# 8-  yaslar listesini rakamsal büyüklüğe göre sıraladım
yaslar.sort()

# 9-  s = "IPhone X,IPhone XR" karakter dizisini listeye çevirdim
s = "IPhone X,IPhone XR"
sonuc = s.split(',')
print(sonuc)

# 10- yaslar dizisinin en büyük ve en küçük elemanı nedir ?
print(min(yaslar))
print(max(yaslar))

# 11- yaslar dizisinde kaç tane 1998 değeri vardır ?
print(yaslar.count(1998))

# 12- yaslar dizisinin tüm elemanlarını sildim
yaslar.clear()

# 13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede sakladım

markalar = []

marka = input("marka: ")
markalar.append(marka)

marka = input("marka: ")
markalar.append(marka)

marka = input("marka: ")
markalar.append(marka)

print(markalar)

print(isimler)
print(yaslar)