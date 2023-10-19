import streamlit as st

# Import your form functions here with the dot prefix.
from .form0 import form_0
from .form1 import form_1
from .form2 import form_2
from .form3 import form_3
from .form4 import form_4
from .form5 import form_5
from .form6 import form_6
from .form7 import form_7
from .form8 import form_8
from .form9 import form_9
from .form10 import form_10
from .form11 import form_11
from .form12 import form_12
from .form13 import form_13

# Create a dictionary to track form submission status
form_submission_status = {
    "form0": False,
    "form1": False,
    "form2": False,
    "form3": False,
    "form4": False,
    "form5": False,
    "form6": False,
    "form7": False,
    "form8": False,
    "form9": False,
    "form10": False,
    "form11": False,
    "form12": False,
    "form13": False,
}

def main_form():
    form_functions = {
        "form0": form_0,
        "form1": form_1,
        "form2": form_2,
        "form3": form_3,
        "form4": form_4,
        "form5": form_5,
        "form6": form_6,
        "form7": form_7,
        "form8": form_8,
        "form9": form_9,
        "form10": form_10,
        "form11": form_11,
        "form12": form_12,
        "form13": form_13
    }
    
    user_selected_page = st.sidebar.radio("Please read the form carefully and fill the below form.", list(form_functions.keys()))

    # Check if the form has been submitted successfully
    if user_selected_page in form_submission_status and form_submission_status[user_selected_page]:
        st.sidebar.markdown(f"**{user_selected_page} (Completed)**")
    else:
        st.sidebar.radio(user_selected_page, list(form_functions.keys()))

    # Call the selected form function
    form_functions.get(user_selected_page, lambda: st.write("Select a form from the sidebar."))()

    # Check if the form was submitted and update the status
    if st.form_submit_button("Submit Form"):
        if user_selected_page in form_submission_status:
            form_submission_status[user_selected_page] = True

if __name__ == "__main__":
    main_form()
