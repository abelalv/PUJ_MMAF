import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display, clear_output

# Función para graficar el polinomio
def grafica_polinomio(coefs):
    x = np.linspace(-10, 10, 400)
    y = np.polyval(coefs[::-1], x)  # Invertir los coeficientes
    plt.plot(x, y, label='Polinomio')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    polinomio_str = ' '.join([f'{coef:.2f}' if i == 0 else (f'- {abs(coef):.2f}x' if i == 1 else f'- {abs(coef):.2f}x^{i}') if coef < 0 else (f'+ {coef:.2f}x' if i == 1 else f'+ {coef:.2f}x^{i}') for i, coef in enumerate(coefs)])
    plt.title('$' + polinomio_str + '$', fontsize=16)
    plt.show()
    

# Función para crear los widgets
def crear_widget_polinomio():
    grado_slider = widgets.IntSlider(min=0, max=10, step=1, value=0, description='Grado')
    coef_sliders = [widgets.FloatSlider(min=-10, max=10, step=0.1, value=0, description=f'Coef {i}') for i in range(grado_slider.value + 1)]
    coef_container = widgets.VBox(coef_sliders)
    output = widgets.Output()

    def update_coef_sliders(change):
        coef_sliders = [widgets.FloatSlider(min=-10, max=10, step=0.1, value=0, description=f'Coef {i}') for i in range(change.new + 1)]
        coef_container.children = coef_sliders
        for slider in coef_sliders:
            slider.observe(update_grafica, 'value')
        update_grafica()

    grado_slider.observe(update_coef_sliders, 'value')

    def update_grafica(*args):
        coefs = [slider.value for slider in coef_container.children]
        with output:
            clear_output(wait=True)
            grafica_polinomio(coefs)

    for slider in coef_sliders:
        slider.observe(update_grafica, 'value')

    display(grado_slider, coef_container, output)
    update_grafica()


