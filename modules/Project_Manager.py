import streamlit as st
import numpy as np
import pandas as pd
from os import path
import os
from streamlit import session_state as ss
from modules import order, group
from enum import Enum
from shutil import make_archive

class ReportState(Enum):
	INACTIVE = 1
	CONFIRMING = 2
	GENERATING = 3
	FINISHED = 4
	INVALID = 5

def render():
	
	st.title('Project Manager')
	st.markdown(
	        """
	        Your role is to generate customer orders, monitor the progress of your team members, delegate tasks, and provide constructive feedback.
	        """)
	if 'order_requested' not in ss:
		ss['orders_requested'] = False
	if 'display_orders' not in ss:
		ss['display_orders'] = False
	if 'orders_full' not in ss:
		ss['orders_full'] = False

	st.markdown("Specify the number of orders you would like to place using the slider, and then click \"Generate Customer Orders")

	col1, col2 = st.columns([1, 2])

	with col1:
		
		order_request = st.button('Generate Customer Orders',on_click=create_orders)
		
		if ss.orders_requested:
			st.write(f"{ss.orders_created} orders have been recieved. There are {len(ss.group_state['orders'])} ongoing orders. Click on 'View/Hide Orders' to see order details.")
			
		if ss.orders_full:
			st.write(f"WARNING: That number of incomming orders will exceed the current limit of {ss.order_limit} ongoing customer orders. Select a smaller number of orders.")
			
	with col2:
		
		num_requested = st.slider('Select the number of orders you would like to generate:', key="num_orders", min_value=1, max_value=ss.order_limit, value=1)

	if 'report_status' not in ss:
    		ss.report_status = ReportState.INACTIVE

	#this is checked up here so that clicking "Refresh" will immediately show if the report is eady
	if(ss.report_status == ReportState.GENERATING):
		check_report()
	
	st.write(f"As Project Manager, you can report your progress to the instructor by creating a downloadable report.")
	#report button
	if(ss.report_status == ReportState.INACTIVE):
		st.button('Create Report', on_click=advance_state)
	elif(ss.report_status == ReportState.CONFIRMING):
		st.button('Cancel Report', on_click=reset_state)
	elif(ss.report_status == ReportState.GENERATING):
		st.button('Refresh') #this button doesn't really do anything, but clicking it will cause the check_report to be run again
	elif(ss.report_status == ReportState.FINISHED):
		st.button('Close Report', on_click=advance_state)
	else:
		print('State Error - Button') #this should never be reached unless an error occurs

	#revealed items that appear once the button is clicked for the first time
	if(ss.report_status != ReportState.INACTIVE):
		if(ss.report_status == ReportState.CONFIRMING):
			st.write(f"Are you sure you want to make a report? You can continue playing, but your additional progress will not be reflected in the report.")
			st.button('Confirm', on_click=generate_report) #this function call will advance the state
		elif(ss.report_status == ReportState.GENERATING):
			st.write(f"Input confirmed, generating...")			
		elif(ss.report_status == ReportState.FINISHED):
			st.write(f"Report generated successfully. You may now close this report.")
		else:
			print('State Error - Revealed Area') #this also should never be reached unless an error occurs
	
	if path.isfile(ss.filepath+'parts_selction.csv'):
	    st.header(":blue[Mechanical Engineer]")
	    st.markdown("Parts, materials, and manufacturing processes selected by the :blue[Mechanical Engineer]")
	    selection_df = pd.read_csv(ss.filepath+'parts_selction.csv')
	    selection_df.index = list(range(1, len(selection_df)+1))
	    st.dataframe(selection_df, width=3000)
	
	if path.isfile(ss.filepath+'parts_material_process_justification.csv'):
	    st.markdown("Justifications of the :blue[Mechanical Engineer]")
	    just_df = pd.read_csv(ss.filepath+'parts_material_process_justification.csv')
	    just_df.index = list(range(1, len(just_df)+1))
	    st.dataframe(just_df, width=3000)
	
def feedback():
	st.header("Feedback **:red[TO]**")
	st.markdown("---")
	
	text = ""
	if path.isfile(ss.filepath+'fb_pm_m.txt'):
	    with open(ss.filepath+'fb_pm_m.txt', 'r') as f:
	        text = f.read()
	
	fb_pm_m = st.text_area("Your feedback to the Mechanical Engineer", text)
	if fb_pm_m != "":
	    with open(ss.filepath+"fb_pm_m.txt", "w") as f:
	        f.write(fb_pm_m)
	    st.markdown("---")
	
	if st.button('Clear Feedback', key=0):
	    if path.isfile(ss.filepath+'fb_pm_m.txt'):
	        os.remove(ss.filepath+'fb_pm_m.txt')
	
	if path.isfile(ss.filepath+'orders.csv'):
	    st.header(":blue[Industrial Engineer]")
	    st.markdown("Orders by the :blue[Industrial Engineer]")
	    orders_df = pd.read_csv(ss.filepath+'orders.csv')
	    orders_df.index = list(range(1, len(orders_df)+1))
	    st.dataframe(orders_df, width=3000)
	
	text = ""
	if path.isfile(ss.filepath+'fb_pm_i.txt'):
	    with open(ss.filepath+'fb_pm_i.txt', 'r') as f:
	        text = f.read()
	
	fb_pm_i = st.text_area("Your feedback to the Industrial Engineer", text)
	if fb_pm_i != "":
	    with open(ss.filepath+"fb_pm_i.txt", "w") as f:
	        f.write(fb_pm_i)
	
	if st.button('Clear Feedback', key=1):
	    if path.isfile(ss.filepath+'fb_pm_i.txt'):
	        os.remove(ss.filepath+'fb_pm_i.txt')
	
	st.markdown("---")
	text = ""
	if path.isfile(ss.filepath+'fb_pm_pum.txt'):
	    with open(ss.filepath+'fb_pm_pum.txt', 'r') as f:
	        text = f.read()
	
	fb_pm_pum = st.text_area("Your feedback to the Purchasing Manager", text)
	if fb_pm_pum != "":
	    with open(ss.filepath+"fb_pm_pum.txt", "w") as f:
	        f.write(fb_pm_pum)
	    st.markdown("---")
	
	if st.button('Clear Feedback', key=2):
	    if path.isfile(ss.filepath+'fb_pm_pum.txt'):
	        os.remove(ss.filepath+'fb_pm_pum.txt')
	
	
	st.markdown("---")
	text = ""
	if path.isfile(ss.filepath+'fb_pm_d.txt'):
	    with open(ss.filepath+'fb_pm_d.txt', 'r') as f:
	        text = f.read()
	
	fb_pm_d = st.text_area("Your feedback to the Design Engineer", text)
	if fb_pm_d != "":
	    with open(ss.filepath+"fb_pm_d.txt", "w") as f:
	        f.write(fb_pm_d)
	    st.markdown("---")
	
	if st.button('Clear Feedback', key=3):
	    if path.isfile(ss.filepath+'fb_pm_d.txt'):
	        os.remove(ss.filepath+'fb_pm_d.txt')


	# reading
	st.header("Feedback **:red[From]**")
	if path.isfile(ss.filepath+'fb_d_pm.txt'):
		st.markdown("---")
		st.write("Feedback from the **:red[Design Engineer]**")
		with open(ss.filepath+'fb_d_pm.txt', 'r') as f:
			text = f.read()
		st.write(text)
		st.markdown("---")

	if path.isfile(ss.filepath+'fb_i_pm.txt'):
		st.markdown("---")
		st.write("Feedback from the **:red[Industrial Engineer]**")
		with open(ss.filepath+'fb_i_pm.txt', 'r') as f:
			text = f.read()
		st.write(text)
		st.markdown("---")


	if path.isfile(ss.filepath+'fb_m_pm.txt'):
		st.markdown("---")
		st.write("Feedback from the **:red[Mechanical Engineer]**")
		with open(ss.filepath+'fb_m_pm.txt', 'r') as f:
			text = f.read()
		st.write(text)
		st.markdown("---")


	if path.isfile(ss.filepath+'fb_pum_pm.txt'):
		st.markdown("---")
		st.write("Feedback from the **:red[Purchasing Manager]**")
		with open(ss.filepath+'fb_pum_pm.txt', 'r') as f:
			text = f.read()
		st.write(text)
		st.markdown("---")

def create_orders():
		
	if len(ss.group_state['orders']) + ss.num_orders <= ss.order_limit:
		for i in range(ss.num_orders):
			group.add_new_order(ss.group)
		ss.orders_requested = True
		ss.orders_full = False
		ss['orders_created'] = ss.num_orders
	else:
		ss.orders_requested = False
		ss.orders_full = True
	
def switch_orders_display():
	if ss.display_orders == True:
		ss.display_orders = False
	else:
		ss.display_orders = True

def advance_state():
	ss.report_status = ReportState(ss.report_status.value + 1)
	if (ss.report_status.value > 4):
		reset_state()

def reset_state():
	ss.report_status = ReportState(1)

def generate_report():
	group_state = group.load(ss.group_state.get('group_key'))
	#setting this boolean array to all false prompts the other roles to create heir files for the report
	for i in range(4):
		(group_state['roles_reported'])[i] = False
	group.save_group_state(group_state)
	
	advance_state()

def check_report():
	#all other roles must do their render function so that we have the info for the zip file, so that is checked here
	group_state = group.load(ss.group_state.get('group_key'))
	submission_count = 0

	#checking how many players have submitted
	for i in range(4):
		if((group_state['roles_reported'])[i] == True):
			submission_count += 1

	if(submission_count == group_state['player_count'] - 1):
		#resetting boolean array so that new players who join don't try to submit a report
		if(group_state['player_count'] < 4):
			for i in range(4):
				(group_state['roles_reported'])[i] = True

		#making the zip file if there is at least one other player
		if(group_state['player_count'] > 1):
			make_archive(ss.group_state.get('group_key')+'_report', 'zip', ss.filepath, 'report')
		advance_state()
