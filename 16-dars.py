#17-dars
 #1-amaliyot
'''
print('Salom,so\'rovnamada qatnashing so\'rovnomani to\'htatish uchun stop ni yozing.')
savol='Yaxshi ko\'rgan kitobingizni kiriting: '
kitob=''
while kitob !='stop':
    kitob=input(savol)
print('Savolnoma to\'htadi')
'''
 #2-amaliyot
  #boolean
'''
print('Salom, muzeyga hush kelibsiz.'
      'Kirib bo\'lganingizdan keyin (quit) va '
      '(exit) kalit so\'zlarini unitma')
savol='iltimosh yoshingizni ayting: '
summa=0
skil=True
yosh=''
while skil:
    yosh=input(savol)
    if yosh=='exit' or yosh=='quit':
        skil=False
    else:
        yosh=int(yosh)
        if yosh<=7:
            summa=2000
        elif yosh>7 and yosh<=18:
            summa=3000
        elif yosh>18 and yosh<=65:
            summa=10000
        else:
            summa=0
        print(f'siz uchun belit narxi= {summa}')
'''
  #break  
'''     
print('Salom, muzeyga hush kelibsiz.'
      'Kirib bo\'lganingizdan keyin (quit) va '
      '(exit) kalit so\'zlarini unitma')
savol='iltimosh yoshingizni ayting: '
summa=0
yosh=''
while True:
    yosh=input(savol)
    if yosh=='exit' or yosh=='quit':
        break
    else:
        yosh=int(yosh)
        if yosh<=7:
            summa=2000
        elif yosh>7 and yosh<=18:
            summa=3000
        elif yosh>18 and yosh<=65:
            summa=10000
        else:
            summa=0
        print(f'siz uchun belit narxi= {summa}')
'''
  #if
'''
print('Salom, muzeyga hush kelibsiz.'
      'Kirib bo\'lganingizdan keyin (quit) va '
      '(exit) kalit so\'zlarini unitma')
savol='iltimosh yoshingizni ayting: '
summa=0
yosh=''
while yosh!='exit' or yosh!='quit':
    yosh=input(savol)
    if yosh!='exit' or yosh!='quit':      
        yosh=int(yosh)
        if yosh<=7:
            summa=2000
        elif yosh>7 and yosh<=18:
            summa=3000
        elif yosh>18 and yosh<=65:
            summa=10000
        else:
            summa=0
        print(f'siz uchun belit narxi= {summa}')
'''
savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat=='exit':
        break
    else:
        qiymat=float(qiymat)
        if qiymat>0:
            ildiz = float(qiymat)**(0.5)
            print(f"{qiymat} ning ildizi {ildiz} ga teng")
print('dastur to\'htadi')     
    