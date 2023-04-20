import streamlit as st
import pandas as pd
from os import path
import os

st.set_page_config(page_title='Project Manager')

if path.isfile('parts_selction.csv'):
    st.header(":blue[Mechanical Engineer]")
    st.markdown("Parts, materials, and manufacturing processes selected by the :blue[Mechanical Engineer]")
    selection_df = pd.read_csv('parts_selction.csv')
    selection_df.index = list(range(1, len(selection_df)+1))
    st.dataframe(selection_df, width=3000)
    if st.checkbox("Give Feedback!", key=15):
        feedback_on_mech_1 = st.text_area("", value="Feedback...", 
                                          key=10)
        with open("pm_feedback_mech_1", "w") as f:
            f.write(feedback_on_mech_1)

if st.button("Reset Feedback on Mechanical Engineer for Parts, Materials and Processes", key=20):
    try:
        os.system('rm pm_feedback_mech_1')
    except:
        pass

st.markdown("---")

if path.isfile('parts_material_process_justification.csv'):
    st.markdown("Justifications of the :blue[Mechanical Engineer]")
    just_df = pd.read_csv('parts_material_process_justification.csv')
    just_df.index = list(range(1, len(just_df)+1))
    st.dataframe(just_df, width=3000)
    if st.checkbox("Give Feedback!", key=16):
        feedback_on_mech_2 = st.text_area("", value="Feedback...", 
                                          key=11)
        with open("pm_feedback_mech_2", "w") as f:
            f.write(feedback_on_mech_2)
else:
    st.header("No actions are taken by the :blue[Mechanical Engineer]")

if st.button("Reset Feedback on Mechanical Engineer for Justifications", key=21):
    try:
        os.system('rm pm_feedback_mech_2')
    except:
        pass

st.markdown("---")

if path.isfile('orders.csv'):
    st.header(":blue[Industrial Engineer]")
    st.markdown("Orders by the :blue[Industrial Engineer]")
    orders_df = pd.read_csv('orders.csv')
    orders_df.index = list(range(1, len(orders_df)+1))
    st.dataframe(orders_df, width=3000)
    if st.checkbox("Give Feedback!", key=19):
        feedback_on_ind_1 = st.text_area("", value="Feedback...", 
                                          key=14)
        with open("pm_feedback_ind_1", "w") as f:
            f.write(feedback_on_ind_1)
else:
    st.header("No actions are taken by the :blue[Mechanical Engineer]")

if st.button("Reset Feedback on Industrial Engineer for Demand Forecasting", key=22):
    try:
        os.system('rm pm_feedback_ind_1')
    except:
        pass

st.markdown("---")