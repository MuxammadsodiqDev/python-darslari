#19-dars
 #dars ichidagi vazifa
'''
def oraliq(min,max,qadam=2):
    sonlar=[]
    while min<max:
        sonlar.append(min)
        min+=qadam
    return sonlar
print(oraliq(0,21))
'''
 #dars ichidagi vazifa
"""
def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
    avto = {'kompaniya':kompaniya,
            'model':model,
            'rang':rangi,
            'korobka':korobka,
            'yil':yili,
            'narh':narhi}
    return avto

print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
avtolar=[] # salondagi avtolar uchun bo'sh ro'yxat
while True:
    print("\nQuyidagi ma'lumotlarni kiriting: ")
    kompaniya=input("Ishlab chiqaruvchi: ")
    model=input("Modeli: ")
    rangi=input("Rangi: ")
    korobka=input("Korobka: ")
    yili=input("Ishlab chiqarilgan yili: ")
    narhi=input("Narhi: ")
    
    #Foydalanuvchi kiritdan ma'lumotlardan avto_info yordamida 
    #lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
    avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
    
    # Yana avto qo'shish-qo'shmaslikni so'raymiz
    javob = input("Yana avto qo'shasizmi? (yes/no): ")
    if javob=='no':
        break
"""
 #1-amaliyot
"""
def shaxsiy_malumotlar(ism, familiya,tugilgan_yili,tugilgan_joyi,
                       email_manzil=None,telefon_raqami=None ):
    "foydalnuvchidan shaxsiy malumotlarini so'rab uni lug'at shaklida chiqaruvchi funksiya"
    yosh=2023-int(tugilgan_yili)
    malumotlar={'ism':ism,"familiya":familiya,'tugilgan_yili':tugilgan_yili,"yosh":yosh,
                'tugilgan_joyi':tugilgan_joyi,"email_manzil":email_manzil,
                'telefon_raqam':telefon_raqami}
    return malumotlar
print('Iltimos quyidagi malumotlarni kiriting: ')
ism=input('Ismingiz: ')
familiya=input('Familiyangizni kiriting: ')
tugilgan_yili=input('Tug\'ilgan yilingizni kiriting: ')
tugilgan_joyi=input('Tug\'ilgan joyingizni kiriting: ')
savol =input('email manzilingiz va telefon raqamini kitishni'
             'hohlaysizmi? ha\yoq: ')
if savol=="ha":
    email_manzil=input('Email manzilingizni kiriting: ')
    telefon_raqami=input('Telefon raqami: ')
    print(shaxsiy_malumotlar(ism, familiya, tugilgan_yili, tugilgan_joyi
                             ,email_manzil,telefon_raqami))
else:
    print(shaxsiy_malumotlar(ism, familiya, tugilgan_yili, tugilgan_joyi))
"""
 #2-amaliyot
"""
def shaxsiy_malumotlar(ism, familiya,tugilgan_yili,tugilgan_joyi,
                       email_manzil=None,telefon_raqami=None ):
    "mijozlardan shaxsiy malumotlarini so'rab uni lug'at shaklida chiqaruvchi funksiya"
    yosh=2023-int(tugilgan_yili)
    malumotlar={'ism':ism,"familiya":familiya,'tugilgan_yili':tugilgan_yili,"yosh":yosh,
                'tugilgan_joyi':tugilgan_joyi,"email_manzil":email_manzil,
                'telefon_raqam':telefon_raqami}
    return malumotlar
mijozlar=[]
while True:
    print('Iltimos quyidagi malumotlarni kiriting: ')
    ism=input('Ismingiz: ')
    familiya=input('Familiyangizni kiriting: ')
    tugilgan_yili=input('Tug\'ilgan yilingizni kiriting: ')
    tugilgan_joyi=input('Tug\'ilgan joyingizni kiriting: ')
    savol =input('email manzilingiz va telefon raqamini kitishni'
                 'hohlaysizmi? ha\yoq: ')
    if savol=="ha":
        email_manzil=input('Email manzilingizni kiriting: ')
        telefon_raqami=input('Telefon raqami: ')
        mijozlar.append(shaxsiy_malumotlar(ism, familiya, tugilgan_yili, tugilgan_joyi
                                 ,email_manzil,telefon_raqami))
    else:
       mijozlar.append(shaxsiy_malumotlar(ism, familiya, tugilgan_yili, tugilgan_joyi))
    if savol=='ha':
        break
print(mijozlar)
"""
 #3-amaliyot
"""
def toqqosla(sonlar):
    '3ta sonni taqqoslaydigan funksiya'
    if sonlar[0]<sonlar[1]:
        max=sonlar[1]
    else:
        max=sonlar[0]
    if max<sonlar[2]:
        max=sonlar[2]
    return max
sonlar=[]
for n in range(3):
    sonlar.append(int(input(f'{n+1}-ni sonni kiriting: ')))
print(toqqosla(sonlar))
"""
 #4-amaliyot
"""
import math
def aylana_parametrlari(radius):
    diametri=radius*2
    primetri=radius*2*math.pi
    yuzi=radius*math.pi**2
    parametrlar={'radiusi':radius,'diametri':diametri,
                 'primetri':primetri,'yuzi':yuzi}
    return parametrlar
radius=int(input('radiusni kiritishingizni so\'raymiz: '))
print(aylana_parametrlari(radius))
"""
 #5-amaliyot
"""
def tubmi(oraliq):
    tubsonlar=[]
    for son in oraliq:
        if son>0:
            if son==1 or son==0:
                son1=son
            elif son==2 or son==3 or son==5 or son==7:
                tubsonlar.append(son)
            elif son%2!=0 and son%3!=0 and son%5!=0 and son%7!=0:
                tubsonlar.append(son)
    return tubsonlar
print(tubmi(range(30)))
"""
 #6-amaliyot
"""
def fibonchi_sonlari(son):
    fibonchi=[1,1]
    son1=1
    son2=1
    son3=1
    n=2
    for n in son:
        son1=son2
        son2=son3
        son3=son1+son2
        fibonchi.append(son3)
        if len(fibonchi)==len(son):
            break
    return fibonchi
son=list(range(int(input('Biror son kiriting: '))))
print(fibonchi_sonlari(son))
"""
def mijoz_info(ism, familiya, tyil, tjoy, email='',tel=None):
    """Mijoz haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
    mijoz = {'ism':ism,
             'familiya':familiya,
             'tyil':tyil,
             'yoshi':2020-tyil,
             'tjoy':tjoy,
             'email':email,
             'telefon':tel}
    return mijoz

print("Mijoz haqida ma'lumotlarni kiriting.")
mijozlar =[]
while True:
    ism = input("Ismi: ")
    familiya = input("Familiyasi: ")
    tyil = int(input("Tug'ilgan yili: "))
    tjoy = input("Tug'ilgan joyi: ")
    email = input("Email: ")
    telefon = input("Telefon raqami: ")
    mijozlar.append(mijoz_info(ism, familiya, tyil, tjoy, email, telefon))
    javob = input("Davom etasizmi? (ha/yo'q)")
    if javob!='ha':
        break

print("Mijozlar:")
for mijoz in mijozlar:
    print(f"{mijoz['ism'].title()} {mijoz['familiya'].title()}," 
          f"{mijoz['yoshi']} yoshda, telefoni: {mijoz['telefon']}")
    
    
    
    
    
    
    
    