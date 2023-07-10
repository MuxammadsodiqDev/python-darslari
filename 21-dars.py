#21-dars
 #1-amaliyot
"""
def kopaytma(*sonlar):
    kopaytma=1
    for son in sonlar:
        kopaytma*=son   
    return kopaytma
print(kopaytma(1,2,3,4,5))
"""
 #2-amaliyot
def talaba_info(ism,familiya,**info):
    info["ismi"]=ism
    info["familiyasi"]=familiya
    return info
print(talaba_info('ganisher',"aliyev",yonalishi='amaliy matem',kursi=3))
print(talaba_info("zikrulla", "yashinov", yonalishi='amaliy matem',yoshi=18))
    
    
    