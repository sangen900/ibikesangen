import streamlit as st

# Import your form modules
import form_0
import form_1
import form_2
import form_3
import form_4
import form_5
import form_6
import form_7
import form_8
import form_9
import form_10
import form_11
import form_12
import form_13

def render():
    # Check if "page_index" exists in session state, and initialize it to 0 if not present
    if "page_index" not in st.session_state:
        st.session_state.page_index = 0
    
    # List of form rendering functions
    pages = [
        form_0.render,
        form_1.render,
        form_2.render,
        form_3.render,
        form_4.render,
        form_5.render,
        form_6.render,
        form_7.render,
        form_8.render,
        form_9.render,
        form_10.render,
        form_11.render,
        form_12.render,
        form_13.render,
    ]
    
    # Render the current form based on the page_index
    pages[st.session_state.page_index]()

    # Create columns for navigation buttons
    col1, col3 = st.columns([1, 1])
    
    # Previous button logic
    if col1.button("Previous", key="prev_button") and st.session_state.page_index > 0:
        st.session_state.page_index -= 1
    
    # Next button logic
    if col3.button("Next", key="next_button", disabled=st.session_state.page_index == len(pages) - 1):
        st.session_state.page_index += 1
        st.session_state.page_index = max(0, min(st.session_state.page_index, len(pages) - 1))

# # Streamlit app title
# st.title("Form Navigation")

# # Call the main_form() function when the Streamlit app is run
# main_form()
