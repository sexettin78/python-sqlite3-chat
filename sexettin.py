import sqlite3
db = sqlite3.connect("veri1.db")
cr = db.cursor()
cr.execute("CREATE TABLE IF NOT EXISTS sohbet ('isim', 'mesaj')")
cr.execute("SELECT isim, mesaj FROM sohbet")
db.commit()
isimm = "sexettin"

secim = input("1-Mesaj yaz 2-mesajları oku")
if secim=="1":
    mesajj = str(input("Mesaj>"))
    parametre = (isimm,mesajj)
    cr.execute("INSERT INTO sohbet (isim, mesaj) VALUES (?, ?)", parametre)
    db.commit()

if secim=="2":
    cekilen_veri = cr.fetchall()
    for veri in cekilen_veri:
        print(veri[0]+": "+veri[1])