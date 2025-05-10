# Esta es la funcion para calular. 4 operaciones básicas.
def calculadora(valor1, valor2, Op):

 # Entradas para el usuario
    valor1=int(input("valor "))
    valor2=int(input("valor "))
    Op=input("operacion ")

# Objetos para las variables
    suma = valor1 + valor2 
    resta = valor1 - valor2
    divicion = valor1 / valor2
    multiplicacion = valor1 * valor2

# Condicionales
    if Op == "+":
        print (suma)
    elif Op == "-":
        print (resta)
    elif Op == "/":
        print (divicion)
    elif Op == "*":
        print (multiplicacion)
    elif Op != "+" "-" "/" "*":
        print ("Error de valor o operacion, intenta de nuevo")

# Mensaje de entrada y llamada de la aplicacion.
print("Bienvenido a la calculadora")
permiso=input("¿Desea iniciar la calculadora? ")
while permiso == "si":
    calculadora(0,0,"+")
else:
    print ("Adios")