import streamlit as st
def render():
    st.markdown(
        """
        <p style='font-size: 20px; margin-bottom: 0;'>Please select your age.</p>
        """,
        unsafe_allow_html=True
    )
    selected_age = st.selectbox("", list(range(18, 61)))
    st.markdown("---")
    st.markdown(
        """
        <p style='font-size: 20px; margin-bottom: 0;'>Please select your gender</p>
        """,
        unsafe_allow_html=True
    )
    options_q40 = [
        "Male", 
        "Female", 
        "Transgender female", 
        "Transgender male",
        "Non-binary/third gender",
        "Prefer not to say",
        "Not Listed"
    ]
    selected_option_q40 = st.radio("", options_q40)
    other_input_gender = ""
    if selected_option_q40 == "Not Listed":
        other_input_gender = st.text_input("Please specify your gender", key="text_input_gender")

    st.markdown("---")
    st.markdown(
        """
        <p style='font-size: 20px; margin-bottom: 0;'>Please select your race</p>
        """,
        unsafe_allow_html=True
    )
    options_q41 = [
        "Asian or Pacific Islander", 
        "Black or African American", 
        "Hispanic or Latino", 
        "Native American or Alaskan native", 
        "White or Caucasian", 
        "Multiracial or Biracial", 
        "A Race/ethnicity not listed here"
    ]
    selected_option_q41 = st.radio("", options_q41)
    other_input_race = ""
    if selected_option_q41 == "A Race/ethnicity not listed here":
        other_input_race = st.text_input("Please specify your race/ethnicity", key="text_input_race")

    st.markdown("---")

    st.markdown(
        """
        <p style='font-size: 20px; margin: 0;'>What is your cumulative GPA?</p>""",
        unsafe_allow_html=True
    )
    # Create a selectbox widget for cumulative GPA
    selected_gpa = st.selectbox("", [str(x/10) for x in range(40, 19, -1)])
    st.markdown("---")

    st.markdown(
        """
        <p style='font-size: 20px; margin-bottom: 0;'>What year of college are you in?.</p>
        """,
        unsafe_allow_html=True
    )
    selected_option = st.radio("", ["First", "Second", "Third", "Fourth", "Fifth", "Sixth", "Seventh"])
    other_input_college = ""
    if selected_option == "Not Listed":
        other_input_college = st.text_input("Please specify your college year", key="text_input_college")
    st.markdown("---")
    st.markdown(
        """
        <p style='font-size: 20px; margin-bottom: 0;'>What is your major?</p>
        """,
        unsafe_allow_html=True
    )
    selected_concentration = st.radio("", ["Engineering (list specific concentration)"])
    other_input_major = ""
    if selected_concentration == "Engineering (list specific concentration)":
        other_input_major = st.text_input("Please specify your major concentration", key="text_input_major")
    st.markdown("---")
