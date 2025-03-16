import streamlit as st
from pages import home, chatbot, healthcare, history, law, tourism

st.set_page_config(page_title="chat with us", page_icon="🐘", layout="wide")
st.markdown("""
    <style>
        [data-testid="stSidebarNav"] { display: none; }  /* Hides extra navigation */
    </style>
""", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'> <marquee>WELCOME TO OUR HELPDESK </marquee></h1>", unsafe_allow_html=True)

def main():
    st.sidebar.title("Pages")
    
    selected_page = st.sidebar.radio("Select a page", ["Home", "Chatbot", "Law", "Tourism","Healthcare","History"])

    if selected_page == "Home":
        home.app()
    elif selected_page == "Chatbot":
        chatbot.app()
    elif selected_page == "Law":
        law.app()
    elif selected_page == "Tourism":
        tourism.app()
    elif selected_page == "Healthcare":
        healthcare.app()
    elif selected_page =="History":
        history.app()

main()
    

