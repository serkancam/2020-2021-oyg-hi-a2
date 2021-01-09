# import quick_sort bu modülü
# from modül import fonskiyon/sınıf
from quick_sort import quick_sort
from selection_sort import selecion_sort
from datetime import datetime
from random import randint



if __name__=='__main__':
    listem = [randint(1,1_000_000_000) for _ in range(2_000_000)]
    ssl = listem.copy()
    hsl = listem.copy()
    psl = listem.copy()
    # # selection sort hız testi
    # ssBaslangic=datetime.now()
    # sirali = selecion_sort(ssl)
    # ssBitis =datetime.now() 
    # print("Selction sort çalışma süresi:\t",ssBitis-ssBaslangic)

    #quick sort hız testi
    hsBaslangic = datetime.now()
    sirali = quick_sort(hsl)
    hsBitis = datetime.now()
    print("quick sort çalışma süresi:\t",hsBitis-hsBaslangic)

    #python built-in  sort hız testi
    psBaslangic = datetime.now()
    sirali = psl.sort()
    psBitis = datetime.now()
    print("python built-in  sort çalışma süresi:\t",psBitis-psBaslangic)








