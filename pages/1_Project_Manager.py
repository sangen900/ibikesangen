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

if path.isfile('parts_material_process_justification.csv'):
    st.markdown("Justifications of the :blue[Mechanical Engineer]")
    just_df = pd.read_csv('parts_material_process_justification.csv')
    just_df.index = list(range(1, len(just_df)+1))
    st.dataframe(just_df, width=3000)

text = ""
if path.isfile('fb_pm_m.txt'):
    with open('fb_pm_m.txt', 'r') as f:
        text = f.read()

fb_pm_m = st.text_area("Your feedback to the Mechanical Engineer", text)
if fb_pm_m != "":
    with open("fb_pm_m.txt", "w") as f:
        f.write(fb_pm_m)
    st.markdown("---")

if st.button('Clear Feedback', key=0):
    if path.isfile('fb_pm_m.txt'):
        os.remove('fb_pm_m.txt')

if path.isfile('orders.csv'):
    st.header(":blue[Industrial Engineer]")
    st.markdown("Orders by the :blue[Industrial Engineer]")
    orders_df = pd.read_csv('orders.csv')
    orders_df.index = list(range(1, len(orders_df)+1))
    st.dataframe(orders_df, width=3000)

text = ""
if path.isfile('fb_pm_i.txt'):
    with open('fb_pm_i.txt', 'r') as f:
        text = f.read()

fb_pm_i = st.text_area("Your feedback to the Industrial Engineer", text)
if fb_pm_i != "":
    with open("fb_pm_i.txt", "w") as f:
        f.write(fb_pm_i)

if st.button('Clear Feedback', key=1):
    if path.isfile('fb_pm_i.txt'):
        os.remove('fb_pm_i.txt')

st.markdown("---")
text = ""
if path.isfile('fb_pm_pum.txt'):
    with open('fb_pm_pum.txt', 'r') as f:
        text = f.read()

fb_pm_pum = st.text_area("Your feedback to the Purchasing Manager", text)
if fb_pm_pum != "":
    with open("fb_pm_pum.txt", "w") as f:
        f.write(fb_pm_pum)
    st.markdown("---")

if st.button('Clear Feedback', key=2):
    if path.isfile('fb_pm_pum.txt'):
        os.remove('fb_pm_pum.txt')


st.markdown("---")
text = ""
if path.isfile('fb_pm_d.txt'):
    with open('fb_pm_d.txt', 'r') as f:
        text = f.read()

fb_pm_d = st.text_area("Your feedback to the Design Engineer", text)
if fb_pm_d != "":
    with open("fb_pm_d.txt", "w") as f:
        f.write(fb_pm_d)
    st.markdown("---")

if st.button('Clear Feedback', key=3):
    if path.isfile('fb_pm_d.txt'):
        os.remove('fb_pm_d.txt')