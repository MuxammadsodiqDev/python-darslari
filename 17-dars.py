#18-dars
 #1-amaliyot
'''
buyurtmalar=[]
n=1
while True:
    buyurtma=input(f'{n}-ni buyurtmani kiriting: ')
    n+=1
    if buyurtma=="bo'ldi":
        print('buyurtma ro\'yhati: ')
        print(buyurtmalar)
        break
    else:
        buyurtmalar.append(buyurtma)
'''
 #2-amaliyot
'''
elektron_bazor={}
elektron=True
while elektron:
    mahsulot=input('mahsulotni kiriting: ')
    if mahsulot== 'tugadi':
        elektron=False
    else:
        narx=input(f'{mahsulot} narxini kiriting:')
        elektron_bazor[mahsulot]=int(narx)
print(elektron_bazor)
''' 
 #3-amaliyot
buyurtmalar=[]
n=1
while True:
    buyurtma=input(f'{n}-ni buyurtmani kiriting: ')
    n+=1
    if buyurtma=="bo'ldi":
        print('buyurtma ro\'yhati: ')
        print(buyurtmalar)
        break
    else:
        buyurtmalar.append(buyurtma)
elektron_bazor={}
elektron=True
while elektron:
    mahsulot=input('mahsulotni kiriting: ')
    if mahsulot== 'tugadi':
        elektron=False
    else:
        narx=input(f'{mahsulot} narxini kiriting:')
        elektron_bazor[mahsulot]=int(narx)
print(elektron_bazor)
for buyurtma in buyurtmalar:
    if buyurtma in elektron_bazor:
        print(f"{buyurtma} narxi {elektron_bazor[buyurtma]}")
    else:
        print(f"Bizda {buyurtma} mahsulot yo'q")