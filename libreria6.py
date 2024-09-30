import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display, clear_output

 




# Función para graficar la función exponencial
def grafica_funcion_exp(a, b, c,d):
    x = np.linspace(-10, 10, 400)
    y = a*np.exp(b*x + c)+d
    plt.plot(x, y, label=f'{a}$exp(x{b}+{c})$ + {d}')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.title('Gráfica de la función exponencial ')
    plt.show()

# Crear los deslizadores
a_slider = widgets.FloatSlider(min=-10, max=10, step=0.1, value=1, description='a')
b_slider = widgets.FloatSlider(min=-10, max=10, step=0.1, value=0, description='b')
c_slider = widgets.FloatSlider(min=-10, max=10, step=0.1, value=0, description='c')
d_slider = widgets.FloatSlider(min=-10, max=10, step=0.1, value=0, description='d')

# Función para actualizar la gráfica
def update_grafica_exp(a, b, c,d):
    grafica_funcion_exp(a, b, c,d)


# Función para graficar la función logaritmica
def grafica_funcion_log(a, b, c, d):
    x = np.linspace(0.001, 10, 400)
    y = a*np.log(b*x + c)+d
    plt.plot(x, y, label=f'{a}ln({b}x + {c})+{d}')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.xlim(0, 10)
    plt.ylim(-10, 10)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.title('Gráfica de la función exponencial ')
    plt.show()

# Crear los deslizadores
a_slider = widgets.FloatSlider(min=-10, max=10, step=0.1, value=1, description='a')
b_slider = widgets.FloatSlider(min=-10, max=10, step=0.1, value=1, description='b')
c_slider = widgets.FloatSlider(min=-10, max=10, step=0.1, value=0, description='c')
d_slider = widgets.FloatSlider(min=-10, max=10, step=0.1, value=0, description='d')

# Función para actualizar la gráfica
def update_grafica_log(a, b, c,d):
    grafica_funcion_log(a, b, c,d)