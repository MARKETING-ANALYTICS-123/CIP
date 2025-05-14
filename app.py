import streamlit as st
from streamlit_extras.switch_page_button import switch_page
 
# Page Config
st.set_page_config(page_title="Snowtrack", layout="wide")
 
# Header / Navigation Bar
with st.container():
    st.markdown(
        """
        <div style="background-color:#29B5E8;padding:10px 20px;border-radius:0px 0px 10px 10px;">
            <h1 style="color:white;text-align:center;">Snowtrack</h1>
        </div>
        """,
        unsafe_allow_html=True,
    )
 
# Spacer
st.write("")
 
# Card Section
st.markdown("## Welcome to Snowtrack")
st.markdown("---")
 
# Card-like Button (fixed)
with st.container():
   st.markdown(
    """
    <div style="padding:30px;border-radius:15px;background-color:#f0f2f6;text-align:center;">
        <h3 style="color:#000000; padding: 60px;">Let's Get Started 🚀</h3>
        <a href="/page1">
            <button style="padding:10px 30px;font-size:16px;background-color:#29B5E8;color:white;border:none;border-radius:10px;cursor:pointer;">
                Enter
            </button>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)
 