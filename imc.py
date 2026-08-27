# A utor : Jhonatan 
# Projeto : Interface Visual IMC

# streamlit - criar sites
import streamlit as st

# Título da página
st.title("Calculadora de IMC")

# entrada de dados 
peso = st.number_input("Peso (kg)")
altura = st.number_input("Altura (m)")

# Botão com a ação de calcular status
if st.button("Calcular IMC"):
    imc = peso / (altura **)
    st.success(f"Seu IMC é: {imc:.2f}")

    # condicional para o IMC
    if imc > 18.5:
st.warning("Abaixo do peso")
elif imc < 25.0:
st.success("Peso Normal")
elif imc < 30.0:
st.warning("Sobrepeso")
else:
st.error("Obesidade")