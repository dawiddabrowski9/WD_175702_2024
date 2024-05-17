import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ts = pd.Series(np.random.randn(1000))
# data = {'Kraj' : ['Belgia','Indie','Brazylia','Polska'],
#         'Stolica': ['Bruksela','New Delhi','Brasilia','Warszawa'],
#         'Kontynent': ['Europa','Azja','Ameryka Południowa','Europa'],
#         'Populacja': [11190846,1303171035,207847528,38675467]}
# df = pd.DataFrame(data)
# print(df)
#
# grupa = df.groupby(['Kontynent']).agg({'Populacja':['sum']})
# print(grupa)
#
# grupa.plot(rot=0,kind='bar',xlabel='Kontynent',ylabel='Mld',legend=True,title='Populacja z podziałem na kontynenty')
# plt.show()
# df = pd.read_csv('dane.csv',header=0,sep=';',decimal=',')
#print(df)
# grupa = ((df.groupby(['Imię i nazwisko'])).
#          agg({'Wartość zamówienia':["sum"]}))
# grupa.plot(kind='pie', subplots=True, autopct='%.2f %%',
#            fontsize=20, figsize=(6, 6), colors=['red','green'])
# plt.legend(loc='lower right')
# plt.title('Suma zamówienia dla sprzedawcy')
# plt.show()
# ts = pd.Series(np.random.randn(1000))
# ts = ts.cumsum()
#
# df = pd.DataFrame(ts,columns=['Wartości'])
# print(df)
#
# df['Średnia krocząca'] = df.rolling(window=50).mean()
# df.plot()
# plt.legend()
# plt.show()

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx,header=0)
#Zad1

# print(df)
# grupa = df.groupby(['Rok']).agg({'Liczba':['sum']})
# grupa.plot(rot=0 ,xlabel='Lata', ylabel='Liczba urodzeń', legend=True,title='Liczba urodzeń w latach ')
# plt.show()

#Zad2

# grupa = df.groupby(['Plec']).agg({'Liczba':['sum']})
# grupa.plot(kind='bar',ylabel='Mln',fontsize="15")
# plt.legend()
# plt.show()

#Zad3
#grupa = df.groupby(['Rok']).agg({'Liczba':['sum']})

#Zad1/2
# x = np.arange(0,20)
# y = 1/x
# plt.ylabel("f(x)")
# plt.xlabel('x')
# plt.legend()
# plt.xlim(0,20)
# plt.ylim(0,1)
# plt.title('Wykres funkcji f(x) dla x[1,20]')
# plt.plot(y,linestyle='dotted',color='green',label='f(x)=1/x')
# plt.plot(y,'g>')
#
# plt.show()
#

#zad3

#x = np.arange(0,30,0.1)
#y1= np.sin(x)
#y2=np.cos(x)
#plt.ylabel('y')
#plt.xlabel('x')
#plt.plot(y1,label='sin(x)')
#plt.plot(y2,label='cos(x)')
#plt.legend()
#plt.show()

# #zad4
# csv = pd.read_csv('iris.data',names=['sepal_lenght','sepal_width','niepotrzebne','niepotrzebne1'])
# data_a = csv['sepal_lenght']
# data_b = csv['sepal_width']
# skala = np.abs(data_a-data_b)
# plt.scatter(data_a,data_b,s =skala, c=data_a, cmap ='magma')
# plt.show()


#zad5
grupa1 = df.groupby(['Plec']).agg({'Liczba':['sum']})
grupa = df.groupby(['Rok']).agg({'Liczba':['sum']})
grupa3 = df.groupby(['Rok']).agg({'Liczba':['sum']})
plt.subplot(122)
plt.plot(grupa)
plt.subplot(121)
plt.plot(grupa1)
plt.subplot(313)
plt.plot(grupa3)
plt.show()