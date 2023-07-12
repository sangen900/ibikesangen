import streamlit as st
from streamlit import session_state as ss
from modules import game, group
import time

def game_reset():
	dirpath = 'files/data'
	shutil.rmtree(dirpath)
	os.mkdir(dirpath)
	for key in ss.keys():
		del ss[key]

# main function to render the instructor game setup and dashboard			
def render():

	if 'setup_complete' not in ss:
		ss['setup_complete'] = False

	if not ss.setup_complete:
		st.title('iBIKE Game Setup')
		st.markdown('On this page, you will specify the number of student groups participating in your game. Each group must have 5 (and no more than 5) students. You will be able to monitor the groups\' progress, and at the end of the game download each group\'s data.')
		init()

	st.button("GAME RESET", on_click=game_reset)

	if ss.setup_complete:
		dashboard()

# Callback function to assign text input widget value to session state name variable
def name_assign():
	if len(ss.name_input) > 0:
		ss.name = ss.name_input

# Callback function to generate group_state and game_state files to manage the game
#	and to flag the game setup as complete.
def game_state_assign():
	try:
		group_num = int(ss.group_num_input)
	except:
		st.write('please enter an integer between 1 and 10 for your group number')
	else:
		game_state = game.init(ss.name, group_num)
		ss.game_state = game_state

def init():
	# function for instructor setup. Includes setting the instructor name and number of groups.
	if not ss.name:
		st.text_input('What is your name?', key='name_input' , on_change=name_assign)

	elif not ss.game_state:
		group_num = st.text_input('How many student groups do you have?', key='group_num_input', on_change=game_state_assign)

	elif not ss.setup_complete:
		st.write("Please specify the limit of concurrent, unfulfilled customer orders that you would like to allow, along with the total number of fulfilled orders required to complete the game. When you done, click \'Complete Setup\' below.'")
		st.slider("Concurrent Unfulfilled Order Limit",min_value=0,max_value=100,value=25,step=5,key='order_limit_input')
		st.slider("Fulfilled Orders Required to Complete the Game",min_value=0,max_value=500,value=100,step=10,key='completed_limit_input')
		st.button("Complete Setup", on_click=complete_game_setup)

def complete_game_setup():
	game_state = game.load()
	ss.order_limit = ss.order_limit_input
	game_state['order_limit'] = ss.order_limit_input
	ss.completed_limit = ss.completed_limit_input
	game_state['completed_limit'] = ss.completed_limit_input
	game.save_game_state(game_state)
	ss.setup_complete = True

def display_groups():
	
	game_state = game.load()
	groups = game_state['groups']
	num = len(groups)
	cols = st.columns(num, gap='large')

	p_roles = ['p1_role','p2_role','p3_role','p4_role','p5_role']
	p_names = ['p1_name','p2_name','p3_name','p4_name','p5_name']
	for i in range(num):
		group_state = group.load(groups[i])
		with cols[i]:
			st.write("GROUP "+str(i+1))
			st.write(f"Player Count: {group_state['player_count']}")
			st.write(f"Group Status: {group_state['status']}")
			st.write(f"Current Orders: {len(group_state['orders'])}")
			st.write(f"Completed Orders: {len(group_state['completed'])}")
			for role in ss.roles:
				name = None
				for p_role in p_roles:
					if role == group_state[p_role]:
						idx = p_roles.index(p_role)
						name = group_state[p_names[idx]]
				if name:
					st.write(role+':  '+name)
				else:
					st.write(role+':  unfilled')
	
def dashboard():
	# function to, upon setup completion, display the instructor dashboard for the rest of the game.
	st.title('iBIKE Instructor Dashboard')
	st.write(f'Instructor name:  {ss.name}')
	st.write(f"Number of student groups: {ss.game_state['group_num']}")
	display_groups()
	time.sleep(5)
	st.experimental_rerun()


