import streamlit as st
import re

st.title("Clasificador de Gastos con IA")

gasto = st.text_input("Ingresa un gasto")

if gasto:

    # Buscar monto
    monto = re.findall(r'\d+', gasto)

    if monto:
        monto = monto[0]
    else:
        monto = "0"

    # Limpiar descripción
    descripcion = re.sub(r'\d+', '', gasto).strip()

    # Categorías básicas
    texto = gasto.lower()

    if "almuerzo" in texto or "cena" in texto or "comida" in texto:
        categoria = "Alimentación"

    elif "uber" in texto or "taxi" in texto or "bus" in texto:
        categoria = "Transporte"

    elif "cuaderno" in texto or "libro" in texto:
        categoria = "Educación"

    else:
        categoria = "Otros"

    st.subheader("Resultado")

    st.write("**Categoría:**", categoria)
    st.write("**Monto:** $", monto)
    st.write("**Descripción:**", descripcion)