
import math
import random
def zad1():

    rownanie1 = ((math.e**4)-math.log(34,2))**(1/3)
    print(round(rownanie1,2))
    rownanie2=(math.log(20,math.e)+math.cos(45)+math.e)**(1/3)
    print(round(rownanie2,2))
    rownanie3=(math.log(20,3)+math.sin(45)*(5/8))**(1/4)
    print(round(rownanie3,2))
    rownanie4=math.log(23,3)+((math.sin(34)+5)**(1/4))
    print(round(rownanie4,2))
    rownanie5=(math.log(32,2)+math.pi+math.sin(56))**(1/4)
    print(round(rownanie5,2))
def zad2():
    a = "A"
    szerokosc = 1
    wysokosc = int(input("Podaj wysokosc wiezy "))
    if wysokosc > 10:
        print("Nie wolno!")
        return 0
    for i in range(1,wysokosc+1):
        print(a*szerokosc)
        szerokosc +=1

def zad3():
    a = " "

    szerokosc = 1

    wysokosc = int(input("Podaj wysokosc wiezy "))
    if wysokosc > 10:
        print("Nie wolno!")
    else:
        licznik = wysokosc
        for i in range(1,wysokosc+1):
            print((a*licznik),"a" * szerokosc )
            szerokosc += 2
            licznik -=1
def zad5():
    wektor2d =[]
    n=int(input('Podaj wymiar wektora nxn: '))
    pomocniczy_wektor= []
    for i in range(1,n+1):
        pomocniczy_wektor.clear()
        pomocniczy_wektor.append(random.randint(0, 100))
        wektor2d.append(pomocniczy_wektor)


    print(wektor2d)



def main():
    #zad1()
    #zad2()
    #zad3()
    #zad5()
if __name__ == '__main__':
    main()