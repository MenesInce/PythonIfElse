isim = str(input("Adınızı Giriniz: "))
yas = int(input("Yaşınızı Giriniz: "))
egitim = str(input("Eğitim Durumunuzu Giriniz: "))

egitim1 = ("İlkokul","Ortaokul","Lise","Üniversite")

if egitim not in egitim1 :
    print("Geçerli bir eğitim durumu giriniz")
elif (yas >= 18) and (egitim == "Lise" or egitim == "Üniversite") :
    print(f'{isim} ehliyet almak için şartları sağlıyorsun. ')
else : print(f'{isim} ehliyet almak için uygun değilsin')
