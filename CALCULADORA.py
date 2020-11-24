resultado="si"
while resultado!="no":
print ("""************
Calculadora
************
Menu
1) Suma
2) Resta
3) Multiplicacion
4) Division
5) Salir""")
opcion=int(input("Ingrese su opcion a calcular: "))
if opcion == 5:
print("gracias por usar mi calculadora")
resultado="no"
else:
x=int(input("Ingrese el primer numero para calcular: "))
y=int(input("Ingrese el segundo numero para calcular: "))
if opcion==1:
print("la suma es ", x+y)
elif opcion==2:
print("la resta es ", x-y)
elif opcion==3:
print("la multiplicacion es ", x*y)
elif opcion==4:
print("la division es ",x/y)
elif opcion==5:
print("gracias por usar mi calculadora")
resultado=input("ingrese 'si' o 'no' para realizar un nuevo calculo: ")
