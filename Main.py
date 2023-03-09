import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title='iBIKE'
)

st.write('# Welcome to iBIKE! 👋')

st.markdown(
    """
    iBIKE is an online simuation game developed to create 
    an environment for **Mechanical Engineers**, **Electrical Engineers**, 
    **Inustrial Engineers**, and **Product Managers** to practice their skills
    in selecting the appropriate parts, their order quantities, best materials 
    and manufacturing processes, parcticing supply chain management, and more.

    **👈 Select your role from the sidebar to start**
    """
)

st.image('bike_image.jpg')