# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 17:02:23 2020

aşağıda girilen değerlerden farklı yolla çıktılar alınmaya çalışılmıştır. 
"""
deger1=input("Lütfen birinci degeri giriniz: ")
print("Girdiginiz ilk deger {} ve degerin türü {}".format(deger1,type(deger1)))

deger2=input("Lütfen ikinci degeri giriniz: ")
print(f'Girdiginiz ucuncu deger: {deger2} ve degerin türü ',type(int(deger2))) #input ile alınan her değer string tipinde olduğu için farklı bir çıktı almak adına tip dönüşümü yapıldı.

deger3=input("Lütfen ücüncü degeri giriniz: ")
print(f'Girdiginiz ucuncu deger: {deger3} ve degerin türü {type(deger3)}')

deger4=input("Lütfen dördüncü degeri giriniz: ")
print("Girdiginiz dorduncu deger {} ve degerin türü {}".format(deger4,type(deger4)))


deger5=input("Lütfen besinci degeri giriniz: ","\n" )
print("Girdiginiz besinci deger ",deger5, "ve degerin türü ",type(deger5))




