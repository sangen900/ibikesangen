import streamlit as st
from streamlit import session_state as ss
from modules import game, group
import numpy as np
import matplotlib.pyplot as plt
import time
from modules import Project_Manager as pr_m, Design_Engineer as d_e, Mechanical_Engineer as m_e, Industrial_Engineer as i_e, Purchasing_Manager as pu_m, mainform as survey

def render():
	if 'setup_complete' not in ss:
		ss['setup_complete'] = False
	if 'order_view' not in ss:
		ss['order_view'] = False
	if not ss.setup_complete:
		init()
	else:
		st.title('iBIKE Simulation')
		st.write('Work with your team members to complete orders!')
		ss.group_state = group.load(ss.group)
		if ss.group_state['status'] != 'completed':
			tab1, tab2, tab3 = st.tabs(["Your Page","Feedback Page","Group Status"])
			with tab1:
				display_role_page()
				display_current_orders()
			with tab2:
				display_feedback_page()
			with tab3:
				display_group_info()
		else:
			display_game_complete()

	#time.sleep(30)
	#st.experimental_rerun()
	#synchronize()

# Callback function that first checks availability and assigns a user to a group if it is not already full.
# if a user is the 5th member of a group, that group will be removed from the available, displayed groups for all other users
def group_assign(group_key):

	group_state = group.load(group_key)
	game_state = game.load()
	groups = game_state['available_groups']
	if group_key not in groups:
		st.write("I'm sorry, the group you chose is full. Please select a different group.")
	else:
		ss.group = group_key
		ss['filepath'] = 'files/data/'+ss.group+'/'
		group_state['player_count'] += 1
		ss['player'] = group_state['player_count']
		if group_state['player_count'] == 5:
			groups.remove(group_key)
			game_state['available_groups'] = groups
			game.save_game_state(game_state)
			group_state['status'] = 'in progress'
		group.save_group_state(group_state)
	
# a function to display the available groups to join based on the current state of the game.
def display_group_buttons():   
    game_state = game.load()
    groups = game_state['available_groups']
    num = len(groups)
    cols = st.columns(num)
    for i in range(num):
        with cols[i]:
            st.button(f"{groups[i]}", on_click=group_assign, args=(groups[i], ))
		
def display_role_page():
	if ss.role == 'Project Manager':
		pr_m.render()
	elif ss.role == 'Design Engineer':
		d_e.render()
	elif ss.role == 'Mechanical Engineer':
		m_e.render()
	elif ss.role == 'Industrial Engineer':
		i_e.render()
	elif ss.role == 'Purchasing Manager':
		pu_m.render()

  
def display_feedback_page():

	if ss.role == 'Project Manager':
		pr_m.feedback()
	elif ss.role == 'Design Engineer':
		d_e.feedback()
	elif ss.role == 'Mechanical Engineer':
		m_e.feedback()
	elif ss.role == 'Industrial Engineer':
		i_e.feedback()
	elif ss.role == 'Purchasing Manager':
		pu_m.feedback()

def display_group_info():

	p_roles = ['p1_role','p2_role','p3_role','p4_role','p5_role']
	p_names = ['p1_name','p2_name','p3_name','p4_name','p5_name']
	
	st.title("Group Information")
	st.write(f"Group Member Count: {ss.group_state['player_count']}")
	st.write(f"Group Status: {ss.group_state['status']}")
	st.write(f"Current Orders: {len(ss.group_state['orders'])}")
	st.write(f"Completed Orders: {len(ss.group_state['completed'])}")
	
	for role in ss.roles:
		name = None
		for p_role in p_roles:
			if role == ss.group_state[p_role]:
				idx = p_roles.index(p_role)
				name = ss.group_state[p_names[idx]]
		if name:
			st.write(role+':  '+name)
		else:
			st.write(role+':  unfilled')


def display_game_complete():
	st.title("The Simulation is Over")
	st.write("Thank you for playing!")

# Callback function to assign text input widget value to session state name variable
def name_assign():
	if len(ss.name_input) > 0:
		ss.name = ss.name_input

def role_assign(role):
	
	group_state = group.load(ss.group)
	roles = group_state['available_roles']
	
	if role not in roles:
		st.write("I'm sorry, the role you chose is already filled. Please select a different role.")
		
	else:
		ss.role = role
		roles.remove(role)
		group_state['available_roles'] = roles
		
		if ss.player == 1:
			group_state['p1_name'] = ss.name
			group_state['p1_role'] = ss.role
		elif ss.player == 2:
			group_state['p2_name'] = ss.name
			group_state['p2_role'] = ss.role
		elif ss.player == 3:
			group_state['p3_name'] = ss.name
			group_state['p3_role'] = ss.role
		elif ss.player == 4:
			group_state['p4_name'] = ss.name
			group_state['p4_role'] = ss.role
		else:
			group_state['p5_name'] = ss.name
			group_state['p5_role'] = ss.role
			
		group.save_group_state(group_state)
		
def display_role_buttons():
    if st.button("Refresh button"):
       st.write("Your page has been refreshed")
    st.write(f"Alright, {ss.name}, you are now in {ss.group}.")
    st.write("Please select one of the available group roles below.")
    st.write("This will be your role for the rest of this session:")

    group_state = group.load(ss.group)
    roles = group_state['available_roles']
    num = len(roles)
    cols = st.columns(num)
    for i in range(num):
        with cols[i]:
            st.button(f"{roles[i]}", on_click=role_assign, args=(roles[i], ))


def init():
	game_state = game.load()
	size = len(game_state['available_groups'])
	if size == 0: 
		st.write("I'm sorry, this simulation is full. Please wait for the next round")
	elif not ss.name:
			st.title('Welcome to the User Page!')
			st.write('On this page, you will choose your group and role.')
			st.text_input('What is your name?', key='name_input' , on_change=name_assign)
	elif not ss.group:
		if st.button('I would like to take the survey'):
		   survey.main_form()
		else:
		   st.write(f"Hello, {ss.name}! Please select one of the available groups below:")
		   display_group_buttons()

	if ss.group and not ss.role:
		display_role_buttons()
		sync_game_settings()

def sync_game_settings():

	game_state = game.load()
	ss.order_limit = game_state['order_limit']
	ss.completed_limit = game_state['completed_limit']
	ss.setup_complete = True

def switch_order_view():
	if ss.order_view == True:
		ss.order_view = False
	else:
		ss.order_view = True

def move_order(order_key):

	idx = ss.roles.index(ss.role)
	# get most up-to-date group state first:
	group_state = group.load(ss.group)
	group_state['orders'][order_key]['checklist'][ss.role] = True
	if idx == 4:
		group_state['completed'][order_key] = group_state['orders'][order_key]
		del group_state['orders'][order_key]
		if len(group_state['completed']) >= ss.completed_limit :
			group_state['status']='completed'
	group.save_group_state(group_state)
	
	
# Function to be called on each user page to display widgets to select orders and pass
# them on to the next role.
def display_current_orders():

	st.write("Click the \"Refresh Orders\" button below in order to refresh your page and view current orders.")
	st.button("Refresh Orders")
	
	if len(ss.group_state['orders']) > 0:

		idx = ss.roles.index(ss.role)
		order_keys = []
		for order_key in ss.group_state['orders'].keys():
			if idx == 0 and not ss.group_state['orders'][order_key]['checklist'][ss.roles[idx]]:
				order_keys.append(order_key)
			elif not ss.group_state['orders'][order_key]['checklist'][ss.roles[idx]] and ss.group_state['orders'][order_key]['checklist'][ss.roles[idx-1]]:
				order_keys.append(order_key)

		if len(order_keys) > 0:
			st.write('Total Number of Unfulfilled Orders: '+str(len(ss.group_state['orders'])))
			st.write('Total Number of Completed Orders: '+str(len(ss.group_state['completed'])))
			col1, col2 = st.columns(2)
			with col1:
				st.radio('Orders Ready for your input:  ', order_keys, key='order_choice')
			with col2:
				st.write('Please select an order for processing:')
				if 'order_choice' in ss:
					st.button("View "+ss.order_choice, on_click=switch_order_view)
					if ss.order_view:
						st.write(ss.group_state['orders'][ss.order_choice])
					idx = ss.roles.index(ss.role)
					if idx < 4:
						button_text = "Send "+ss.order_choice+" to "+ss.roles[idx+1]
					else:
						button_text = "Complete Order"
					st.button(button_text, on_click=move_order, args=(ss.order_choice, ))

		
		else:
			st.write('There are no orders for you to work on right now.')

		display_orders_graph()
		
	else:
		st.write('There are no current customer orders. Please wait for your Project Manager to receive more orders.')




def display_orders_graph():
	data = np.array([0, 0, 0, 0, 0])
	for i in range(5):
		count = 0
		for key in ss.group_state['orders']:
			current = ss.group_state['orders'][key]['checklist'][ss.roles[i]]
			if i == 0 and not current:
				data[i] += 1
			else:
				previous = ss.group_state['orders'][key]['checklist'][ss.roles[i-1]]
				if previous and not current:
					data[i] += 1
						
	inds=range(len(data))
	fig,ax = plt.subplots(figsize=(10,4))
	rects = ax.bar(inds, data, width=0.5)
	ax.set_xticks([ind for ind in inds])
	ax.set_xticklabels(ss.roles)

	plt.xticks(rotation=60, ha="right")
	plt.title("Current Orders Distribution")
	ax.set_ylabel("Orders Waiting for Processing")
	st.pyplot(fig)

# I need a different way to automatically synchronize the group state for group members. This is causing issues with widget interaction with the rest of my code and I don't know why.
def synchronize():
	while True:
		time.sleep(5)
		group_state = group.load(ss.group)
		if group_state != ss.group_state:
			st.experimental_rerun()
