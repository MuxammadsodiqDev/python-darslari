#21-dars
 #1 va 2-amaliyot
"""
def katta_harfla(matnlar):
    katta_harfli=[]
    while matnlar:
        matn=matnlar.pop()
        katta_harfli.append(matn.capitalize())
    return katta_harfli
matnlarim=['abbos universitutga kirdi','sardor oqishni zavushni oqiyapti'
         ,'sulaymon yaqinda uylanadi']  
print(katta_harfla(matnlarim[:]))
print(matnlarim)
"""
 #3-amaliyot
"""
def bahola(ismlar):
    baholar = {}
    for ism in ismlar:
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
        baholar[ism]=baho
    return baholar

talabalar = ['ali', 'vali', 'hasan', 'husan']
baholar = bahola(talabalar)
print(baholar)
"""
def bahola(ismlar):
    baholar={}
    for ism in ismlar:
        baho=int(input(f'{ism.title()}ning bahosini kiriting: '))
        baholar[ism.title()]=baho
    return baholar
talabalar=['abbos','ganisher','sattor','shoira']
print(bahola(talabalar))
    
    
    
    
    
    
    