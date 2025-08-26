import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv('pizzas.csv')

model = LinearRegression()
x = df[['diametro']]
y = df[['preco']]

st.title('Previsão de Preço de Pizza por Diâmetro')
st.divider()

diametro = st.number_input('Diâmetro da Pizza em (cm)', min_value=0, max_value=999, value=30, step=1, key='diametro')

if diametro:
    model.fit(x, y)
    preco = model.predict([[diametro]])[0][0]
    st.write(f'O preço previsto para uma pizza de {diametro} cm é R$ {preco:.2f}')
