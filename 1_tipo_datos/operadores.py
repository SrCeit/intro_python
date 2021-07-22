#Operadores y sus variantes

#Suma
x = 5
x += 3
print(x)

x = 5
x = x + 3
print(x)

#Resta
x = 5
x -= 3
print(x)

x = 5
x = x - 3
print(x)

#Multiplicación
x = 5
x *= 3
print(x)

x = 5
x = x * 3
print(x)

#Division
x = 5
x /= 3
print(x)

x = 5
x = x / 3
print(x)

#Modulo/resto de la división
x = 5
x %= 3
print(x)

x = 5
x = x % 3
print(x)

print("divmod(5,2) nos devuelve cociente y resto de la división en una tupla: ", divmod(5,2))


#Exponente
x = 5
x **= 3
print(x)

x = 5
x = x ** 3
print(x)

print("Otra dorma de calcular la potencia de 5^3 es con pow(5,3): ", pow(5,3))

#Floor division (devuelve siempre un entero)
x = 5
x //= 3
print(x)

x = 5
x = x // 3
print(x)

x = 10
y = 12

# Mayor: x > y is False
print('x > y is',x>y)

# Menor: x < y is True
print('x < y is',x<y)

# Igual: x == y is False
print('x == y is',x==y)

# Distinto de: x != y is True
print('x != y is',x!=y)

# Mayor o igual: x >= y is False
print('x >= y is',x>=y)

# Menor o igual: x <= y is True
print('x <= y is',x<=y)

#Lógica
x = True
y = False

print('x AND y is',x and y)

print('x OR y is',x or y)


print('NOT x is',not x)

a = 0b1111
b= 0b1011

print("1111 OR 1011 coloca un bit si existe en cualquiera de los operandos", bin(a|b))

print("1111 XOR 1011 coloca un bit si existe en uno de los operandos pero no en los dos", bin(a^b))

print("1111 AND 1011 colaca un 1 si en ambos operandos hay un 1", bin(a&b))

print("inversion de bits de 1011", bin(~b))

print("<<1011", bin(b<<2))

print(">>1011", bin(b>>2))



#Valor absoluto
print(abs(-5))

#Aproximar
print("El numero 1,2367 a dos decimales :", round(1.2367, 2))


