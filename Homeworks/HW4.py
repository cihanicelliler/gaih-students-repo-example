#Cihan İçelliler

class Oyun():
    def __init__(self,kelime):
        self.kelime=kelime
        
    def tahmin(self,kelime):
        harfsayısı=len(kelime)
        for i in range(harfsayısı):
            print("_",end=" ")

        
        self.kontrol(kelime)
    
    def kontrol(self,kelime):
        kelime = kelime.upper()
        hak=0
        harfler=[]
        kelimeHarfListe=[]
        for kelimeHarfleri in kelime:
            kelimeHarfListe.append(kelimeHarfleri)
        while hak!=5:
            harflerSayisi=len(harfler)
            kelimeHarfListeSayisi=len(kelimeHarfListe)
            kalanHarfSayisi=kelimeHarfListeSayisi-harflerSayisi
            if(kalanHarfSayisi==0):
                break
            else:
                harf=input("\nHarf Tahmin Ediniz.\n")  
                harf=harf.upper()
                if len(harf)>1 or len(harf)<0:
                    print("Harf Giriniz!")
                    continue   
                else:
                    if harf not in kelime :
                        hak+=1
                        print(f"Yanlis Tahmin! {5-hak} hakkınız kaldı.")
                    else:

                        print("Doğru Tahmin!")
                        harfler.append(harf)
                        print("Bulunan Harfler")
                        for harfbul in harfler:
                            if harfbul in kelimeHarfListe:
                                print(f"{harfbul}",end=" ")
                        print(f"Kalan harf sayısı {kalanHarfSayisi-1}")   
                
        if hak==5:
            print("Hakkınız Doldu. Oyun Bitti")
        else:
            print("Tebrikler Kazandınız!")

print("Arkadaşınızın Bilmesi İçin Bir Kelime Giriniz.")
kelime=input()
oyun=Oyun(kelime)
oyun.tahmin(kelime)