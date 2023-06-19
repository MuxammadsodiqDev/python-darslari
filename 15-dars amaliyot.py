#15-dars
 #1-amaliytot
""" 
python= {"urganch":"haqida","kochalar":"tor","odamlar":"bez","havo":"sassiq",
         "binolar":"chala", "masjidlar":"obod", "togaraklar":"qimmat",
         "imkoniyatlar":"keng", "non":"qimmat","qizla":"kop"}
for kalit,qiymat in sorted(python.items()):
    print("kalit: "+kalit +"\nqiymat: "+qiymat +'\n')
"""
 #2-amaliyot
"""
davlat_poytaht={"uzbekiston":"toshkent", "finlandiya": "helsinki",
                "germaniya":"berlin","angliya":"london","ispaniya":"madrid",
                "turkiya":"ankara","qozog\'iston": "astana","avg\'oniston":
                    "kabul", "eron":"paris","qirg\'iziston":'biskek'}
for kalit in davlat_poytaht.keys():
    print(kalit.title()+"\n")
for qiymat in davlat_poytaht.values():
    print(qiymat.title()+"\n")
"""
 #3-topshiriq
"""
davlat_poytaxt={"uzbekiston":"toshkent", "finlandiya": "helsinki",
                "germaniya":"berlin","angliya":"london","ispaniya":"madrid",
                "turkiya":"ankara","qozog\'iston": "astana","avg\'oniston":
                    "kabul", "eron":"paris","qirg\'iziston":'biskek'}
davlat=input("istalgan davlatni ayting: ")
if davlat.lower() in davlat_poytaxt:
    print(f"{davlat.title()} poytaxti {davlat_poytaxt[davlat].title()}")
else:
    print("bizda unaqa malumot yoq")
"""
 #4-topshiriq
"""
menu={"shashlik":8000, "manti":25000, "tovuq":70000, "samsa":9000,
      "gumma": 6000, "sho\'rva": 18000, "barak": 15000,"boliq":72000,
      "gamburger":10000,"kabob": 30000}
buyurtmalar=[]
n=0
for n in range(3):
    print("buyurtmani ayting: ")
    buyurtma=input()
    print(f"{n+1}-{buyurtma}")
    buyurtmalar.append(buyurtma.lower())
for buyur in buyurtmalar:
    if buyur in menu:
        print(f"{buyur} ni narxi {menu[buyur]}")
    else:
        print("bizda bunaqa toam yoq")
"""  

















        