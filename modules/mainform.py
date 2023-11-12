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
    
    form_display_names = {
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

    st.sidebar.header("Please read the form carefully and fill the below form.")

    form_statuses = st.session_state.form_statuses
    user_selected_page = st.sidebar.radio("Select a form", list(form_statuses.keys()), format_func=lambda x: form_display_names[x])

    forms_to_exclude = ["form0", "form3", "form5", "form8", "form10", "form13"]

    try:
        form_key = next(key for key, value in form_display_names.items() if value == user_selected_page)
    except StopIteration:
        # Handle the case where the selected page name doesn't match any values
        form_key = None

    if form_key and form_key not in forms_to_exclude and form_key in form_statuses:
        form_function = globals()[form_key]
        if form_function():
            form_statuses[form_key] = True

    st.sidebar.header("Form Completion Status")
    for page, completed in form_statuses.items():
        if page not in forms_to_exclude:
            display_name = form_display_names[page]
            if completed:
                st.sidebar.write(f"{display_name}: ✔️")
            else:
                st.sidebar.write(f"{display_name}: ❌")

    if form_key == "Starting Form":
        form_0()
    elif form_key == "Manufacturing Knowledge Form":
        form_3()
    elif form_key == "YouTube Video 1 Form":
        form_5()
    elif form_key == "YouTube Video 2 Form":
        form_8()
    elif form_key == "YouTube Video 3 Form":
        form_10()
    elif form_key == "Ending Form":
        form_13()
    elif form_key:
        form_function = globals()[form_key.lower().replace(" ", "_")]
        form_function()

if __name__ == "__main__":
    main_form()
