#Explain your work
#Cihan İçelliler
#Öncelikle istenildiği gibi 1 ile 100 arasındaki asal sayılar bulunur. Sonrasında elde edilen 25 sayıdan rastgele 9 tanesi
#bir liste içerisine aktarılır ve son olarak matrix görüntüsü olacak şekilde yazdırılır.

#Question 1
#Cihan İçelliler
import random
#1-100 arası asal sayıları bul
primeNumbers=[]
for numbers in range(100):  
    if numbers > 1:  
        for i in range(2,numbers):  
            #Eğer sayı kendisinden küçük ve 2den büyük sayılara modu 0 oluyorsa asal olmadığını anla
            if (numbers % i) == 0:  
                break  
        #Eğer sayı kendisinden küçük ve 2den büyük sayılara modu 0 olmuyorsa asal olduğunu anla
        else:  
            primeNumbers.append(numbers) 

#25 tane asal sayıdan rastgele 9 tanesini seç
randomPrimeNumbers=[]
for i in range(9):
    randomNumber=primeNumbers[random.randint(0,24)]
    #Ekleme işlemini yap
    randomPrimeNumbers.append(randomNumber)

#Elde edilen 9 tane asal sayıyı matrix görüntüsü olacak şekilde yazdır
for matrix in range(0,9,3):
    print(randomPrimeNumbers[matrix],randomPrimeNumbers[matrix+1],randomPrimeNumbers[matrix+2])