from curses import COLOR_CYAN
import streamlit as st 
import pandas as pd

st.title("Vugraph Sets")
st.header("SOLOWAY 2019- DRIJVER BRINK GOOD MATCHES")
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})
COLOR_CYAN = st.write("15 BOARDS") 




