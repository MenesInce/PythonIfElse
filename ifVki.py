print("Merhaba, Hoş geldiniz!")
print("-" * 30)

kilo = int(input("Kilonuzu giriniz : "))
boy = int(input("Boyunuzu cm cinsinden giriniz : "))

vki = round(((kilo)/(boy/100)**2),2) #* round virgülden sonra kaç basamak olacağını belirler

if vki < 18.5 : 
    print("Vücut kitle indeksiniz {}. Düşük kilolu grubundasınız. " .format(vki))
elif vki > 18.5 and vki <=24.9 :
    print(f'Vücut kitle indeksiniz {vki}. Normal kilolu grubundasınız.')
elif vki > 25 and vki <=29.9 :
    print(f'Vücut kitle indeksiniz {vki}. Fazla kilolu grubundasınız.')
elif vki > 30 and vki <=40 :
    print(f'Vücut kitle indeksiniz {vki}. Obez kilolu grubundasınız.')
else :
    print(f'Vücut kitle indeksiniz {vki}. Aşırı kilolu grubundasınız.')