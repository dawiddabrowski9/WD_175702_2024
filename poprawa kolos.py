import math
import random as r
def zad1():
    suma = 0
    for i in range(14,33):
        suma = suma + (((i**math.e) + (math.cos(i)))**(1/5))
    print(round(suma,2))

def zad2(min,max,ile):
    if max > min and ile > 0:
        lista = []
        for i in range(0,ile+1):
            lista.append(r.randint(min,max))
        print(lista)
        for i in range(0,ile+1):
            if lista[i]>0:
                lista[i] = -lista[i]
            else:
                lista[i] = -lista[i]
    else:
        print("Błąd parametrów")
def zad3(nazwa_pliku):
    try:
        f = open(nazwa_pliku,'r')
        lista = list(f.readlines())
        print(lista)
        for i in range(0,len(lista)):

    except FileNotFoundError:
        print("Plik nie istnieje!")






def zad4(a,b,c):
    if a and b and c > 0:
        if (a*a)+(b*b) == (c*c):
            return (a*b)/2
    else:
        print("Błąd parametrów")
def main():
    zad3("liczby.txt")


if __name__ == "__main__":
    main()