import streamlit as st
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Polygon

# Título principal
st.title("📐 Mi aplicación para calcular el área y perímetro de figuras geométricas")

# Selección de figura
figura = st.selectbox(
    "Selecciona una figura:",
    ("Círculo", "Triángulo", "Rectángulo", "Cuadrado")
)

# Color de la figura
color = st.color_picker("Elige un color para la figura:", "#1f77b4")

# --- Cálculo según figura seleccionada ---
if figura == "Círculo":
    st.header("🔵 Círculo")
    st.latex("A = \\pi r^2 \\quad\\text{y}\\quad P = 2\\pi r")
    radio = st.slider("Selecciona el radio (r):", 0.0, 20.0, 5.0)
    area = math.pi * radio**2
    perimetro = 2 * math.pi * radio
    st.success(f"Área = {area:.2f} unidades²")
    st.success(f"Perímetro = {perimetro:.2f} unidades")

    # Gráfico
    fig, ax = plt.subplots()
    circle = Circle((0, 0), radio, edgecolor=color, facecolor='none', linewidth=2)
    ax.add_patch(circle)
    ax.set_xlim(-radio * 1.3, radio * 1.3)
    ax.set_ylim(-radio * 1.3, radio * 1.3)
    ax.set_aspect('equal')
    ax.set_title("Visualización del círculo")
    st.pyplot(fig)

elif figura == "Triángulo":
    st.header("🔺 Triángulo")
    st.latex("A = \\frac{b \\cdot h}{2}")
    base = st.number_input("Base (b):", min_value=0.0, value=5.0)
    altura = st.number_input("Altura (h):", min_value=0.0, value=4.0)
    lado1 = st.number_input("Lado 1:", min_value=0.0, value=3.0)
    lado2 = st.number_input("Lado 2:", min_value=0.0, value=4.0)
    lado3 = st.number_input("Lado 3:", min_value=0.0, value=5.0)
    area = (base * altura) / 2
    perimetro = lado1 + lado2 + lado3
    st.success(f"Área = {area:.2f} unidades²")
    st.success(f"Perímetro = {perimetro:.2f} unidades")

    # Gráfico (triángulo isósceles centrado)
    fig, ax = plt.subplots()
    puntos = [[0, 0], [base, 0], [base / 2, altura]]
    triangulo = Polygon(puntos, edgecolor=color, facecolor='none', linewidth=2)
    ax.add_patch(triangulo)
    ax.set_xlim(-1, base + 1)
    ax.set_ylim(-1, altura + 1)
    ax.set_aspect('equal')
    ax.set_title("Visualización del triángulo")
    st.pyplot(fig)

elif figura == "Rectángulo":
    st.header("🟥 Rectángulo")
    st.latex("A = b \\cdot h \\quad\\text{y}\\quad P = 2(b+h)")
    base = st.number_input("Base (b):", min_value=0.0, value=6.0)
    altura = st.number_input("Altura (h):", min_value=0.0, value=3.0)
    area = base * altura
    perimetro = 2 * (base + altura)
    st.success(f"Área = {area:.2f} unidades²")
    st.success(f"Perímetro = {perimetro:.2f} unidades")

    # Gráfico
    fig, ax = plt.subplots()
    rect = Rectangle((0, 0), base, altura, edgecolor=color, facecolor='none', linewidth=2)
    ax.add_patch(rect)
    ax.set_xlim(-1, base + 1)
    ax.set_ylim(-1, altura + 1)
    ax.set_aspect('equal')
    ax.set_title("Visualización del rectángulo")
    st.pyplot(fig)

elif figura == "Cuadrado":
    st.header("⬛ Cuadrado")
    st.latex("A = l^2 \\quad\\text{y}\\quad P = 4l")
    lado = st.slider("Selecciona el lado (l):", 0.0, 20.0, 5.0)
    area = lado**2
    perimetro = 4 * lado
    st.success(f"Área = {area:.2f} unidades²")
    st.success(f"Perímetro = {perimetro:.2f} unidades")

    # Gráfico
    fig, ax = plt.subplots()
    cuadrado = Rectangle((0, 0), lado, lado, edgecolor=color, facecolor='none', linewidth=2)
    ax.add_patch(cuadrado)
    ax.set_xlim(-1, lado + 1)
    ax.set_ylim(-1, lado + 1)
    ax.set_aspect('equal')
    ax.set_title("Visualización del cuadrado")
    st.pyplot(fig)

# Pie de página
st.markdown("---")
st.caption("Creado por Sofía Fernanda Lechuga Chávez — Programación 💻")
