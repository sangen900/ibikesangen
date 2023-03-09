import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from os import path

st.set_page_config(page_title='Industrial Engineer')

st.title("Welcome to the Industrial Engineer Page!")

tab1, tab2, tab3 = st.tabs(["Welcome", "Demand Forecasting", "Product and Layout Design"])

with tab1:
    st.markdown(
        """
        Your role revolves around two main points. First, you will forecast the demand and order the 
        appropriate quantities based on that. For this task, you will be given a drop list for all the
        bike parts. You will also be provided with the quatities of each part per bike. Moreover, you will
        be shown the demand for the last 12 months for each part you expand and will be shown a line graph 
        encompassing the demand, the inventory level, and the moving average demand for the last 12 months. 
        We also provide you with an initial value that you can use for your prdiction. The initial value is
        average demand minus the current invetory.

        For the second task, you are will make a design for each part of the bike taking into account
        the design itself and the dynamic model to analyze the behavior of the bike and optimize the design.
        For the first task, you can use softwares such as [Autodesk](https://www.autodesk.com/),and for the
        second task, you can use [Matlab/Simulink](https://www.mathworks.com/products/matlab.html) or any
        other software. In your tab, you will find two browsing links to upload your work. 
        """)


def forecasting(seed):
    np.random.seed(seed)
    with st.expander('See last N-month demand and invetory'):
        size = st.slider("Period of Visualization (Months)", 1, 12, 12)
        readings = np.random.randint(50, 400, size=(size,))
        in_stock = np.random.randint(50, 400, size=(size,))
        mean = np.mean(np.float32(readings))
        suggested_order = mean - np.float32(in_stock[-1])
        time = list(range(1-size, 1))
        fig, ax = plt.subplots(2, 1)
        fig.figsize = (6, 6)
        ax[0].plot(time, readings)
        ax[0].axhline(y=mean, c='r', linestyle='--')
        ax[0].plot(time, in_stock)
        ax[0].legend(['Demand', 'Mean Demand', 'Invetory'])
        ax[0].grid()
        ax[0].set_xlabel('')
        ax[0].set_ylabel('Quantity')
        ax[0].set_title(f'Last {size}-Month Demand and Invetory')
        ax[0].set_xticks(time)

        ax[1].bar(time, readings, alpha=0.5)
        ax[1].axhline(y=mean, c='red', linestyle='--')
        ax[1].bar(time, in_stock, alpha=0.5)
        ax[1].set_xlabel('Month')
        ax[1].set_ylabel('Quantity')
        ax[1].legend(['Demand', 'Mean Demand', 'Invetory'])
        st.pyplot(fig)
    return suggested_order
        

with tab2:

    st.title(':blue[Demand Forecasting]')

    st.markdown("""
    In this role, you will forecast the demand and order the 
    appropriate quantities based on that. For this task, you will be given a drop list for all the
    bike parts. You will also be provided with the quatities of each part per bike. Moreover, you will
    be shown the demand for the last 12 months for each part you expand and will be shown a line graph 
    encompassing the demand, the inventory level, and the moving average demand for the last 12 months. 
    We also provide you with an initial value that you can use for your prdiction. The initial value is
    average demand minus the current invetory. 
    """)

    st.markdown('#### :blue[Select Bike Parts to Order]')
    st.markdown("""
                You can do this sequentially. Each time you can select one part, then define the
                order quatity.
                """)

    parts = ['Select Part',
            'Frame',
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
    lead_times = np.random.randint(7, 120, size=len(parts))
    

    # if st.checkbox('Tires'):

    part = st.selectbox(
                        label='Part', 
                        options=parts,
                        label_visibility='collapsed',
                        )
    
    if part != "Select Part":
        np.random.seed(123)
        seeds = np.random.randint(1, 1000, size=(len(parts),))
        idx = parts.index(part)

        st.text('')

        st.markdown(f"#### :blue[Lead time is (Days):] :red[{lead_times[idx]}]")
        seed = seeds[idx]

        st.text('')

        suggested_order = forecasting(seed)
        if suggested_order > 0:
            qty = int(suggested_order)
        else:
            qty = 0

        st.text('')
        st.markdown('#### :blue[Choose the order quantity]')
        st.markdown('The initial value given below is calculated as follows:')
        st.latex('Order = Mean~Demand - Current~Invetory')
        order_qty = st.number_input('Quantity (The initial value is = mean demand - invetory)', 
                                    label_visibility='collapsed',
                                    value=qty, key=0, min_value=0)

        if not path.isfile('orders.csv'):
            orders_df = pd.DataFrame(columns=['Part', 'Qty'])

        else:
            orders_df = pd.read_csv('orders.csv')

        if st.button('Reset Table'):
            os.system('rm orders.csv')
        else:
            try:
                orders_df.loc[len(orders_df)] = [part, order_qty]
                orders_df = orders_df.drop_duplicates(subset=['Part'], keep='last')
                orders_df.index = range(1, len(orders_df)+1)
                orders_df.to_csv('orders.csv', index=False)
                st.text('')
                st.text('')
                st.text('')
                st.write('### Your ordered parts and quantities')
                orders_df.index = list(range(1, len(orders_df)+1))
                st.dataframe(orders_df,
                            width=3000)
                orders_df.to_csv('orders.csv', index=False)
            except:
                pass


with tab3:

    st.markdown("""
    In this role, you are will make a design for each part of the bike taking into account
        the design itself and the dynamic model to analyze the behavior of the bike and optimize the design.
        For the first task, you can use softwares such as [Autodesk](https://www.autodesk.com/),and for the
        second task, you can use [Matlab/Simulink](https://www.mathworks.com/products/matlab.html) or any
        other software. In your tab, you will find two browsing links to upload your work.
    """)

    st.text('')
    st.text('')
    st.text('')
    col1, col2 = st.columns(2)
    with col1:
        st.file_uploader("Upload your bike design")
    with col2:
        st.file_uploader("Upload your plant layout")