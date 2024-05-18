import numpy as np
import random as r


#zad 1

# a = np.array([4,5,6])
# b = np.array([1,2,3])
#print(a*b)

#zad 2
# a = np.array(([1,2,3,4],
#              [5,6,7,8],
#               [4,7,6,4],
#               [3,10,20,2]))
# b= np.array(([1,3,3],
#             [2,3,3],
#             [4,5,3]))
# print(a.min(axis=0))
# print(a.min(axis=1))
# print(b.min(axis=0))
# print(b.min(axis=1))

#zad 3

# a = np.array([4,5,6])
# b = np.array([1,2,3])
#print(a.dot(b)

#zad 4
#
# a = np.array([4.3,4.5,2.2], dtype=float)
# b=  np.array([6,3,2], dtype=int)
# print (a.dot(b))

# #zad 5
# b = np.array(([2,3],[3,4],[5,6]))
# for i in range(0,len(a)):
#     a = np.sin(a[i])
#     print(b)

# # zad 6
# a = np.array(([2,3],[3,4],[5,6]))
# for i in range(0,len(a)):
#     b = np.cos(a[i])
#     print(b)


# zad 7
#a = np.array([4.3,4.5,2.2], dtype=float)
# b=  np.array([6,3,2], dtype=int)
#print(a+b)

# zad 8
# b= np.array(([1,3,3],
#              [2,3,3],
#              [4,5,3]))
# for i in range(0, len(b)):
#     print(b[i])
#     print(" ")

# zad 9
# b= np.array(( [1,3,3],
#               [2,3,3],
#               [4,5,3] ))
# for i in range(0,len(b)*len(b)):
#     print(b.flat[i])

# #zad 10
# m = np.array(([np.arange(9),np.arange(9),np.arange(9),np.arange(9),np.arange(9),np.arange(9),np.arange(9),np.arange(9),np.arange(9),]))
# print(m)
# b=m.ravel()
# a = m.reshape(3,27)
# print(b)
# print(a)
#macierz można przekszalcić na każdą która ma tyle samo elementów co pierwotna
#zad 11

# m = np.array([np.arange(1,13)])
# print(m)
# print(" ")
# a = m.reshape(4,3)
# b = m.reshape(2,6)
# for i in range(0,len(m)**2):
#     print(a.flat[i])
#     print(b.flat[i])