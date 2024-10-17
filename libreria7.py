import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display, clear_output

 

import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, FloatSlider
import ipywidgets as widgets

# Definir la función seno con desfase y la función seno original
def plot_sine(desfase=0):
    x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
    
    # Función seno con desfase
    y_desfase = np.sin(x + desfase)
    
    # Función seno original (sin desfase)
    y_original = np.sin(x)
    
    plt.figure(figsize=(8, 4))
    
    # Graficar seno original en gris
    plt.plot(x, y_original, label=r'$y = \sin(x)$', color='gray', linestyle='--', linewidth=2)
    
    # Graficar seno con desfase
    plt.plot(x, y_desfase, label=fr'$y = \sin(x + {desfase:.2f})$', color='b', linewidth=2)
    
    plt.axhline(0, color='black',linewidth=1)
    plt.axvline(0, color='black',linewidth=1)
    
    plt.title('Simulación de la Función Seno con Desfase', fontsize=14)
    plt.xlabel('x', fontsize=12)
    plt.ylabel('y', fontsize=12)
    
    plt.xlim(-2 * np.pi, 2 * np.pi)
    plt.ylim(-1.5, 1.5)
    
    plt.xticks([-2 * np.pi, -np.pi, 0, np.pi, 2 * np.pi], 
               [r'$-2\pi$', r'$-\pi$', '0', r'$\pi$', r'$2\pi$'])
    
    plt.grid(True)
    plt.legend()
    plt.show()


import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact

# Función para graficar la onda seno con amplitud, frecuencia, desfase y término constante
def graficar_seno(amplitud, frecuencia, desfase, constante):
    # Definir el rango de los valores de x
    x = np.linspace(-3*np.pi, 3 * np.pi, 1000)  # De 0 a 4π para ver varios ciclos

    # Calcular los valores de y usando la función seno
    y = amplitud * np.sin(frecuencia * x + desfase) + constante

    # Limpiar la figura
    plt.figure(figsize=(10, 5))
    plt.plot(x, y, label=f"$y = {amplitud} \\cdot \\sin({frecuencia}x + {desfase}) + {constante}$", color='blue')
    plt.title(f"Onda Senoidal: Amplitud = {amplitud}, Frecuencia = {frecuencia}, Desfase = {desfase}, Constante = {constante}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.ylim(-3*np.pi,3*np.pi)
    plt.xticks([-3 * np.pi,-2 * np.pi, -np.pi, 0, np.pi, 2 * np.pi,3 * np.pi], 
               [r'$-3\pi$',r'$-2\pi$', r'$-\pi$', '0', r'$\pi$', r'$2\pi$',r'$3\pi$'])
    plt.grid(True)
    plt.legend(loc="upper right")
    plt.show()

# Función para graficar la onda coseno con amplitud, frecuencia, desfase y término constante
def graficar_coseno(amplitud, frecuencia, desfase, constante):
    # Definir el rango de los valores de x
    x = np.linspace(-3*np.pi, 3 * np.pi, 1000)  # De 0 a 4π para ver varios ciclos

    # Calcular los valores de y usando la función coseno
    y = amplitud * np.cos(frecuencia * x + desfase) + constante

    # Limpiar la figura
    plt.figure(figsize=(10, 5))
    plt.plot(x, y, label=f"$y = {amplitud} \\cdot \\cos({frecuencia}x + {desfase}) + {constante}$", color='green')
    plt.title(f"Onda Cosenoidal: Amplitud = {amplitud}, Frecuencia = {frecuencia}, Desfase = {desfase}, Constante = {constante}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.ylim(-3*np.pi,3*np.pi)
    plt.xticks([-3 * np.pi,-2 * np.pi, -np.pi, 0, np.pi, 2 * np.pi,3 * np.pi], 
               [r'$-3\pi$',r'$-2\pi$', r'$-\pi$', '0', r'$\pi$', r'$2\pi$',r'$3\pi$'])
    plt.grid(True)
    plt.legend(loc="upper right")
    plt.show()


# Función para graficar la onda tangente con amplitud, frecuencia, desfase y término constante
def graficar_tangente(amplitud, frecuencia, desfase, constante):
    # Definir el rango de los valores de x, evitando las asíntotas de la tangente
    x = np.linspace(-3 * np.pi, 3 * np.pi, 1000)  # De -2π a 2π para ver varios ciclos

    # Calcular los valores de y usando la función tangente
    y = amplitud * np.tan(frecuencia * x + desfase) + constante

    # Limitar los valores de y para evitar que crezcan demasiado cerca de las asíntotas
    y = np.clip(y, -10, 10)  # Limitar el rango de y entre -10 y 10

    # Limpiar la figura
    plt.figure(figsize=(10, 5))
    plt.plot(x, y, label=f"$y = {amplitud} \\cdot \\tan({frecuencia}x + {desfase}) + {constante}$", color='purple')
    plt.title(f"Onda Tangencial: Amplitud = {amplitud}, Frecuencia = {frecuencia}, Desfase = {desfase}, Constante = {constante}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.ylim(-3*np.pi,3*np.pi)
    plt.xticks([-3 * np.pi,-2 * np.pi, -np.pi, 0, np.pi, 2 * np.pi,3 * np.pi], 
               [r'$-3\pi$',r'$-2\pi$', r'$-\pi$', '0', r'$\pi$', r'$2\pi$',r'$3\pi$'])
    plt.grid(True)

    # Dibujar las asíntotas verticales en múltiplos de π/frecuencia
    for i in range(-2, 3):
        plt.axvline(x=(i * np.pi - desfase) / frecuencia, color='red', linestyle='--', alpha=0.5)

    plt.legend(loc="upper right")
    plt.show()

# Función para graficar la onda seno con desfase, con el coseno fijo de fondo
def graficar_seno_desfase(desfase):
    # Definir el rango de los valores de x
    x = np.linspace(-3 * np.pi, 3 * np.pi, 1000)  # De -2π a 2π para ver varios ciclos

    # Calcular los valores de y para la función seno y coseno
    y_seno = np.sin(x + desfase)  # Función seno con desfase
    y_cos = np.cos(x)             # Función coseno fija

    # Limpiar la figura
    plt.figure(figsize=(10, 5))

    # Graficar la función coseno como fondo
    plt.plot(x, y_cos, label=f"$\\cos(x)$ (fija)", color='blue', linestyle='--', alpha=0.7)

    # Graficar la función seno con el desfase ajustado
    plt.plot(x, y_seno, label=f"$\\sin(x + {desfase:.2f})$", color='purple')

    # Ajustar título y etiquetas
    plt.title(f"Función Seno con Desfase: Desfase = {desfase:.2f} rad")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.xlim(-3*np.pi,3*np.pi)
    plt.xticks([-3 * np.pi,-2 * np.pi, -np.pi, 0, np.pi, 2 * np.pi,3 * np.pi], 
               [r'$-3\pi$',r'$-2\pi$', r'$-\pi$', '0', r'$\pi$', r'$2\pi$',r'$3\pi$'])
    plt.grid(True)

    plt.legend(loc="upper right")
    plt.show()

# Función para graficar las funciones trigonométricas inversas con una cuadrícula cuadrada
def graficar_inversas():
    # Definir el rango de x para las funciones inversas
    x_sin_cos = np.linspace(-1, 1, 1000)
    x_tan = np.linspace(-10, 10, 1000)

    # Calcular las funciones inversas
    y_arcsin = np.arcsin(x_sin_cos)
    y_arccos = np.arccos(x_sin_cos)
    y_arctan = np.arctan(x_tan)

    # Crear la figura con tres subgráficos (uno para cada función)
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 12))

    # Graficar la función arcsin(x)
    ax1.plot(x_sin_cos, y_arcsin, label=r"$\arcsin(x)$", color='blue', linewidth=2)
    ax1.set_title("Función Inversa del Seno", fontsize=14)
    ax1.set_xlabel("x", fontsize=12)
    ax1.set_ylabel("y", fontsize=12)
    ax1.grid(True)
    ax1.set_aspect('equal')  # Cuadrícula cuadrada
    ax1.legend(fontsize=12)
    
    # Etiquetas del eje y para arcsin
    ax1.set_yticks([-np.pi/2, 0, np.pi/2])
    ax1.set_yticklabels([r"$-\frac{\pi}{2}$", "0", r"$\frac{\pi}{2}$"])

    # Graficar la función arccos(x)
    ax2.plot(x_sin_cos, y_arccos, label=r"$\arccos(x)$", color='green', linewidth=2)
    ax2.set_title("Función Inversa del Coseno", fontsize=14)
    ax2.set_xlabel("x", fontsize=12)
    ax2.set_ylabel("y", fontsize=12)
    ax2.grid(True)
    ax2.set_aspect('equal')  # Cuadrícula cuadrada
    ax2.legend(fontsize=12)
    
    # Etiquetas del eje y para arccos
    ax2.set_yticks([0, np.pi/2, np.pi])
    ax2.set_yticklabels(["0", r"$\frac{\pi}{2}$", r"$\pi$"])

    # Graficar la función arctan(x)
    ax3.plot(x_tan, y_arctan, label=r"$\arctan(x)$", color='purple', linewidth=2)
    ax3.set_title("Función Inversa de la Tangente", fontsize=14)
    ax3.set_xlabel("x", fontsize=12)
    ax3.set_ylabel("y", fontsize=12)
    ax3.grid(True)
    ax3.set_aspect('equal')  # Cuadrícula cuadrada
    ax3.legend(fontsize=12)

    # Etiquetas del eje y para arctan
    ax3.set_yticks([-np.pi/2, 0, np.pi/2])
    ax3.set_yticklabels([r"$-\frac{\pi}{2}$", "0", r"$\frac{\pi}{2}$"])

    # Ajustar el espaciado y mostrar las gráficas
    plt.tight_layout()
    plt.show()

# Función para graficar y resolver la ecuación seno
def resolver_seno(A):
    # Definir el rango de x (el ángulo θ) en el intervalo [-2π, 2π]
    x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
    
    # Calcular la función seno
    y = np.sin(x)
    
    # Graficar la función seno
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label=r"$\sin(\theta)$", color='blue')
    
    # Graficar la línea horizontal en y = A
    plt.axhline(y=A, color='red', linestyle='--', label=f"$y = {A}$")
    
    # Encontrar las soluciones gráficamente
    sol_x = x[np.isclose(y, A, atol=0.01)]
    
    # Graficar las soluciones encontradas
    for sol in sol_x:
        plt.plot(sol, A, 'ro')  # Poner un punto en cada solución
        plt.text(sol, A + 0.05, f"$\\theta = {sol:.2f}$", fontsize=12, color='red')
    
    # Ajustar el gráfico
    plt.title(f"Soluciones de $\\sin(\\theta) = {A}$ en el intervalo $[-2\\pi, 2\\pi]$")
    plt.xlabel("$\\theta$")
    plt.ylabel("$\\sin(\\theta)$")
    plt.xlim(-2 * np.pi, 2 * np.pi)
    plt.ylim(-1.5, 1.5)
    plt.xticks([-2 * np.pi, -3 * np.pi / 2, -np.pi, -np.pi / 2, 0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi],
               [r'$-2\pi$', r'$-\frac{3\pi}{2}$', r'$-\pi$', r'$-\frac{\pi}{2}$', '0', r'$\frac{\pi}{2}$', r'$\pi$', r'$\frac{3\pi}{2}$', r'$2\pi$'])
    plt.grid(True)
    plt.legend()
    plt.show()

# Función para graficar la ecuación trigonométrica
def graficar_funcion_trigonometrica(rango_x=(0, 2 * np.pi), num_puntos=1000, figsize=(8, 6)):
    # Definir el rango de x
    x = np.linspace(rango_x[0], rango_x[1], num_puntos)
    
    # Definir la función trigonométrica
    y = 2 * np.sin(x)**2 - np.sin(x) - 1
    
    # Crear la figura
    plt.figure(figsize=figsize)
    
    # Graficar la función
    plt.plot(x, y, label=r"$2\sin^2(x) - \sin(x) - 1$", color='blue')
    
    # Añadir líneas verticales y horizontales
    plt.axhline(0, color='black', linewidth=1)  # Línea horizontal en y=0
    plt.axvline(np.pi / 2, color='red', linestyle='--', label=r"$\frac{\pi}{2}$")
    plt.axvline(7 * np.pi / 6, color='red', linestyle='--', label=r"$\frac{7\pi}{6}$")
    plt.axvline(11 * np.pi / 6, color='red', linestyle='--', label=r"$\frac{11\pi}{6}$")
    
    # Etiquetas y leyenda
    plt.title("Gráfica de $2\sin^2(x) - \sin(x) - 1 = 0$", fontsize=16)
    plt.xlabel("x", fontsize=12)
    plt.ylabel("y", fontsize=12)
    plt.grid(True)
    plt.legend()
    
    # Mostrar la gráfica
    plt.show()

# Función para graficar las funciones trigonométricas secante, cosecante y cotangente

def graficar_funciones_trigonometricasotras():
    # Definir el rango de x, excluyendo puntos donde sin(x) y cos(x) son 0
    x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

    # Definir las funciones secante, cosecante y tangente
    def sec(x):
        return 1 / np.cos(x)

    def csc(x):
        return 1 / np.sin(x)

    def cot(x):
        return 1/np.tan(x)

    # Crear una figura con tres gráficos separados
    plt.figure(figsize=(10, 12))

    # Gráfico de sec(x)
    plt.subplot(3, 1, 1)  # Primer subplot
    plt.plot(x, sec(x), label=r"$\sec(x)$", color='blue', linewidth=2)
    plt.axhline(0, color='black',linewidth=1)
    plt.axvline(x=0, color='black',linewidth=1)
    plt.ylim(-10, 10)
    plt.title(r"Gráfica de $\sec(x)$", fontsize=16)
    plt.xticks([-2 * np.pi, -3 * np.pi / 2, -np.pi, -np.pi / 2, 0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi],
               [r'$-2\pi$', r'$-\frac{3\pi}{2}$', r'$-\pi$', r'$-\frac{\pi}{2}$', '0', r'$\frac{\pi}{2}$', r'$\pi$', r'$\frac{3\pi}{2}$', r'$2\pi$'])
    plt.grid(True)
    plt.legend()

    # Gráfico de csc(x)
    plt.subplot(3, 1, 2)  # Segundo subplot
    plt.plot(x, csc(x), label=r"$\csc(x)$", color='green', linewidth=2)
    plt.axhline(0, color='black',linewidth=1)
    plt.axvline(x=0, color='black',linewidth=1)
    plt.ylim(-10, 10)
    plt.title(r"Gráfica de $\csc(x)$", fontsize=16)
    plt.xticks([-2 * np.pi, -3 * np.pi / 2, -np.pi, -np.pi / 2, 0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi],
               [r'$-2\pi$', r'$-\frac{3\pi}{2}$', r'$-\pi$', r'$-\frac{\pi}{2}$', '0', r'$\frac{\pi}{2}$', r'$\pi$', r'$\frac{3\pi}{2}$', r'$2\pi$'])
    plt.grid(True)
    plt.legend()

    # Gráfico de cotan(x)
    plt.subplot(3, 1, 3)  # Tercer subplot
    plt.plot(x, cot(x), label=r"$\cot(x)$", color='purple', linewidth=2)
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(x=0, color='black', linewidth=1)
    plt.ylim(-10, 10)
    plt.title(r"Gráfica de $\cot(x)$", fontsize=16)
    plt.xticks([-2 * np.pi, -3 * np.pi / 2, -np.pi, -np.pi / 2, 0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi],
               [r'$-2\pi$', r'$-\frac{3\pi}{2}$', r'$-\pi$', r'$-\frac{\pi}{2}$', '0', r'$\frac{\pi}{2}$', r'$\pi$', r'$\frac{3\pi}{2}$', r'$2\pi$'])
    plt.grid(True)
    plt.legend()

    # Ajustar el espacio entre subplots
    plt.tight_layout()

    # Mostrar la gráfica
    plt.show()
# Función para visualizar la identidad pitagórica

def identidad_pitagorica(theta_deg):
    # Convertir el ángulo a radianes
    theta_rad = np.deg2rad(theta_deg)

    # Calcular el seno y el coseno
    seno = np.sin(theta_rad)
    coseno = np.cos(theta_rad)
    identidad = seno**2 + coseno**2

    # Limpiar la figura
    plt.figure(figsize=(6, 6))

    # Dibujar el círculo unitario
    circle = plt.Circle((0, 0), 1, color='lightblue', fill=False)
    plt.gca().add_patch(circle)

    # Dibujar el triángulo
    plt.plot([0, coseno], [0, seno], 'k-', lw=2)
    plt.plot([coseno, coseno], [0, seno], 'k--')
    plt.plot([0, coseno], [0, 0], 'k--')

    # Anotar los valores de seno, coseno y la identidad
    plt.text(0.1, 0.9, f"$\\sin^2(\\theta) + \\cos^2(\\theta) = {identidad:.2f}$", fontsize=12, color='red')
    plt.text(0.5, seno / 2, f"$\\sin(\\theta) = {seno:.2f}$", fontsize=12, color='blue')
    plt.text(coseno / 2, -0.1, f"$\\cos(\\theta) = {coseno:.2f}$", fontsize=12, color='green')

    # Ajustes de la gráfica
    plt.xlim(-1.5, 1.5)
    plt.ylim(-1.5, 1.5)
    plt.gca().set_aspect('equal')
    plt.grid(True)
    plt.axhline(0, color='black',linewidth=1)
    plt.axvline(0, color='black',linewidth=1)
    plt.title(f"Identidad Pitagórica para $\\theta = {theta_deg}^\\circ$")
    plt.show()

# Función para dibujar los dos triángulos rectángulos y las fracciones al lado
def plot_two_triangles(angle_radians, hypotenuse1, hypotenuse2):
    # Cálculo de los lados para ambos triángulos
    opposite1 = np.sin(angle_radians) * hypotenuse1
    adjacent1 = np.cos(angle_radians) * hypotenuse1
    
    opposite2 = np.sin(angle_radians) * hypotenuse2
    adjacent2 = np.cos(angle_radians) * hypotenuse2
    
    # Configuración de las subgráficas
    fig, ax = plt.subplots(1, 2, figsize=(12, 8))
    
    # Subgráfico 1: Dibujar los triángulos
    ax[0].plot([0, adjacent1], [0, 0], 'r', lw=3, label='CA')
    ax[0].plot([adjacent1, adjacent1], [0, opposite1], 'b', lw=3, label='CO')
    ax[0].plot([0, adjacent1], [0, opposite1], 'g', lw=3, label='H')
    
    ax[0].plot([0, adjacent2], [0, 0], 'orange', lw=3, label='CA ')
    ax[0].plot([adjacent2, adjacent2], [0, opposite2], 'purple', lw=3, label='CO')
    ax[0].plot([0, adjacent2], [0, opposite2], 'pink', lw=3, label='H')
    
    ax[0].set_xlim(-0.5, max(adjacent1, adjacent2) + 0.5)
    ax[0].set_ylim(-0.5, max(opposite1, opposite2) + 0.5)
    ax[0].set_aspect('equal')
    ax[0].grid(True)
    ax[0].legend()
    ax[0].set_title("Dos triángulos con diferentes hipotenusas")
    
    # Subgráfico 2: Mostrar las fracciones y cocientes de coseno y seno
    ax[1].axis('off')  # Ocultamos los ejes
    fraction_of_pi = angle_radians / np.pi  # Convertir ángulo a múltiplos de π
    
    # Cálculo del cociente de coseno (adyacente / hipotenusa)
    cos_cociente1 = adjacent1 / hypotenuse1
    cos_cociente2 = adjacent2 / hypotenuse2
    
    # Cálculo del cociente de seno (opuesto / hipotenusa)
    sin_cociente1 = opposite1 / hypotenuse1
    sin_cociente2 = opposite2 / hypotenuse2
    
    # Texto de coseno en una sola línea con colores
    ax[1].text(0.1, 0.7, f"cos({fraction_of_pi:.2f}π) =", fontsize=14, color='black')
    ax[1].text(0.4, 0.7, f"{adjacent1:.2f}", fontsize=14, color='red')
    ax[1].text(0.5, 0.7, "/", fontsize=14, color='black')
    ax[1].text(0.55, 0.7, f"{hypotenuse1:.2f}", fontsize=14, color='green')
    ax[1].text(0.65, 0.7, f"= {cos_cociente1:.2f}=", fontsize=14, color='black')
    
    ax[1].text(0.9, 0.7, f"{adjacent2:.2f}", fontsize=14, color='orange')
    ax[1].text(1., 0.7, "/", fontsize=14, color='black')
    ax[1].text(1.01, 0.7, f"{hypotenuse2:.2f}", fontsize=14, color='pink')
    ax[1].text(1.11, 0.7, f"= {cos_cociente2:.2f}", fontsize=14, color='black')
    
    # Texto de seno en una sola línea con colores
    ax[1].text(0.1, 0.6, f"sin({fraction_of_pi:.2f}π) =", fontsize=14, color='black')
    ax[1].text(0.4, 0.6, f"{opposite1:.2f}", fontsize=14, color='blue')
    ax[1].text(0.5, 0.6, "/", fontsize=14, color='black')
    ax[1].text(0.55, 0.6, f"{hypotenuse1:.2f}", fontsize=14, color='green')
    ax[1].text(0.65, 0.6, f"= {sin_cociente1:.2f}=", fontsize=14, color='black')
    
    ax[1].text(0.9, 0.6, f"{opposite2:.2f}", fontsize=14, color='purple')
    ax[1].text(1., 0.6, "/", fontsize=14, color='black')
    ax[1].text(1.01, 0.6, f"{hypotenuse2:.2f}", fontsize=14, color='pink')
    ax[1].text(1.11, 0.6, f"= {sin_cociente2:.2f}", fontsize=14, color='black')
    
    plt.show()