print("""******************                 
BEDEN-KİTLE İNDEXİ
******************
""")

kilo = int(input("Kilonuzu girin:"))
boy = float(input("Boyunuzu girin:"))

if kilo / boy * boy <= 18.5 :
    print("ZAYIF")
elif kilo / boy * boy == 18.5 :
    print("NORMAL")
elif kilo / boy * boy == 25 :
    print("NORMAL")
elif kilo / boy * boy >= 25 :
    print("FAZLA KİLOLU")
elif kilo / boy * boy == 30 :
    print("FAZLA KİLOLU")
elif kilo / boy * boy >= 30 :
    print("OBEZ")









#boy*boy\kilo