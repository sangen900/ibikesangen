import streamlit as st
import numpy as np
import pandas as pd
import os
from os import path


st.set_page_config(page_title='Purchasing Manager')

tab1, tab2 = st.tabs(["Main", "Feedback"])

with tab1:

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

    st.markdown('---')
    vendors = ['GoBike', 'FastBike', 'LazyBiker']
    st.markdown('**:blue[Select Vendor]**')
    vendor = st.selectbox('Vendor',
                        options=vendors,
                        label_visibility='collapsed')
    if vendor == 'GoBike':
        seed = 123
    elif vendor == 'FastBike':
        seed = 321
    else:
        seed = 512
    np.random.seed(seed)
    ordering_cost = np.random.randint(10, 1000, size=(len(parts)))
    holding_cost = np.round(0.05 * ordering_cost, 2)
    annual_demand = np.random.randint(100, 10000, size=(len(parts)))
    distance = np.random.randint(500, 7000)
    lead_time = ((distance / 100) * np.random.uniform(20, 50, size=(len(parts)))) / 24

    eco_df = pd.DataFrame({'Part': parts,
                            'Ordering Cost ($)': ordering_cost,
                            'Annual Demand': annual_demand,
                            'Holding Cost ($)': holding_cost,
                            'Distance (miles)': distance,
                            'Lead Time (Days)': np.round(lead_time, 2)
                            })

    eco_df.index = list(range(1, len(eco_df)+1))
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
        orders['EOQ'] = round(np.sqrt((2*orders["Ordering Cost ($)"]*orders['Annual Demand'])/orders["Holding Cost ($)"]), 3)
        orders.index = list(range(1, len(orders)+1))
        
        st.write('**Orders by the :blue[Industrial Engineer]**')
        st.dataframe(orders, width=3000)

        st.markdown('---')
        total_order_cost = round(orders["Ordering Cost ($)"].sum(),2)
        total_hold_cost = round(orders["Holding Cost ($)"].sum(),2)
        total_ann_demand = orders['Annual Demand'].sum()

        st.write(f'Total Ordering Cost: **:red[${total_order_cost:,}]**')
        st.write(f'Total Holding Cost : **:red[${total_hold_cost:,}]**')
        #st.write(f'Total Annual Demand: **:red[{total_ann_demand:,}]**')
        #st.write(f'**:blue[Economic Order Quantity]: :red[{round(np.sqrt((2*total_order_cost*total_ann_demand)/total_hold_cost), 2):,}]**')
        st.markdown('---')


        if path.isfile('vendors.csv'):
            if st.button('Reset Vendor Selection!'):
                os.system('rm vendors.csv')
                vendor_df = pd.DataFrame(columns=['Part', 'Vendor'])
            else:
                vendor_df = pd.read_csv('vendors.csv')
        else:
            vendor_df = pd.DataFrame(columns=['Part', 'Vendor'])

        st.markdown('**:blue[Select vendor for each part]**')
        ordered_parts = orders.Part.tolist()
        col1, col2 = st.columns(2)
        with col1:
            part_for_vendor = st.selectbox('Part for vendor',
                                            options=['Select Part'] + ordered_parts,
                                            label_visibility='collapsed',)
        with col2:
            vendor_for_part = st.radio('Vendor for part',
                                        options=vendors,
                                        label_visibility='collapsed',)
        
        if part_for_vendor != 'Select Part':
            vendor_df.loc[len(vendor_df), :] = [part_for_vendor, vendor_for_part]
            vendor_df = vendor_df.drop_duplicates(subset='Part', keep='last')
            vendor_df.index = list(range(1, len(vendor_df)+1))
            vendor_df.to_csv('vendors.csv', index=False)

        if len(vendor_df) > 0:
            st.dataframe(vendor_df, width=3000)

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


with tab2:

    # writing
    st.header("Feedback **:red[TO]**")
    st.markdown("---")

    text = ""
    if path.isfile('fb_pum_d.txt'):
        with open('fb_pum_d.txt', 'r') as f:
            text = f.read()
    
    fb_pum_d = st.text_area("Your feedback to the Design Engineer", text)
    if fb_pum_d != "":
        with open("fb_pum_d.txt", "w") as f:
            f.write(fb_pum_d)
        st.markdown("---")

    if st.button('Clear Feedback', key=0):
        if path.isfile('fb_pum_d.txt'):
            os.remove('fb_pum_d.txt')


    st.markdown("---")
    text = ""
    if path.isfile('fb_pum_i.txt'):
        with open('fb_pum_i.txt', 'r') as f:
            text = f.read()

    fb_pum_i = st.text_area("Your feedback to the Industrial Engineer", text)
    if fb_pum_i != "":
        with open("fb_pum_i.txt", "w") as f:
            f.write(fb_pum_i)
        st.markdown("---")

    if st.button('Clear Feedback', key=1):
        if path.isfile('fb_pum_i.txt'):
            os.remove('fb_pum_i.txt')

    
    st.markdown("---")
    text = ""
    if path.isfile('fb_pum_pm.txt'):
        with open('fb_pum_pm.txt', 'r') as f:
            text = f.read()

    fb_pum_pm = st.text_area("Your feedback to the Project Manager", text)
    if fb_pum_pm != "":
        with open("fb_pum_pm.txt", "w") as f:
            f.write(fb_pum_pm)
        st.markdown("---")

    if st.button('Clear Feedback', key=2):
        if path.isfile('fb_pum_pm.txt'):
            os.remove('fb_pum_pm.txt')


    st.markdown("---")
    text = ""
    if path.isfile('fb_pum_m.txt'):
        with open('fb_pum_m.txt', 'r') as f:
            text = f.read()

    fb_pum_m = st.text_area("Your feedback to the Purchasing Manager", text)
    if fb_pum_m != "":
        with open("fb_pum_m.txt", "w") as f:
            f.write(fb_pum_m)
        st.markdown("---")

    if st.button('Clear Feedback', key=3):
        if path.isfile('fb_pum_m.txt'):
            os.remove('fb_pum_m.txt')


    # reading
    st.header("Feedback **:red[From]**")
    if path.isfile('fb_d_pum.txt'):
        st.markdown("---")
        st.write("Feedback from the **:red[Design Engineer]**")
        with open('fb_d_pum.txt', 'r') as f:
            text = f.read()
        st.write(text)
        st.markdown("---")

    if path.isfile('fb_i_pum.txt'):
        st.markdown("---")
        st.write("Feedback from the **:red[Industrial Engineer]**")
        with open('fb_i_pum.txt', 'r') as f:
            text = f.read()
        st.write(text)
        st.markdown("---")


    if path.isfile('fb_pm_m.txt'):
        st.markdown("---")
        st.write("Feedback from the **:red[Project Manager]**")
        with open('fb_pm_m.txt', 'r') as f:
            text = f.read()
        st.write(text)
        st.markdown("---")


    if path.isfile('fb_pum_m.txt'):
        st.markdown("---")
        st.write("Feedback from the **:red[Purchasing Manager]**")
        with open('fb_pum_m.txt', 'r') as f:
            text = f.read()
        st.write(text)
        st.markdown("---")
