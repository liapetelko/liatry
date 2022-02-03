import streamlit as st

st.title("Hi")
st.header("Hello!")
st.subheader("subb")
st.text("please write the vugrapg name")
if st.button("press this"):
  st.text("Write something")
  selectbox = st.selectbox(["Yes","No"])
  if st.textbox()=="hello":
    st.button("works!")
#image = st.file_uploader("Upload image",[JPG,PNG])

#st.sidebar.title("select..")
