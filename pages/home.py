import streamlit as st
import wikipedia as wd
def app():
    st.title("Jaipur City Guide")
    st.header("Welcome to the Pink City -JAIPUR!")
    result=wd.summary("Jaipur",sentences=8)
    st.write(result) 
    
    # Add images of Jaipur
    st.image("pic1.jpg", caption=" Hawa Mahal", use_container_width=True)
    st.image("pic2.jpg", caption=" Amber Fort", use_container_width=True)