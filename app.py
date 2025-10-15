import streamlit as st
import math

st.title("Mi aplicacion para calcular el area y perímetro de figuras geométricas")
st.title("Cálculo del área de un círculo")
st.latex("A = \\pi r^2")

radio = st.slider("Selecciona el radio (en unidades):", 0.0, 20.0, 5.0)
area = math.pi * radio**2
perimetro = 2 * math.pi * radio
