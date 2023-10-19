import streamlit as st

# Import your form functions here without the dot prefix.
from form0 import form_0
from form1 import form_1
from form2 import form_2
from form3 import form_3
from form4 import form_4
from form5 import form_5
from form6 import form_6
from form7 import form_7
from form8 import form_8
from form9 import form_9
from form10 import form_10
from form11 import form_11
from form12 import form_12
from form13 import form_13

def main_form():
    page_names = ["form0", "form1", "form2", "form3", "form4", "form5", "form6", "form7", "form8", "form9", "form10", "form11", "form12", "form13"]
    form_status = {page: False for page in page_names}
    
    # Create checkboxes in the sidebar for each form
    for page in page_names:
        form_status[page] = st.sidebar.checkbox(f"{page} Completed", key=page)
    
    user_selected_page = st.sidebar.radio("Please read the form carefully and fill the below form.", page_names)
    
    # Display the form corresponding to the selected page
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

    if user_selected_page in form_functions:
        form_functions[user_selected_page]()

    # Show success message when the user manually checks the form as completed
    if form_status[user_selected_page]:
        st.success(f"{user_selected_page} marked as completed!")

if __name__ == "__main__":
    main_form()
