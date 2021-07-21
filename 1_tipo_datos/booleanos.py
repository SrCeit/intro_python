print(10 > 9) #True
print(10 == 2) #False
print(10 < 9) #False

a, b = 100, 50
print(a)
print(b)

if b > a:
    print("b es mayor que a")
elif b < a:
    print("a es mayor que b")
else:
    print("a y b son iguales")

x = "Hola"
y = 15

#Devuelven True:
print(bool(x))
print(bool(y))
print(bool(["apple", "cherry", "banana"]))

#Devuelven False:
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))


def myFunction() :
    return True
print(myFunction()) #Devuelve True

if myFunction():
    print("YES!") #Si es True
else:
    print("NO!") #Si es False

#Es int?
x = 200
print(isinstance(x, int))