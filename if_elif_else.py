x = 6
if x == 5 :
    print("Evet x = 5")
else : 
    print("Hayır x 5'e eşit değil")


kullaniciAdi = "Anlaşılır ekonomi"
password = "123456"

if kullaniciAdi == "Anlaşılır ekonomi" and password == "123456" :
    print("Giriş başarılı")
else :
    print("Bilgilerinizi kontrol edin")

print("-" * 30)

kA = input("Kullanıcı adını gir : ")
pswrd = input("Şifre gir : ")

#? alternatif 1

if kA == "Ahmet" and pswrd == "123456" : 
     print("Giriş başarılı") 

elif not(kA == "Ahmet") and pswrd == "123456" : 
     print("Kullanıcı adını kontrol et ")

elif kA == "Ahmet" and not(pswrd == "123456") : 
     print("Şifreni kontrol et ")

else : print("Giriş Başarısız")

print("-" * 30)
#? alternatif 2

sistemKA = "Aslıhan"
sistemPswrd = "1234567"

if kA == sistemKA and pswrd == sistemPswrd : 
    print("Giriş başarılı") 
elif kA != sistemKA and pswrd == sistemPswrd :
    print("Kullanıcı adını kontrol et ")
elif kA == sistemKA and pswrd != sistemPswrd :
    print("Şifreni kontrol et ")
else : print("Giriş Başarısız")
print("-" * 30)