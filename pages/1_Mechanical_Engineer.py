import json
import pandas as pd
from os import path
import streamlit as st
import os

st.set_page_config(page_title='Mechanical Engineer')

st.title("Welcome to the Mechanical Engineer Page!")
# st.image('mechanical_avatar.jpg')

st.markdown(
    """
    Your role revolves around selecting the bike **Parts** to manufacture,
    their **Materials**, and the "Manufacturing Processes". You will be given
    each of these in a drop list from which you can make your choices. For each part,
    you will only be shown the most appropriate materials and manufacturing processes.
    """)


if not path.isfile('parts_selction.csv'):
    df = pd.DataFrame(columns=['Part', 'Material', 'Process'])
else:
    df = pd.read_csv('parts_selction.csv')

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

st.markdown('### :blue[Select a part]')
part = st.selectbox(
    label='Part', 
    options=parts,
    label_visibility='collapsed',
)


def make_selections(materials, processes, minimize, maximize):
    st.write('Objectives are:')
    st.write(f'**:red[Minimize:]** {minimize}')
    st.write(f'**:blue[Maximize:]** {maximize}')
    st.markdown('### :blue[Select an appropriate material]')
    material = st.selectbox(
        label="Material",
        options=materials,
        label_visibility='collapsed',
    )
    
    st.markdown('### :blue[Select an appropriate manufacturing process]')
    process = st.selectbox(
        label="Manufacturing Process",
        options=processes,
        label_visibility='collapsed',
    )
    return material, process


if part == 'Frame':
    minimize =  'Weight (Density)'
    maximize = 'Ultimate Tensile Strength'
    materials = ['Selec Material',
                 'Age-hardening Wrought Al-Alloy',
                 'High Carbon Steel',
                 'Low Alloy Steel',
                 'Titanium Alloys',
                 'Wrought Magnesium Alloys'
                 ]
    processes = ['Selec Manufacturing Process',
                 'Forming', 
                 'Drawing', 
                 'Machining', 
                 'Heat Treatment', 
                 'Joining',
                 'Surface Treatment'
                 ]
    material, process = make_selections(materials, processes, minimize, maximize)

elif part == 'Handlebars':
    minimize =  'Price'
    maximize = 'Young’s Modulus'
    materials = ['Selec Material',
                 'Cast Iron - Ductile (Nodular)',
                 'Cast Iron - Gray',
                 'High Carbon Steel',
                 'Low Carbon Steel',
                 'Medium Carbon Steel'
                 ]
    processes = ['Selec Manufacturing Process',
                 'Forming', 
                 'Drawing', 
                 'Machining', 
                 'Extrusion', 
                 'Heat Treatment',
                 'Joining',
                 'Surface Treatment'
                 ]
    material, process = make_selections(materials, processes, minimize, maximize)

elif part == 'Stem':
    minimize =  'Price'
    maximize = 'Compressive Strength'
    materials = ['Selec Material',
                 'Cast Iron - Ductile (Nodular)',
                 'Cast Iron - Gray',
                 'High Carbon Steel',
                 'Low Alloy Steel',
                 'Medium Carbon Steel'
                 ]
    processes = ['Selec Manufacturing Process',
                 'Forming', 
                 'Machining',
                 'Heat Treatment',
                 'Joining',
                 ]
    material, process = make_selections(materials, processes, minimize, maximize)

elif part == 'Suspension Fork':
    minimize =  'Weight (Density)'
    maximize = 'Compressive Strength'
    materials = ['Selec Material',
                 'Boron Carbide',
                 'Silica Glass',
                 'Silicon',
                 'Silicon Carbide',
                 'Silicon Nitride'
                 ]
    processes = ['Selec Manufacturing Process',
                 'Extrusion', 
                 'Reaction Bonding',
                 'Hot Pressing',
                 ]
    material, process = make_selections(materials, processes, minimize, maximize)

elif part == 'Disc Brake Rotor':
    minimize =  'Price'
    maximize = 'Weight (Density)'
    materials = ['Selec Material',
                 'Cast Iron - Ductile (Nodular)',
                 'Cast Iron - Gray',
                 'High Carbon Steel',
                 'Low Alloy Steel',
                 'Low Carbon Steel'
                 ]
    processes = ['Selec Manufacturing Process',
                 'Forming', 
                 'Drawing', 
                 'Machining',
                 'Heat Treatment',
                 'Joining',
                 'Surface Treatment',
                 'Casting'
                 ]
    material, process = make_selections(materials, processes, minimize, maximize)


elif part == 'Tire':
    minimize =  'Weight (Density)'
    maximize = 'Moldability'
    materials = ['Selec Material',
                 'Butyl Rubber (IIR)',
                 'Ethylene Vinyl Acetate (EVA)',
                 'Ionomer (I)',
                 'Natural Rubber (NR)',
                 'Polyethylene'
                 ]
    processes = ['Selec Manufacturing Process',
                 'Polymer Injection Molding', 
                 'Polymer Extrusion', 
                 'Polymer Thermoforming',
                 ]
    material, process = make_selections(materials, processes, minimize, maximize)

elif part == 'Rim':
    minimize =  'Weight (Density)'
    maximize = 'Young’s modulus'
    materials = ['Selec Material',
                 'Alumina',
                 'Aluminium Nitride',
                 'Boron Carbide',
                 'CFRP - Epoxy Matrix (Isotropic)',
                 'Silicon Carbide'
                 ]
    processes = ['Selec Manufacturing Process',
                 'Ring Rolling', 
                 'Casting', 
                 'Forging',
                 ]
    material, process = make_selections(materials, processes, minimize, maximize)

elif part == 'Hub':
    minimize =  'Price'
    maximize = 'Fatigue strength at 10^7 cycles'
    materials = ['Selec Material',
                 'Cast Iron - Ductile (Nodular)',
                 'Cast Iron - Gray',
                 'High Carbon Steel',
                 ]
    processes = ['Selec Manufacturing Process',
                 'Rolling', 
                 'Cold Forging (Closed die)', 
                 'Casting',
                 'Drawing',
                 'Swaging'
                 ]
    material, process = make_selections(materials, processes, minimize, maximize)

elif part == 'Spoke':
    minimize =  'Price'
    maximize = 'Specific stiffness (level3)'
    materials = ['Selec Material',
                 'Cast Iron',
                 'Dolomite',
                 'Jute Fibre',
                 'Kenaf Fibre',
                 'Mica (p)'
                 ]
    processes = ['Selec Manufacturing Process',
                 'Casting', 
                 'Machining'
                 ]
    material, process = make_selections(materials, processes, minimize, maximize)

elif part == 'Pedal':
    minimize =  'Price'
    maximize = 'Ultimate Tensile Strength'
    materials = ['Selec Material',
                 'Cast Iron - Ductile (Nodular)',
                 'Cast Iron - Gray',
                 'High Carbon Steel',
                 'Low Alloy Steel',
                 'Medium Carbon Steel'
                 ]
    processes = ['Selec Manufacturing Process',
                 'Forming', 
                 'Drawing', 
                 'Machining',
                 'Heat Treatment',
                 'Joining',
                 'Surface Treatment'
                 ]
    material, process = make_selections(materials, processes, minimize, maximize)

elif part == 'Crank Arm':
    minimize =  'Weight(Density)'
    maximize = 'Ultimate Tensile Strength'
    materials = ['Selec Material',
                 'Bamboo',
                 'CFRP - Epoxy Matrix',
                 'Low Alloy Steel',
                 'Titanium alloys',
                 'Wrought Magnesium Alloys'
                 ]
    processes = ['Selec Manufacturing Process',
                 'Casting', 
                 'Machining'
                 ]
    material, process = make_selections(materials, processes, minimize, maximize)

elif part == 'Crank Set':
    minimize =  'Weight(Density)'
    maximize = 'Fatigue strength at 10^7 Cycles'
    materials = ['Selec Material',
                 'Boron Carbide',
                 'CFRP - Epoxy Matrix',
                 'Silicon Nitride',
                 'Titanium Alloys',
                 'Wrought Magnesium Alloys'
                 ]
    processes = ['Selec Manufacturing Process',
                 'Casting', 
                 'Machining'
                 ]
    material, process = make_selections(materials, processes, minimize, maximize)

elif part == 'Cassette':
    minimize =  'Weight(Density)'
    maximize = 'Fatigue strength at 10^7 Cycles'
    materials = ['Selec Material',
                 'Butyl Rubber (IIR)',
                 'Ethylene Vinyl',
                 'Acetate (EVA)',
                 'Ionomer(I)',
                 'Natural Rubber (NR)',
                 'Polyethylene (PE)'
                 ]
    processes = ['Selec Manufacturing Process',
                 'Casting', 
                 'Machining'
                 ]
    material, process = make_selections(materials, processes, minimize, maximize)


elif part == 'Chain':
    minimize =  'Price'
    maximize = 'Fatigue strength at 10^7 Cycles'
    materials = ['Selec Material',
                 'Medium carbon steel',
                 'Low carbon steel',
                 'Low alloy steel',
                 'Cast iron - gray',
                 'Cast iron - ductile (nodular)'
                 ]
    processes = ['Selec Manufacturing Process',
                 'Forming', 
                 'Drawing', 
                 'Machining',
                 'Heat Treatment',
                 'Joining',
                 'Surface Treatment'
                 ]
    material, process = make_selections(materials, processes, minimize, maximize)


elif part == 'Seat Post':
    minimize =  'Weight (Density)'
    maximize = 'Compressive Strength'
    materials = ['Selec Material',
                 'Cast Al-Alloys',
                 'Low carbon steel',
                 'Stainless Steel Cast',
                 'Magnesium Alloys',
                 'Low Alloy Steel'
                 ]
    processes = ['Selec Manufacturing Process',
                 'Forming',
                 'Heat Treatment',
                 'Joining',
                 'Surface Treatment'
                 ]
    material, process = make_selections(materials, processes, minimize, maximize)


elif part == 'Seat':
    minimize =  'Weight (Density)'
    maximize = 'Price'
    materials = ['Selec Material',
                 'Polyurethane',
                 'Rigid Polymer',
                 'Foam (HD)',
                 'Rigid Polymer Foam (LD)',
                 'Flexible Polymer Foam (VLD)',
                 'Ceramic Foam'
                 ]
    processes = ['Selec Manufacturing Process',
                 'Injection molding',
                 'Open Die Forging',
                 'Casting'
                 ]
    material, process = make_selections(materials, processes, minimize, maximize)

st.text("")
st.text("")
st.write(
    """
    These are your selections. To make a change, go up :point_up:, select the part and 
    continue the process.
    """)

if st.button('Reset Table'):
    os.system('rm parts_selction.csv')

else:
    try:
        df.loc[len(df)] = [part, material, process]
        df = df.drop_duplicates(subset=['Part'], keep='last')
        df.index = range(1, len(df)+1)
        df.to_csv('parts_selction.csv', index=False)
        st.dataframe(df, width=4000)
    except:
        pass
