#Explain your work
#Öğrencilerin isimleri ve soyisimlerini input ile alarak sonrasında notlarını alarak listeye aktarılma işlemi yapıldı.Daha
#sonra isimler ve soyisimler birbirinden ayrılarak info dict e eklendi. Ortalamalar alındı ve en büyük ortalama bulundu.En büyük 
# ortalamanın indexi bulunarak en büyük ortalamayı alan öğrenci ekrana yazdırıldı.
#Question 1
#Cihan İçelliler
#Info adlı bir dict oluştur
info={
    'name':[],
    'lastname':[],
    'homework':[],
    'vize':[],
    'final':[]
}
#Ad ve soyadları tutan bir liste oluştur
nameAndSurnameList=[]
#Notları tutan bir liste oluştur
Grades=[]
for i in range(5):
    #Ad ve soyadı al aralarında boşluk olacak şekilde
    nameAndSurname=input("Öğrencinin adını ve soyadını giriniz: ")
    #Ödev notunu gir
    homework=int(input("Ödevini giriniz(0-100): "))
    #Vize notunu gir
    vize=int(input("Vizesini giriniz(0-100): "))
    #Final notunu gir
    final=int(input("Finalini giriniz(0-100): "))
    #Notları Kontrol et
    if homework<0 or homework>100 or vize<0 or vize>100 or final<0 or final>100:
        print("Hatalı not girdiniz!")
        break
    #Listeye ödev notunu ekle
    Grades.append(homework)
    #Listeye vize notunu ekle
    Grades.append(vize)
    #Listeye final notunu ekle
    Grades.append(final)
    #Dict e ödev notunu ekle
    info['homework'].append(homework)
    #Dict e vize notunu ekle
    info['vize'].append(vize)
    #Dict e final notunu ekle
    info['final'].append(final)
    #Listeye ad ve soyadı ekle
    nameAndSurnameList.append(nameAndSurname)

#Ad ve soyad listesini dolaş
for name in nameAndSurnameList:
    #Ad ve soyadı birbirinden ayır
    FullName=name.split()
    #Dict e adı ekle
    info['name'].append(FullName[0])
    #Dict e soyadı ekle
    info['lastname'].append(FullName[1])

#Ortalamalar için liste oluştur
ortalamalar=[]
#Ortalamaları hesapla
for i in range(5):
    toplam=int(info['homework'][i])+int(info['vize'][i])+int(info['final'][i])
    ort=toplam/3
    ortalamalar.append(ort)

#En büyük ortalamayı bul
maxOrt=max(ortalamalar);
#En büyük ortalamanın indexini bul
indexMax=ortalamalar.index(maxOrt)
#En büyük ortalamalı öğrenciyi yazdır
print(f"{info['name'][indexMax]} {info['lastname'][indexMax]} adlı öğrenci {maxOrt} ortalama ile en yüksek ortalamaya sahiptir.")

#Info Dict ini yazdır
print(info)