import random

def dizininEnkucugunuBul(dizim):
    enKucukDeger=dizim[0]
    enkucukYeri=0
    for i in range(1,len(dizim)):
        if dizim[i]<enKucukDeger:
            enKucukDeger = dizim[i]
            enkucukYeri=i
    return enkucukYeri

def selecion_sort(dizim):
    siraliDizi=[]#geri döndürülecek sıralı dizi
    for i in range(len(dizim)):
        enKucukIndisi = dizininEnkucugunuBul(dizim)
        siraliDizi.append(dizim.pop(enKucukIndisi))
    return siraliDizi
# yerinde sıralama yapmayacak yani bize verilen dizinin 
# sıralanmış halde yeni bir dizi olarak verecek
if __name__=="__main__":
    sd = [random.randint(1,1000) for i in range(20)]
    print(sd,"ceeee")

    sirali=selecion_sort(sd)
    del sd
    print(sirali)