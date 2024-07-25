website = "http://www.sadikturan.com"
course  = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

# 1- 'course' karakter dizisinde kaç karakter bulunmaktadır ?
lengthCourse =len(course)
lengthWebsite =len(website)
print(lengthCourse)

# 2- 'website' içinden www karakterlerini alın.
result01 = website[7:10]
print(result01)

# 3- 'website' içinden com karakterlerini alın.
result02 = website[lengthWebsite-3 : lengthWebsite]
print(result02)

# 4- 'course' içinden ilk 15 ve son 15 karakterlerini alın.
result03 = course[0:15]
result04 = course[lengthCourse-15 : lengthCourse]
result05 =course[-15:]
print(result03)
print(result04)
print(result05)

# 5- 'course' ifadesindeki karakterleri tersten yazdırın.
result06 = course[::-1]

name, surname, age, job = 'İhsan','Dedeç', 24, 'mühendis' 

# 6- Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
#    'Benim adım İhsan Dedeç, Yaşım 24 ve mesleğim mühendis.' 
result06 = "Benim adım {} {}, Yaşım {} ve mesleğim {}".format(name,surname,age,job)
print(result06)

# 7- 'Hello world' ifadesindeki w harfini 'W' ile değiştirin.
s = 'Hello world'
s = s[0:6] + 'W'+ s[-4:]
print(s)

# 8- 'abc' ifadesini yan yana 3 defa yazdırın.
result = 'abc ' * 3