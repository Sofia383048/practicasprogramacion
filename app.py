import streamlit as st
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Polygon

st.set_page_config(
    page_title="Cálculo de área y perímetro",
    page_icon="📐",
    layout="wide"
)

with st.sidebar:
    st.title("Información del alumno")
    st.write("**Nombre:** Sofía Fernanda Lechuga Chávez")
    st.write("**Matrícula:** 383048")
    st.markdown("---")
    st.write("Aplicación hecha en Streamlit")
    
st.title("📏 Cálculo de área y perímetro de figuras geométricas")


figura = st.selectbox(
    "Selecciona una figura geométrica:",
    ["Círculo", "Triángulo", "Rectángulo", "Cuadrado"]
)

if figura == "Círculo":
    radio = st.slider("Selecciona el radio", 0.0, 50.0, 10.0)
    area = math.pi * radio**2
    perimetro = 2 * math.pi * radio
    st.success(f"🔹 Área: {area:,.2f}")
    st.success(f"🔹 Perímetro: {perimetro:,.2f}")

    st.subheader("Visualización del círculo")
    fig, ax = plt.subplots()
    circle = Circle((0, 0), radio, fill=False, color="lime", linewidth=2)
    ax.add_patch(circle)
    ax.set_aspect('equal')
    ax.set_xlim(-radio*1.2, radio*1.2)
    ax.set_ylim(-radio*1.2, radio*1.2)
    ax.axis('off')
    st.pyplot(fig)

elif figura == "Triángulo":
    base = st.slider("Base", 0.0, 50.0, 10.0)
    altura = st.slider("Altura", 0.0, 50.0, 8.0)
    lado1 = st.number_input("Lado 1:", 0.0, 50.0, 10.0)
    lado2 = st.number_input("Lado 2:", 0.0, 50.0, 10.0)
    lado3 = st.number_input("Lado 3:", 0.0, 50.0, 10.0)
    area = (base * altura) / 2
    perimetro = lado1 + lado2 + lado3
    st.success(f"🔹 Área: {area:,.2f}")
    st.success(f"🔹 Perímetro: {perimetro:,.2f}")

    st.subheader("Visualización del triángulo")
    fig, ax = plt.subplots()
    puntos = [[0, 0], [base, 0], [base / 2, altura]]
    triangulo = Polygon(puntos, edgecolor='lime', facecolor='none', linewidth=2)
    ax.add_patch(triangulo)
    ax.set_xlim(-1, base + 1)
    ax.set_ylim(-1, altura + 1)
    ax.axis('off')
    st.pyplot(fig)

elif figura == "Rectángulo":
    base = st.slider("Base", 0.0, 50.0, 12.0)
    altura = st.slider("Altura", 0.0, 50.0, 6.0)
    area = base * altura
    perimetro = 2 * (base + altura)
    st.success(f"🔹 Área: {area:,.2f}")
    st.success(f"🔹 Perímetro: {perimetro:,.2f}")

    st.subheader("Visualización del rectángulo")
    fig, ax = plt.subplots()
    rect = Rectangle((0, 0), base, altura, fill=False, color="lime", linewidth=2)
    ax.add_patch(rect)
    ax.set_xlim(-1, base + 1)
    ax.set_ylim(-1, altura + 1)
    ax.axis('off')
    st.pyplot(fig)

elif figura == "Cuadrado":
    lado = st.slider("Selecciona el lado", 0.0, 50.0, 10.0)
    area = lado**2
    perimetro = 4 * lado
    st.success(f"🔹 Área: {area:,.2f}")
    st.success(f"🔹 Perímetro: {perimetro:,.2f}")

    st.subheader("Visualización del cuadrado")
    fig, ax = plt.subplots()
    cuadrado = Rectangle((0, 0), lado, lado, fill=False, color="lime", linewidth=2)
    ax.add_patch(cuadrado)
    ax.set_xlim(-1, lado + 1)
    ax.set_ylim(-1, lado + 1)
    ax.axis('off')
    st.pyplot(fig)

st.markdown("---")
st.header("📈 Funciones Trigonométricas")

rango = st.slider("Rango (x)", 0.0, 10 * math.pi, 6.28)
amplitud = st.slider("Amplitud", 0.1, 5.0, 1.0)

x = np.linspace(0, rango, 1000)
y_sin = amplitud * np.sin(x)
y_cos = amplitud * np.cos(x)
y_tan = amplitud * np.tan(x)

fig, ax = plt.subplots()
ax.plot(x, y_sin, label="sin(x)", color='orange')
ax.plot(x, y_cos, label="cos(x)", color='cyan')

mask = np.abs(y_tan) < 10
ax.plot(x[mask], y_tan[mask], label="tan(x)", color='lime')
ax.legend()
ax.set_title("Funciones Trigonométricas")
ax.grid(True)
st.pyplot(fig)


