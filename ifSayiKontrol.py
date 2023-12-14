sayi = int(input("Bir sayı girin : "))
control = (sayi > 0) and (sayi % 2 == 1) 

if control:
    print(f'{sayi} pozitif tek sayıdır! ')
else : 
      print(f'{sayi} pozitif tek sayı değildir! ')