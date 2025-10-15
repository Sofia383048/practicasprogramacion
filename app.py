import streamlit as st
import math

# Título y descripción
st.title("🟢 Calculadora de Área de un Círculo")
st.write("Esta aplicación calcula el área de un círculo usando la fórmula:")
st.latex("A = \\pi r^2")

# Entrada de datos
radio = st.slider("Selecciona el radio (en unidades):", 0.0, 20.0, 5.0)

# Cálculo del área y perímetro
area = math.pi * radio**2
perimetro = 2 * math.pi * radio

# Mostrar resultados
st.subheader("Resultados:")
st.write(f"✅ **Área:** {area:.2f} unidades²")
st.write(f"📏 **Perímetro:** {perimetro:.2f} unidades")

st.markdown("---")
st.write("### Visualización del círculo")

# Pequeña visualización con matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

fig, ax = plt.subplots()
circle = Circle((0, 0), radio, fill=False, color="blue", linewidth=2)
ax.add_patch(circle)
ax.set_aspect("equal")
ax.set_xlim(-radio*1.2, radio*1.2)
ax.set_ylim(-radio*1.2, radio*1.2)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.grid(True)
st.pyplot(fig)

# Pie de página
st.markdown("---")
st.caption("Creado por [Tu nombre] — usando Streamlit y Python 💻")
