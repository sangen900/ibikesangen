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
            "consent_form": False,
            "basic_info_form": False,
            "manufacturing_knowledge_form": False,
            "defining_manufacturing_terms_form": False,
            "youtube_video1_form": False,
            "agreement_form": False,
            "ibike_part1_form": False,
            "youtube_video2_form": False,
            "ibike_part2_form": False,
            "youtube_video3_form": False,
            "ibike_part3_form": False,
            "manufacturing_form": False,
            "ending_form": False,
        }
    
    # Form names mapping
    form_names = {
        "form0": "Starting Form",
        "consent_form": "Consent Form",
        "basic_info_form": "Basic Information Form",
        "manufacturing_knowledge_form": "Manufacturing Knowledge Form",
        "defining_manufacturing_terms_form": "Defining Manufacturing Terms Form",
        "youtube_video1_form": "YouTube Video 1 Form",
        "agreement_form": "Agreement Form",
        "ibike_part1_form": "iBike Part 1 Form",
        "youtube_video2_form": "YouTube Video 2 Form",
        "ibike_part2_form": "iBike Part 2 Form",
        "youtube_video3_form": "YouTube Video 3 Form",
        "ibike_part3_form": "iBike Part 3 Form",
        "manufacturing_form": "Manufacturing Form",
        "ending_form": "Ending Form",
    }

    # Always display the sidebar
    st.sidebar.header("Please read the form carefully and fill the below form.")

    # Sidebar menu with radio buttons
    form_statuses = st.session_state.form_statuses
    user_selected_page = st.sidebar.radio("Select a form", list(form_statuses.keys()))

    # Forms to exclude from status bar updates
    forms_to_exclude = ["form0", "manufacturing_knowledge_form", "youtube_video1_form", "youtube_video2_form", "youtube_video3_form", "ending_form"]

    # Update the status of the selected form if it's not excluded
    if user_selected_page not in forms_to_exclude:
        form_function = globals().get(user_selected_page)
        if form_function and form_function():
            form_statuses[user_selected_page] = True  # Mark form as completed

    # Display the completion status for each form in the sidebar, excluding the specified forms
    st.sidebar.header("Form Completion Status")
    for page, completed in form_statuses.items():
        if page not in forms_to_exclude:
            form_name = form_names.get(page, page.capitalize())
            if completed:
                st.sidebar.write(f"{form_name}: ✔️")
            else:
                st.sidebar.write(f"{form_name}: ❌")

    # Display the content of the selected form, including excluded forms
    form_function = globals().get(user_selected_page)
    if form_function:
        form_function()

if __name__ == "__main__":
    main_form()
