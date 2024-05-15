#import random
#def bezpowtorzen(start,stop):
#    lista=[]
#    while len(lista) < liczba:
#        liczba1 = random.randint(1,100)
#        if liczba1 not in lista and liczba1%2 == 0:
#            lista.append(liczba1)
 #   return lista
#print ("ile liczb")
#liczba = int(input())
#print ()

#def sumaparzystych(lista):
#    suma = 0
#    for i in lista:
#        if i%2 ==0:
#            suma += i
#    return suma
#lista = [1,2,3,4,5,6,7,8]
#wynik = sumaparzystych(lista)
#print (wynik)       

#def srednia(lista):
#    suma = 0
#    for i in lista:
#        suma += i
#    srednia1 = suma/len(lista)
#    return srednia1
#lista = [1,2,3,4,5]
#wynik = srednia(lista)
#print (wynik)

#def usun(lista):
#    lista1 = []
#    for i in lista:
#        if i not in lista1:
#            lista1.append(i)
#    return lista1
#lista = [1,2,2,2,3,5,3]
#wynik = usun(lista)
#print (wynik)

#def najczestszyelement(lista):
#    liczba = 0
#    slowo = ""
#    for i in lista:
#        if lista.count(i) > liczba:
#            liczba = lista.count(i)
#            slowo = i 
#    return slowo
#lista = [1,2,3,3,3,4,4]
#wynik = najczestszyelement(lista)
#print (wynik)

def cyfrynakwa(liczba):
    liczba2 = ""
    for i in range (len(liczba)):
        lol = liczba[i-1]**2
        liczba2 += lol
    return liczba2
liczba = "123"
wynik = cyfrynakwa(liczba)
print (wynik)   