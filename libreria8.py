import matplotlib.pyplot as plt
import numpy as np
import ipywidgets as widgets
from ipywidgets import interact

def plot_sucesion(sucesion):
    # Definir los valores de n
    n = np.arange(1, 101)  # n desde 1 hasta 100

    # Evaluar la sucesión
    try:
        a_n = eval(sucesion)
    except Exception as e:
        print(f"Error al evaluar la sucesión: {e}")
        return

    # Definir el límite L
    L = 0

    # Crear el slider para epsilon, evitando epsilon = 0
    epsilon_slider = widgets.FloatSlider(value=0.1, min=0.01, max=0.5, step=0.01, description=r'$\epsilon$')

    # Función interna para graficar con el valor de epsilon
    def actualizar_grafica(epsilon):
        # Crear la gráfica
        plt.figure(figsize=(10, 6))

        # Graficar la sucesión
        plt.scatter(n, a_n, marker='o', linestyle='-', color='b', label=f'$a_n = {sucesion}$')

        # Graficar las líneas para epsilon y -epsilon
        plt.axhline(y=epsilon, color='r', linestyle='--', label=r'$\epsilon$')
        plt.axhline(y=-epsilon, color='r', linestyle='--', label=r'$-\epsilon$')
        plt.axhline(y=L, color='g', linestyle='--', label=r'$L$')

        # Encontrar el valor de N tal que |a_n - L| < epsilon
        N_indices = np.where(np.abs(a_n - L) < epsilon)[0]
        if N_indices.size > 0:
            N = N_indices[0] + 1

            # Anotaciones
            plt.annotate(r'$\epsilon$', xy=(len(n) - 10, epsilon + 0.02), color='red')
            plt.annotate(r'$-\epsilon$', xy=(len(n) - 10, -epsilon - 0.05), color='red')
            plt.annotate(r'$L$', xy=(len(n) - 10, L + 0.02), color='green')
            plt.annotate(r'$N$', xy=(N, a_n[N - 1]), xytext=(N + 5, a_n[N - 1] + 0.1),
                         arrowprops=dict(facecolor='black', shrink=0.05))
        else:
            plt.text(50, epsilon + 0.1, '$\epsilon$ no puede ser 0', color='red')

        # Etiquetas y título
        plt.xlabel('n')
        plt.ylabel(r'$a_n$', rotation=0, labelpad=20)
        plt.title(f'Valores de la Sucesión $a_n = {sucesion}$ a medida que $n$ se incrementa')
        plt.grid(True)
        plt.legend()

        # Mostrar la gráfica
        plt.show()

    # Usar interact para actualizar la gráfica según el valor de epsilon
    interact(actualizar_grafica, epsilon=epsilon_slider)

    # Función para calcular la sucesión de Fibonacci
def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

# Función para graficar la sucesión de Fibonacci de tres formas diferentes
def graficar_fibonacci(n):
    fib_sequence = fibonacci(n)
    naturales = np.arange(n)

   
# naturales vs. sucesión
    plt.figure(figsize=(10, 6))
    plt.scatter(naturales, fib_sequence, color='b')
    plt.xlabel('n')
    plt.ylabel(r'$F_n$', rotation=0, labelpad=20)
    plt.title('Natural vs. Sucesión de Fibonacci')
    plt.grid(True)
    plt.show()

