#Programa para calculadora


from __future__ import barry_as_FLUFL
from secrets import choice


def add(x,y):
    return x+y
def substract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
print("Seleccione una operación")
print("1 Suma")
print("2 Resta")
print("3 Multiplicación")
print("4 Dividir")
while True:
    choice=input("Ingrese selección 1 2 3 4")
    if choice in ('1','2','3','4'):
        num1=float(input("Ingrese primer número:"))
        num2=float(input("Ingrese segundo número"))
        if choice == '1':
            print(num1,"+",num2,"=",add(num1,num2))
        elif choice == '2':
            print (num1,"+",num2,"=",substract(num1,num2))
        elif choice == '3':
            print (num1,"+",num2,"=",multiply(num1,num2))
        elif choice == '4':
            print(num1,"+",num2,"=",divide(num1,num2))
    next_calculation = input("Quieres otro calculo (si/no)"):
    if next_calculation == "no":
        break
    else:
        print("Carácter inválido")