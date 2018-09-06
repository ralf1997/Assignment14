#Q1

first = []
for i in range(int(input("Enter number of values in list\n"))):
    a = int(input("Enter value\t"))
    first.append(a)
firstCube = [ x**3 for x in first ]
print(firstCube)

#Q2

Pri = [ x for x in range(2,int(input("Enter number"))) if all(x%y!=0 for y in range(2,x)) ] 
print(Pri)

#Q3

'''A Generator Expression is doing basically the same thing as a List Comprehension does, but the GE does it lazily. The difference is quite similar to the difference between range and xrange.
A List Comprehension, just like the plain range function, executes immediately and returns a list.
A Generator Expression, just like xrange returns and object that can be iterated over.
The comparision is not perfect though, because in an object returned by the generator expression, we cannot access an element by index.
The difference between the two kinds of expressions is that the List comprehension is enclosed in square brackets [] while the Generator expression is enclosed in plain parentheses ().

The type of resulting values are list and generator respectively:

print(type(l))  # 'list'
print(type(g))  # 'generator' '''

#Lambda and Map

#Q1

Cel = [39.2, 36.5, 37.3, 37.8]
Fah = [ x*(9/5) + 32 for x in Cel ]
print(Fah)

#Q2

fGet = [1,2,3,4,5]
fSq = list(map(lambda x:x**2,fGet))
print(fSq)


#FILTER & REDUCE

#Q1
listp = [1,2,3,4,7,9,11,14,15,17,18,19,22,27]
def isPrime(x):
    c=0
    for i in range(2,x):
        if x%i==0:
            c=1
            break
    if c!=1:
        return True
    else:
        return False
pri = list(filter(isPrime,listp))
print(pri)

#Q2

from functools import *
fRed = [1,2,3,4]
li = reduce( lambda x,y:x*y,fRed )
print(li)
