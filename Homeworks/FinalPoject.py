#Cihan İçelliler
class Recipe:
    #Ortak Fonksiyonlar
    def __init__(self,yemekAdi,urunler):
        self.yemekAdi=yemekAdi
        self.urunler=urunler
    def preparation(self,urunler):
        print(f"{urunler} i hazırlayınız")
    def cooking(self,yemekAdi):
        print(f"Kısık ateşte {yemekAdi} 'i 10-15 dakika bekletin")
    def boiled(self,yemekAdi):
        print(f"10-15 dakika {yemekAdi} 'i haşlayın")
    def sauce(self,yemekAdi):
        print(f"{yemekAdi} için sosu hazırlayın")
    def salting(self,yemekAdi):
        print(f"Tuzlama işlemini yapınız")
#Kalıtım
class Pilav(Recipe):
    def __init__(self,yemekAdi,urunler):
        Recipe.__init__(self,yemekAdi,urunler)
    #Yemeğe özel fonksiyonlar
    def Dinlendirme(self,yemekAdi):
        print(f"{yemekAdi} 10 dakika havlu ile üzerini kapatıp dinlendirin.")
#Kalıtım
class Makarna(Recipe):
    def __init__(self,yemekAdi,urunler):
        Recipe.__init__(self,yemekAdi,urunler)
    #Yemeğe özel fonksiyonlar
    def Yogurtlama(self,yemekAdi):
        print(f"{yemekAdi} sarımsakli yogurt dökünüz.")
#Kalıtım
class Et(Recipe):
    def __init__(self,yemekAdi,urunler):
        Recipe.__init__(self,yemekAdi,urunler)
    #Yemeğe özel fonksiyonlar
    def Kekikleme(self,yemekAdi):
        print(f"{yemekAdi} kekik dökünüz")
    def Izgara(self,yemekAdi):
        print(f"{yemekAdi} izgaraya koyup 20 dakika pişirin")
    

print("**********Pilav Tarifi**********")
yemekTarifiPilav=Pilav("pilav",["pilav,tuz,su"])
yemekTarifiPilav.preparation(["pilav,tuz,su"])
yemekTarifiPilav.salting("pilav")
yemekTarifiPilav.boiled("pilav")
yemekTarifiPilav.cooking("pilav")
yemekTarifiPilav.Dinlendirme("pilav")
print("\n\n\n")

print("**********Makarna Tarifi**********")
yemekTarifiMakarna=Makarna("Makarna",["Makarna,tuz,su,ketçap,yogurt"])
yemekTarifiMakarna.preparation(["Makarna,tuz,su,ketçap,yogurt"])
yemekTarifiMakarna.cooking("Makarna")
yemekTarifiMakarna.sauce("Makarna")
yemekTarifiMakarna.Yogurtlama("Makarna")
print("\n\n\n")


print("**********Et Tarifi**********")
yemekTarifiEt=Et("Makarna",["Et,tuz,su,kekik"])
yemekTarifiEt.preparation(["Et,tuz,su,kekik"])
yemekTarifiEt.Kekikleme("Et")
yemekTarifiEt.cooking("Et")
yemekTarifiEt.sauce("Et")
yemekTarifiEt.Izgara("Et")

