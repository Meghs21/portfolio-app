import streamlit as st

col1, col2= st.columns(2)

with col1:
    st.image("imageshai/myimage.png",width=280)

with col2:
    st.title("Meghna Mandawra")
    content="""
    Passionate About Learning:
     I'm a first-year enthusiast who loves learning 
     new things. I enjoy taking on challenges and 
     growing through them. Whether it's exploring 
     new technologies or staying updated on trends, 
     I'm always eager to expand my skills and knowledge. 
     """
    cont="Below you can find some of the apps i have built in python,Feel free to contact me."
    st.info(content)
st.write(cont)