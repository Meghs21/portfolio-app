import streamlit as st

col1, col2= st.columns(2)

with col1:
    st.image("imageshai/myimage.png")

with col2:
    st.title("Meghna Mandawra")
    content="""Passionate About Learning:
     I'm a first-year enthusiast who loves learning 
     new things. I enjoy taking on challenges and 
     growing through them. Whether it's exploring 
     new technologies or staying updated on trends, 
     I'm always eager to expand my skills and knowledge. 
     """
    st.info(content)