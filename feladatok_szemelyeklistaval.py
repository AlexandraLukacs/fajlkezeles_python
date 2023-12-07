""" Készíts metódust, amely kiszámolja a személyek átlagéletkorát """

def atlageletkor(lista):
    osszeg:int=0
    for i in range(0, len(lista), 1):
        osszeg += lista[i].kor

    return osszeg/len(lista)

""" Készíts metódust, mely megmondja a listában lévő nők számát """

def nokszama(lista):
    db:int=0
    for i in range(0, len(lista), 1):
        if lista[i].nem == "nő":
            db += 1
    
    return db