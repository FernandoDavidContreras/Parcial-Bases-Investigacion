class Nodo:
    def __init__(self, coeficiente, grado):
        self.coeficiente = coeficiente
        self.grado = grado
        self.siguiente = None

class Polinomio:
    def __init__(self):
        self.cabeza = None

    def agregar_termino(self, coeficiente, grado):
        nuevo_termino = Nodo(coeficiente, grado)
        nuevo_termino.siguiente = self.cabeza
        self.cabeza = nuevo_termino

    def mostrar_polinomio(self):
        actual = self.cabeza
        while actual:
            print(f"{actual.coeficiente}x^{actual.grado}", end=" ")
            if actual.siguiente:
                print("+", end=" ")
            actual = actual.siguiente
        print()

def sumar_resta_polinomios(polinomio_a, polinomio_b, operacion):
    resultado = Polinomio()
    actual_a, actual_b = polinomio_a.cabeza, polinomio_b.cabeza

    while actual_a or actual_b:
      #verificamos el valor de la operacion si existe si no la operacion la dejaremos en 0 osea que no existe un exponente con el mismo grado de elevacion
        coeficiente_a = actual_a.coeficiente if actual_a else 0
        coeficiente_b = actual_b.coeficiente if actual_b else 0

        if operacion == 'suma':
            coeficiente_resultado = coeficiente_a + coeficiente_b
        elif operacion == 'resta':
            coeficiente_resultado = coeficiente_a - coeficiente_b

        #aqui evaluaremos si el termino a existe lo utilizaremos como mayor para meterlo en el grado si no pasa al actual b
        resultado.agregar_termino(coeficiente_resultado, actual_a.grado if actual_a else actual_b.grado)

        if actual_a:
            actual_a = actual_a.siguiente
        if actual_b:
            actual_b = actual_b.siguiente

    return resultado

def evaluar_polinomio(polinomio, valor):
    resultado = 0
    actual = polinomio.cabeza

    while actual:
        resultado += actual.coeficiente * (valor ** actual.grado)
        actual = actual.siguiente

    return resultado

polinomio_a = Polinomio()
polinomio_b = Polinomio()

cantidadTerminos = input('Ingrese la cantidad de terminos para su funcion A:\n')
for a in range(int(cantidadTerminos)):
  termino = int(input('Ingrese el termino:\n'))
  grado = int(input('Ingrese el grado de elevacion de su exponente de 0 a cualquier numero real positivo(ingresar 0 si es un numero normal ejemplo:\n45x^0 = 45, 45x^1 = 45x):\n'))
  polinomio_a.agregar_termino(termino, grado)


cantidadTerminos = input('Ingrese la cantidad de terminos para su funcion B:\n')
for a in range(int(cantidadTerminos)):
  termino = int(input('Ingrese el termino:\n'))
  grado = int(input('Ingrese el grado de elevacion de su exponente de 0 a cualquier numero real positivo(ingresar 0 si es un numero normal ejemplo:\n45x^0 = 45, 45x^1 = 45x):\n'))
  polinomio_b.agregar_termino(termino, grado)


print('---------------')
print("| Polinomio A |")
print('---------------')
polinomio_a.mostrar_polinomio()

print('---------------')
print("| Polinomio B |")
print('---------------')
polinomio_b.mostrar_polinomio()

resultado_suma = sumar_resta_polinomios(polinomio_a, polinomio_b, 'suma')
print('______________________')
print("| Suma de polinomios |")
print('______________________')
resultado_suma.mostrar_polinomio()

resultado_resta = sumar_resta_polinomios(polinomio_a, polinomio_b, 'resta')
print('_______________________')
print("| Resta de polinomios |")
print('_______________________')

resultado_resta.mostrar_polinomio()


valor_evaluacion = int(input('Ingrese el valor a evaluar en la función:\n'))
ecuacion = input('Ingrese la ecuacion a utilizar a/b:\n')

if ecuacion == 'a':
  resultado_evaluacion = evaluar_polinomio(polinomio_a, valor_evaluacion)
  print('---------------------------------------')
  print(f"| Evaluación de polinomio A para x={valor_evaluacion} |")
  print('---------------------------------------')
  print(f'El resultado es: {resultado_evaluacion}')
elif ecuacion == 'b':
  resultado_evaluacion = evaluar_polinomio(polinomio_b, valor_evaluacion)
  print('---------------------------------------')
  print(f"| Evaluación de polinomio B para x={valor_evaluacion} |")
  print('---------------------------------------')
  print(f'El resultado es: {resultado_evaluacion}')
