salario = float(input("Ingresar salario: "))

#Salario_neto = salario - eps - pension

def pagoEps(salario):
    return salario * 0.04

eps = pagoEps(salario)

def pagoPension(salario):
    return salario * 0.04

pension = pagoPension(salario)

def pagoNomina(salario, eps, pension):
    salario_neto = salario - eps - pension
    print(salario_neto)

pagoNomina(salario, eps, pension)

# def pagoNomina2(salario):
#     eps = pagoEps(salario)
#     pension = pagoNomina(salario)
#     salario_neto = salario - eps - pension
#     print(salario_neto)

# pagoNomina2(salario, eps, pension)

# def pagoNomina3(salario):
#     eps = lambda salary: salario * 0.04
#     pension = lambda salary: salario * 0.04
#     salario_neto = salario - eps(salario) - pension(salario)
#     print(salario_neto)
# pagoNomina3(salario)

#ejemplo de callbacks, son funciones llamadas dentro de funciones
#que solo se ejecutan cuando se cumplen las instrucciones de la funcion
#que la esta llamando

#en el siguiente ejemplo se muestra una funcion llamada ejemploCallback que ejecuta un print
#luego la funcion pagoNomina3 tiene tres instrucciones para calcular el pago neto de un salario
#posterior a este calculo se llama la funcion ejemploCalback con parametro asignado de salario_neto
#que es el dato que ingresara a su instruccion para ser impreso
#si no se ejecutan las acciones de calculo de la funcion de pago de nomina, no se tendría el valor
#de salario neto, por ende no existiría dato para el parametro salario_neto de la función ejemploCallback
#y el print de dicha función no se ejecutaría.


def ejemploCallback(valor):
    print(f"El salario neto es: {valor}")

def pagoNomina3(salario, ejemploCallback):
    eps = lambda salary: salario * 0.04
    pension = lambda salary: salario * 0.04
    salario_neto = salario - eps(salario) - pension(salario)
    ejemploCallback(salario_neto)
    #return salario_neto

pagoNomina3(salario, ejemploCallback)
