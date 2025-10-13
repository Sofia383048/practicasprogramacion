import streamlit as st
import math
st.title("mi aplicacion para calcular el area de un circulo")
radio= st.slider("Selecciona el radio", 0.0, 10.0, 5.0)
area= math.pi * radio**2
st.write(f"El area del circulo con radio {radio} es:{area: .2f}")
