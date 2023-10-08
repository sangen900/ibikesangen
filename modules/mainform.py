import streamlit as st
from form_0 import form_1
from form_1 import form_2
from form_2 import form_3
from form_3 import form_4
from form_4 import form_5
from form_5 import form_6
from form_6 import form_7
from form_7 import form_8
from form_8 import form_9
from form_9 import form_10
from form_10 import form_11
from form_11 import form_12
from form_12 import form_13
from form_13 import form_14
def main_form():
    page_names1001 = ["form_0", "form_1", "form_2", "form_3", "form_4", "form_5", "form_6", "form_7", "form_8", "form_9", "form_10", "form_11", "form_12", "form_13"]
    user_selected_page = st.sidebar.radio("Please read the form carefully and fill the below form.", page_names1001)
    
    if user_selected_page == "form_0":
        form_1()
    elif user_selected_page == "form_1":
        form_2()
    elif user_selected_page == "form_2":
        form_3()
    elif user_selected_page == "form_3":
        form_4()
    elif user_selected_page == "form_4":
        form_5()
    elif user_selected_page == "form_5":
        form_6()
    elif user_selected_page == "form_6":
        form_7()
    elif user_selected_page == "form_7":
        form_8()
    elif user_selected_page == "form_8":
        form_9()
    elif user_selected_page == "form_9":
        form_10()
    elif user_selected_page == "form_10":
        form_11()
    elif user_selected_page == "form_11":
        form_12()
    elif user_selected_page == "form_12":
        form_13()
    elif user_selected_page == "form_13":
        form_14()
if __name__ == "__main__":
    main_form()
