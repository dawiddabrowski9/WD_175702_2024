import sys

def zad1():
    lista = []
    counter = 0
    zdanie = input("Wpisz zdanie: ")
    lista = zdanie.split()
    for i in range(0,len(lista)):
        counter += 1
    print(counter)

def zad2():
    sys.stdout.write('Wczytaj 1 liczbe: ')
    a = int(sys.stdin.readline())
    sys.stdout.write('Wczytaj 2 liczbe: ')
    b = int(sys.stdin.readline())
    sys.stdout.write('Wczytaj 3 liczbe: ')
    c = int(sys.stdin.readline())
    wynik = a**b+c
    print(wynik)
def zad3():
    napis = input("Podaj slowo: ")
    if napis == napis[::-1]:
        print("Napis jest palindromem")
    else:
        print("napis nie jest palindromem")
def zad4():
    counter = 0
    liczba = int(input("Podaj liczbę: "))
    for i in range(1, liczba+1):
        if liczba%i==0:
            counter+=1
    if counter == 2:
        print("liczba jest pierwsza")
    else:
        print("liczba nie jest pierwsza")
def zad5():
    counter = 0
    suma= 0



def zad6():
    lista=[1,2,3.5,5,6.5,7,8.2,9,10,3]
    lista1=[]
    for i in range(0,len(lista)):
        wynik=lista[i]*lista[i]
        lista1.append(wynik)
    print(lista1)
def zad7():
    counter=0
    lista = []
    while counter != 10:
        liczba = int(input("Podaj liczbę: "))
        counter += 1
        if liczba % 2 == 0:
            lista.append(liczba)
    print(lista)
def zad8():
    lista =['banan',1,4,5,'drzewo',6,6,'drzewo']
    slownik = {}
    for i in range(0,len(lista)):
        slownik[i] = lista[i]
        if
    print(slownik)

def main():
    #zad1()
    #zad2()
    #zad3()
    #zad4()
    #zad5()
    #zad6()
   # zad7()
    zad8()
if __name__ == '__main__':
    main()