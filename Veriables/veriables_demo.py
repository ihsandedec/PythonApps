"""
    1- Bir müşterinin aşağıdaki bilgileri için değişken oluşturunuz.

    Müşteri adı
    Müşteri soyadı
    Müşteri ad + soyad
    Müşteri cinsiyet
    Müşteri tc kimlik
    Müşteri doğum yılı
    Müşteri adres bilgisi   
    Müşteri yaşı 
"""
musteriAdi = "İhsan"
musteriSoyadi = "Dedeç"
musteriAdSoyad = musteriAdi + musteriSoyadi
print(musteriAdSoyad)
musteriCinsiyet = True
musteriTC = "12312312345" 
musteriDogumYili = 2000
musteriAdres = "İstanbul"
musteriYas = 2024 - musteriDogumYili
print(musteriYas)


"""
    2- Aşağıdaki siparişlerin toplam bilgisini hesaplayınız.
    
    Sipariş 1 => 110    TL
    Sipariş 2 => 1100.5 TL
    Sipariş 3 => 356.95 TL

"""

siparis01,siparis02,siparis03 = (110,1100.5,356.95)
toplam = siparis01+siparis02+siparis03
print(toplam)

