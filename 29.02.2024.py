import random
from turtle import *
def zad1():
    wynik = 0
    liczba = random.randint(0, 5)
    for i in range(0,5):
        wybor = (int(input('Zgadnij liczbę!: ')))
        if wybor == liczba:
            print("Wygrałeś! Zdobywasz 1 punkt.")
            wynik = wynik + 10
        else:
            print("Spróbuj jeszcze raz!")

    print("Twój wynik to:",wynik )

def zad2():
    speed(1000)
    pencolor("green")
    for i in range(0,10):
        forward(100)
        left(36)
    left(60)
    for i in range(0,10):
        forward(100)
        left(36)
    left(60)
    for i in range(0, 10):
        forward(100)
        left(36)
    left(60)
    for i in range(0, 10):
        forward(100)
        left(36)
    left(60)
    for i in range(0, 10):
        forward(100)
        left(36)
    left(60)
    for i in range(0, 10):
        forward(100)
        left(36)
    pencolor('red')
    forward (100)
    left(60)
    forward(100)
    left(120)
    forward(100)
    right(60)
    forward(100)
    left(120)
    forward(100)
    right(60)
    forward(100)
    left(120)
    forward(100)
    right(60)
    forward(100)
    left(120)
    forward(100)
    right(60)
    forward(100)
    left(120)
    forward(100)
    right(60)
    forward(100)
    left(120)
    forward(100)
    right(60)
    forward(100)
    left(60)
    forward(100)
    for i in range(0,6):
        left(60)
        forward(200)

    exitonclick()

def zad3():
    iloscgier = 10000
    drzwi=[1,2,3]
    wygrane = 0
    for i in range(iloscgier):
        nagroda = random.choice(drzwi)
        pierwszywybor = random.choice(drzwi)
        prowadzacymozeotworzyc = set(drzwi) - set([pierwszywybor,nagroda])
        prowadzacyotwiera = random.choice(list(prowadzacymozeotworzyc))
        drugiwybor = min(set(drzwi) - set([pierwszywybor,prowadzacyotwiera]))
        if drugiwybor == nagroda:
            wygrane = wygrane +1
    print((wygrane / iloscgier)*100 , "%")


def main():
    #zad1()
    #zad2()
    #zad3()

if __name__ == '__main__':
    main()