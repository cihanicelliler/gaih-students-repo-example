#Explain your work

#Question 1
def prime_first():
    for numbers in range(500):  
        if numbers > 1:  
            for i in range(2,numbers):  
                #Eğer sayı kendisinden küçük ve 2den büyük sayılara modu 0 oluyorsa asal olmadığını anla
                if (numbers % i) == 0:  
                    break  
            #Eğer sayı kendisinden küçük ve 2den büyük sayılara modu 0 olmuyorsa asal olduğunu anla
            else:  
                print(numbers)
def prime_second():
    for numbersSecond in range(500,1000):  
        if numbersSecond > 1:  
            for i in range(2,numbersSecond):  
                #Eğer sayı kendisinden küçük ve 2den büyük sayılara modu 0 oluyorsa asal olmadığını anla
                if (numbersSecond % i) == 0:  
                    break  
            #Eğer sayı kendisinden küçük ve 2den büyük sayılara modu 0 olmuyorsa asal olduğunu anla
            else:  
                print(numbersSecond)

prime_first()
prime_second()