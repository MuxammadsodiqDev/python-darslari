#19-dars
 #1-amaliyot
"""
def tugilgan_yili(ism, yosh):
    '''Foydalanuvchidan ism va yoshini so'rab,
    uni tug'ilgan yilini hisobyadigan funksiya'''
    print(f'{ism.title()} siz {2023-int(yosh)}-yilda tug\'ilgan siz')
ism=input('Salom, ismingizni ayting: ')
yosh=input(f'{ism.title()} yoshingizni ham kiriting: ')
tugilgan_yili(ism, yosh)
"""
 #2-amaliyot
"""
def hisob_kitob(son):
    '''Sonni kvadrati va kubini hisoblaydigan funksiya'''
    print(f'{son} ni kvadrati={int(son)**2}\n'
          f'{son} ni kubi={int(son)**3}')
son=input('Salom, biror son kiriting: ')
hisob_kitob(son)
"""
 #3-amaliyot
"""
def juft_toq_aniqlovchi(son):
    '''Sonni toq yoki juft ekanini aniqlovchi funksiya'''
    if son%2==0:
        print(f'{son} juft son')
    else:
        print(f'{son} toq son')
son =int(input('Iltimos biror son kiriting: '))
juft_toq_aniqlovchi(son)
"""
 #4-amaliyot
"""
def taqqoslash_fucntion(son1, son2):
    '''Sonlarni taqqoslab kattasini consolga chiqaradi,
    agar sonlar teng bo'lsa sonlar teng degan yozuv chiqaradi'''
    if son1<son2:
        print(son2)
    elif son1>son2:
        print(son1)
    else:
        print('sonlar teng')
son1=int(input('1-sonni kiriting: '))
son2=int(input('2-sonni kiriting: '))
taqqoslash_fucntion(son1, son2)
"""
 #5-amaliyot
"""
def hisoblash(x,y):
    '''Foydalanuvchidan x va y ni qiymatlarini olib
    x^y ni hisoblaydigan funksiya'''
    print(f'x^y={x**y}')
x=int(input('x= '))
y=int(input('y= '))
hisoblash(x, y)
"""
 #6-amaliyot
"""
def hisoblash(x,y=2):
    '''Foydalanuvchidan x va y ni qiymatlarini olib
    x^y ni hisoblaydigan funksiya'''
    print(f'x^y={x**y}')
x=int(input('x= '))
hisoblash(x)
"""
 #7-amaliyot
"""
def qoldiqli_bolish(son):
    '''Foydalanuchidan son qabul qilib olib,
    uni 2 dan 10 gacha bolganda qoldiksizlarini topadidigan funksiya'''
    qoldiqsiz=[]
    for n in range(2,11):
        if son%n==0:
            qoldiqsiz.append(n)
    print(f"{son} quyudagilarga qoldiqsiz bo'linadi ekan\n {qoldiqsiz}") 
son=int(input('biror sonni kiriting: '))
qoldiqli_bolish(son)
print(qoldiqli_bolish.__doc__)
"""