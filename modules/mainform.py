import streamlit as st
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

def main_form():
    if "form_statuses" not in st.session_state:
        st.session_state.form_statuses = {
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
    
    form_names = {
        "form0": "Starting Form",
        "form1": "Consent Form",
        "form2": "Basic Information Form",
        "form3": "Manufacturing Knowledge Form",
        "form4": "Defining Manufacturing Terms Form",
        "form5": "YouTube Video 1 Form",
        "form6": "Agreement Form",
        "form7": "iBike Part 1 Form",
        "form8": "YouTube Video 2 Form",
        "form9": "iBike Part 2 Form",
        "form10": "YouTube Video 3 Form",
        "form11": "iBike Part 3 Form",
        "form12": "Manufacturing Form",
        "form13": "Ending Form",
    }

    # Always display the sidebar
    st.sidebar.header("Please read the form carefully and fill in the below form.")

    # Sidebar menu with radio buttons
    form_statuses = st.session_state.form_statuses
    user_selected_page = st.sidebar.radio("Select a form", list(form_statuses.keys()), format_func=lambda x: form_names[x])

    # Forms to exclude from status bar updates
    forms_to_exclude = ["form0", "form3", "form5", "form8", "form10", "form13"]

    # Update the status of the selected form if it's not excluded
    if user_selected_page not in forms_to_exclude:
        matching_keys = [key for key, value in form_names.items() if value == user_selected_page]
        current_form_key = matching_keys[0] if matching_keys else None

        if current_form_key == "form1":
            if form_1():
                form_statuses["form1"] = True  # Mark form as completed
        elif current_form_key == "form2":
            if form_2():
                form_statuses["form2"] = True  # Mark form as completed
        elif current_form_key == "form4":
            if form_4():
                form_statuses["form4"] = True  # Mark form as completed
        elif current_form_key == "form6":
            if form_6():
                form_statuses["form6"] = True  # Mark form as completed
        elif current_form_key == "form7":
            if form_7():
                form_statuses["form7"] = True  # Mark form as completed
        elif current_form_key == "form9":
            if form_9():
                form_statuses["form9"] = True  # Mark form as completed
        elif current_form_key == "form11":
            if form_11():
                form_statuses["form11"] = True  # Mark form as completed
        elif current_form_key == "form12":
            if form_12():
                form_statuses["form12"] = True  # Mark form as completed

    # Display the completion status for each form in the sidebar, excluding the specified forms
    st.sidebar.header("Form Completion Status")
    for page, completed in form_statuses.items():
        if page not in forms_to_exclude:
            form_name = form_names[page]
            if completed:
                st.sidebar.write(f"{form_name}: ✔️")
            else:
                st.sidebar.write(f"{form_name}: ❌")

    # Display the content of the selected form, including excluded forms
    if user_selected_page == "form0":
        form_0()
    elif user_selected_page == "form3":
        form_3()
    elif user_selected_page == "form5":
        form_5()
    elif user_selected_page == "form8":
        form_8()
    elif user_selected_page == "form10":
        form_10()
    elif user_selected_page == "form13":
        form_13()

if __name__ == "__main__":
    main_form()
