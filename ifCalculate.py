print(""" Merhaba! Yapmak istediğiniz işlemi seçiniz:
    
[1] Toplama
[2] Çıkarma
[3] Çarpma 
[4] Bölme
[5] Üs Alma
[Q] Çıkış
""")



islem = str(input("Yapmak istediğiniz işlemi seçiniz :"))



if islem == "Q" or islem == "q" :
    print("Çıkış Yaptınız..")
    quit

elif islem == "1" :
    sayi1 = int(input("İlk sayıyı giriniz: "))
    sayi2 = int(input("İkinci sayıyı giriniz: "))
    print(f'{sayi1} + {sayi2} = {sayi1 + sayi2}') 

elif islem == "2" :
    sayi1 = int(input("İlk sayıyı giriniz: "))
    sayi2 = int(input("İkinci sayıyı giriniz: "))
    print(f'{sayi1} - {sayi2} = {sayi1 - sayi2}') 

elif islem == "3" :
    sayi1 = int(input("İlk sayıyı giriniz: "))
    sayi2 = int(input("İkinci sayıyı giriniz: "))
    print(f'{sayi1} * {sayi2} = {sayi1 * sayi2}') 

elif islem == "4" :
    sayi1 = int(input("İlk sayıyı giriniz: "))
    sayi2 = int(input("İkinci sayıyı giriniz: "))
    print(f'{sayi1} / {sayi2} = {sayi1 /  sayi2}') 

elif islem == "5" :
    sayi1 = int(input("İlk sayıyı giriniz: "))
    sayi2 = int(input("İkinci sayıyı giriniz: "))
    print(f'{sayi1} ** {sayi2} = {sayi1 **sayi2}') 
    



