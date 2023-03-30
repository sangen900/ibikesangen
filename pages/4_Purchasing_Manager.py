import streamlit as st
import numpy as np
import pandas as pd
from os import path


st.set_page_config(page_title='Purchasing Manager')

st.title("Welcome to the Purchasing Manager Page!")

st.markdown(
    """
    Your role revolves around monitoring the order quantities made by the :blue[Industrial Engineer], 
    the annual demand, the ordering cost, and the holding cost. The :red[Economic Order Quantity (EOQ)] will
    be calculated for you, and your task will be to give feedback to the :blue[Industrial Engineer] on their
    performance.
    """)


parts = ['Frame',
         'Handlebars',
         'Stem',
         'Suspension Fork',
         'Disc Brake Rotor',
         'Tire',
         'Rim',
         'Hub',
         'Spoke',
         'Pedal',
         'Crank Arm',
         'Crank Set',
         'Cassette',
         'Chain',
         'Seat Post',
         'Seat',
         ]

np.random.seed(123)
ordering_cost = np.random.randint(10, 1000, size=(len(parts)))
holding_cost = np.round(0.05 * ordering_cost, 2)
annual_demand = np.random.randint(100, 10000, size=(len(parts)))

eco_df = pd.DataFrame({'Part': parts,
                        'Ordering Cost ($)': ordering_cost,
                        'Annual Demand': annual_demand,
                        'Holding Cost ($)': holding_cost,
                        })

eco_df.index = list(range(1, len(eco_df)+1))
st.markdown('---')
st.write('')
with st.expander('Expand to see the part economics table'):
    st.write('**:blue[Part Economics Table]**')
    st.dataframe(eco_df, width=3000)

st.markdown('---')
st.write('')
if path.isfile('orders.csv'):
    orders = pd.read_csv('orders.csv')
    orders.index = list(range(1, len(orders)+1))
    orders = orders.merge(eco_df, on='Part', how='left')
    orders['Ordering Cost ($)'] *= orders['Qty']
    orders['Holding Cost ($)'] *= orders['Qty']

    st.write('**Orders by the :blue[Industrial Engineer]**')
    st.dataframe(orders, width=3000)

    st.markdown('---')
    total_order_cost = round(orders["Ordering Cost ($)"].sum(),2)
    total_hold_cost = round(orders["Holding Cost ($)"].sum(),2)
    total_ann_demand = orders['Annual Demand'].sum()

    st.write(f'Total Ordering Cost: **:red[${total_order_cost:,}]**')
    st.write(f'Total Holding Cost : **:red[${total_hold_cost:,}]**')
    st.write(f'Total Annual Demand: **:red[{total_ann_demand:,}]**')
    st.write(f'**:blue[Economic Order Quantity]: :red[{round(np.sqrt((2*total_order_cost*total_ann_demand)/total_hold_cost), 2):,}]**')
    st.markdown('---')

    with st.expander('Give Feedback!'):
        if path.isfile('purchasing_manager_feedback'):
            with open('purchasing_manager_feedback', 'rb') as f:
                previous_feedback = f.read().decode()
            feedback = st.text_area('feedback ...',
                                    value=previous_feedback,
                                    label_visibility='collapsed')
            
        else:
            feedback = st.text_area('feedback ...',
                                    value='Your feedback...',
                                    label_visibility='collapsed')
        with open('purchasing_manager_feedback', 'w') as f:
            f.write(feedback)
