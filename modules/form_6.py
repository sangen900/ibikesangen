def render(): 
    import streamlit as st
    st.markdown(
        """
        <p style='font-size: 20px; margin-bottom: 0;'>Please indicate your level of agreement with the following statements. </p>
        """,
        unsafe_allow_html=True
    )

    # Define the list of text titles
    text_titles = [
        "My parents see me as an engineer.",
        "My instructors see me as an engineer.",
        "My peers see me as an engineer.",
        "I am interested in learning more about engineering.",
        "I enjoy learning engineering.",
        "I find fulfilslment in doing engineering.",
        "I am confident that I can understand engineering in class.",
        "I am confident that I can understand engineering outside of class.",
        "I can do well on exams in engineering.",
        "I understand concepts I have studied in engineering.",
        "Others ask me for help in this subject."
    ]

    # Define a CSS style to set the font size to 20 pixels
    css_style = f"font-size: 20px;"

    # Create a loop to generate radio buttons for each title with the custom style
    for title in text_titles:
        st.markdown(f'<div style="{css_style}">{title}:</div>', unsafe_allow_html=True)
        selected_option = st.radio("", ["Strongly Disagree", "Disagree", "Somewhat Disagree", "Neither Agree nor Disagree", "Somewhat Agree", "Agree", "Strongly Agree"], index=3, key=title)

    # You can access the selected_option variable for each title to get the user's choice
    st.markdown("---")
    st.markdown(
        """
        <p style='font-size: 20px; margin-bottom: 0;'>Please indicate your level of agreement with the following statements. </p>
        """,
        unsafe_allow_html=True
    )
    import streamlit as st

    # Define the list of text titles
    text_titles = [
        "I can master the content in the engineering-related courses I am taking this semester.",
        "I can master the content in even the most challenging engineering course.",
        "I can do a good job on almost all my engineering coursework.",
        "I can learn the content taught in my engineering-related courses.",
        "I can earn a good grade in my engineering-related courses."
    ]

    # Define a CSS style to set the font size to 20 pixels
    css_style = f"font-size: 20px;"

    # Create a loop to generate radio buttons for each title with the custom style
    for title in text_titles:
        st.markdown(f'<div style="{css_style}">{title}:</div>', unsafe_allow_html=True)
        selected_option = st.radio("", ["Strongly Disagree", "Disagree", "Somewhat Disagree", "Neither Agree nor Disagree", "Somewhat Agree", "Agree", "Strongly Agree"], index=3, key=title)
    render()
