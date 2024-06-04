import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# # zad 1
# x = np.arange(0,11)
# y = (x**2+4)/(2**x)
# plt.plot(y,x,label = 'x^2+4/(2**x)')
# plt.ylabel('y')
# plt.xlabel('x')
# plt.title('Wykres funkcji f(x)')
# plt.legend()
# plt.show()

# zad 2
# fig, axs = plt.subplots(1,3)
# x2 = np.arange(-3,4,dtype=float)
# x1 = np.arange(-3,4,dtype=float)
# y1 = (x1**2)+5
# y2 = -(x2**2)+4*x2
# axs[1].axis('off')
# axs[0].set_title('Wykres funkcji f(x)=x^2+5')
# axs[2].set_title('Wykres dwóch funkcji')
# axs[0].set_xlabel('x')
# axs[2].set_xlabel('x')
# axs[0].set_ylabel('Wartość funkcji')
# axs[2].set_ylabel('Wartość funkcji')
# axs[0].plot(x1,y1,label='x^2+5')
# axs[2].plot(x1,y1,color='red',linestyle='dotted',linewidth=2,label='x^2+5')
# axs[2].plot(x2,y2,color='green',linestyle='dotted',linewidth=2,label='-x^2+4x')
# axs[0].legend()
# axs[2].legend()
# plt.show()
#
# #zad 3
# csv = pd.read_csv('automobile.csv',header=0,sep=';')
# df = pd.DataFrame(csv)
# los = df.sample(n=100)
# plt.title('Ilość samochodów danej marki')
# grupa = los.groupby(los['Car model']).size()
# grupa.plot(kind='pie',autopct='%1.2f',fontsize='14')
# plt.show()

# # zad 4
# plt.title("Średnie ceny samochodów danej marki")
# grupa = df.groupby('Car model')['Price'].mean()
# grupa.plot(kind='bar')
# plt.show()
#
#zad 1b
# x = np.arange(-5,6)
# y = -(x**2)-4*x
# plt.xticks((-5,-3,-1,1,3,5))
# plt.title('Wykres funkcji f(x)')
# plt.ylabel('f(x)')
# plt.xlabel('x')
# plt.plot(x,y,label='-x^2-4x')
# plt.legend()
# plt.show()

#zad 2b
# fig,axs =plt.subplots(3,1)
# x1 = np.arange(4,10)
# y1 = x1**(1/2)
# axs[0].set_xticks((4,5,6,7,8,9))
# axs[0].set_title('Wykres słupkowy funkcji')
# axs[0].set_xlabel('x')
# axs[0].set_ylabel('wyniki funkcji')
# axs[0].set_yticks((0,1,2,3))
# axs[0].bar(x1,y1,label='f(x)=sqrt(x)')
# axs[0].legend()
# axs[1].axis('off')
# x2=np.linspace(0,11)
# y2=np.cos(x2)+0.4
# axs[2].set_title('Wykres cos(x)+0.4')
# axs[2].set_xlabel('x')
# axs[2].set_ylabel('cos(x)+0.4')
# axs[2].plot(x2,y2,linestyle='None',marker='o',color='green',label='cos(x)+0.4')
# plt.legend()
# plt.show()

#zad 3b

# df = pd.read_csv('cars.csv',header=0,sep=';')
# ramka = df.sample(n=100)
# grupa = ramka.groupby('Cylinders').size()
# plt.title('Procentowa wartość cylindrów w samochodach')
# plt.pie(grupa,labels=grupa.index,autopct='%1.1f',textprops={'fontsize':14})
# plt.legend()
# plt.show()
#
# #zad 4b
# df = pd.read_csv('iris.data',header=None, sep=',')
# x =df[2]
# y= df[3]
# grupa = df.groupby(4)
#
# plt.scatter(x=x,y=y)
# plt.show()
