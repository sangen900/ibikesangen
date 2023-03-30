import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from os import path
import seaborn as sns

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
    
    st.text("")
    st.text("")

    cond = False
    try:
        if path.isfile('parts_selction.csv'):
            st.markdown("---")
            st.markdown("### Parts selected by the :blue[Mechanical Engineer] with justifications")
        selection_df = pd.read_csv('parts_selction.csv')
        st.dataframe(selection_df, width=6000)
        cond = True
    except:
        pass

    try:
        justification_df = pd.read_csv('parts_material_process_justification.csv')
        st.dataframe(justification_df, width=6000)
    except:
        pass

    
    if cond:
        st.text("")
        st.text("")
        st.markdown("---")

        if not path.isfile('material_feedback.csv'):
            material_feedback_df = pd.DataFrame(columns=['Part', 'Feedback'])
        else:
            material_feedback_df = pd.read_csv('material_feedback.csv')

        st.markdown("### :blue[Your feedback on material]")
        part = st.selectbox("Select a part to give feedback",
                        options=['Select part'] + selection_df.Part.tolist(),
                        key=1)
                        #label_visibility='collapsed')
        if part != 'Select part':
            feedback = st.text_area(label='',
                                    value='Your feedback', 
                                    key=2)
            material_feedback_df.loc[len(material_feedback_df)] = [part, feedback]
            material_feedback_df = material_feedback_df.drop_duplicates(subset=['Part'], keep='last')
            material_feedback_df.index = range(1, len(material_feedback_df)+1)
            material_feedback_df.to_csv('material_feedback.csv', index=False)

            if st.button('Reset Table', key=6):
                os.system('rm material_feedback.csv')
            else:
                st.dataframe(material_feedback_df, width=3000)

        
        st.text("")
        st.text("")
        st.markdown("---")

        if not path.isfile('process_feedback.csv'):
            process_feedback_df = pd.DataFrame(columns=['Part', 'Feedback'])
        else:
            process_feedback_df = pd.read_csv('process_feedback.csv')

        st.markdown("### :blue[Your feedback on manufacturing process]")
        part = st.selectbox("Select a part to give feedback",
                        options=['Select part'] + selection_df.Part.tolist(),
                        key=3)
                        #label_visibility='collapsed')
        if part != 'Select part':
            feedback = st.text_area(label='',
                                    value='Your feedback',
                                    key=4)
            process_feedback_df.loc[len(process_feedback_df)] = [part, feedback]
            process_feedback_df = process_feedback_df.drop_duplicates(subset=['Part'], keep='last')
            process_feedback_df.index = range(1, len(process_feedback_df)+1)
            process_feedback_df.to_csv('process_feedback.csv', index=False)

            if st.button('Reset Table', key=7):
                os.system('rm process_feedback.csv')

            else:
                st.dataframe(process_feedback_df, width=3000)
        st.markdown("---")

    if path.isfile('pm_feedback_ind_1'):
        st.markdown("""
                    Here is the feedback by the :red[Project Manager] on the order quantities""")
        with open ('pm_feedback_ind_1', 'rb') as f:
            text = f.read().decode()
        with st.expander("Expand to see feedback!"):
            st.markdown(f":red[{text}]")
        st.markdown("---")

    if path.isfile('purchasing_manager_feedback'):
        st.markdown("""
                    Here is the feedback by the :red[Purchasing Manager] on the order quantities""")
        with open('purchasing_manager_feedback', 'rb') as f:
            purch_manager_feedback = f.read().decode()
        with st.expander('Expand to see feedback'):
            st.markdown(f":red[{purch_manager_feedback}]")
        st.markdown("---")


def forecasting(seed):
    st.markdown("---")
    np.random.seed(seed)
    with st.expander('See last N-month demand and invetory'):
        size = st.slider("Period of Visualization (Months)", 1, 12, 12)
        readings = np.random.randint(50, 400, size=(size,))
        in_stock = np.random.randint(50, 400, size=(size,))
        mean = np.mean(np.float32(readings))
        suggested_order = mean - np.float32(in_stock[-1])
        time = list(range(1-size, 1))
        fig, ax = plt.subplots()
        fig.figsize = (12, 6)

        data1 = pd.DataFrame({'Month':time,
                            'Reading': in_stock, # inventory
                            })
        data2 = pd.DataFrame({'Month':time,
                            'Reading': readings, # demand
                            })

        data = pd.concat([data1, data2], axis=0)
        data['Type'] = ['Inventory']*(len(data)//2) + ['Demand']*(len(data)//2)

        sns.barplot(data=data, x='Month', y='Reading', hue='Type', ax=ax, alpha=0.7)
        ax.axhline(y=mean, c='red', linestyle='--')
        st.pyplot(fig)
        st.markdown("---")
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
    
    st.markdown("---")
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
    
    col1, col2 = st.columns(2)

    with col1:
        part = st.selectbox(
                            label='Part', 
                            options=parts,
                            label_visibility='collapsed',
                            key=5,
                            )
    
    if part != "Select Part":
        np.random.seed(123)
        seeds = np.random.randint(1, 1000, size=(len(parts),))
        idx = parts.index(part)

        with col2:
            st.markdown(f":blue[Lead time is (Days):] :red[{lead_times[idx]}]")
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
                                    value=qty, min_value=0)
        st.markdown("---")

        if not path.isfile('orders.csv'):
            orders_df = pd.DataFrame(columns=['Part', 'Qty'])

        else:
            orders_df = pd.read_csv('orders.csv')

        if st.button('Reset Table', key=8):
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