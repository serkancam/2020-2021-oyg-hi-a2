import random
def quick_sort(dizim):
    if len(dizim) < 2:
        return dizim
    else:
        pivot = dizim[0]#diznin ilk eleman değeri pivot olsun
        sol = [i for i in dizim[1:] if i <= pivot] # pivottan küçük veya olanslar sola
        sag = [i for i in dizim[1:] if i > pivot] # pivottan bütük olanlar sağa

        return quick_sort(sol) + [pivot] +quick_sort(sag)
    

if __name__=='__main__':
    sd = [random.randint(1,1000) for i in range(20)]

    print("sırasız:\n",sd)
    sirali=quick_sort(sd)
    print("sıralı:\n",sirali)



# listelerde + operatörü kullanımı
# a = [3,5,8]

# b= [17,25,9]

# c= a+[333]+b

# print(c)
