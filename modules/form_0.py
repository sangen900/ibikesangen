import streamlit as st
def render():
    st.markdown(
        """
        <p style='font-size: 20px; margin-bottom: 0;'>Do you want to take the survey? If you want to take it, please proceed.</p>
        """,
        unsafe_allow_html=True
    )
