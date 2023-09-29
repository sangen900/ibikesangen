def render():
    import streamlit as st


    st.markdown(
        """
        <p style='font-size: 20px; margin-bottom: 0;'><b>Check-in: iBike Lesson Part 1</b></p>
        """,
        unsafe_allow_html=True
    )
    st.markdown("---")
    st.markdown(
        """
        <p style='font-size: 20px; margin-bottom: 0;'>Check all descriptions that are correct about “manufacturing”</p>
        """,
        unsafe_allow_html=True
    )
    # Define the list of text statements
    text_statements = [
        "The word manufacturing means made by machine.",
        "The manufacturing process is technological.",
        "The manufacturing process is economical.",
        "Manufacturing industry produces goods with added value.",
        "Manufacturing creates job opportunities."
    ]

    # Define a CSS style to set the font size to 20 pixels
    css_style = f"font-size: 20px;"

    # Create a loop to generate radio buttons for each statement with the custom style
    for statement in text_statements:
        st.markdown(f'<div style="{css_style}">{statement}</div>', unsafe_allow_html=True)
        selected_option = st.radio("", ["Correct", "Incorrect"], index=0, key=statement)

    # You can access the selected_option variable for each statement to get the user's choice
    st.markdown("---")
    st.markdown(
        """
        <p style='font-size: 20px; margin-bottom: 0;'>Which of the following statements is NOT true regarding manufacturing pillars?</p>
        """,
        unsafe_allow_html=True
    )
    statements = [
        "Manufacturing pillars are specific domains of knowledge necessary for bringing a concept of a product to the end user in the market.",
        "Business processes are distinct and separate from manufacturing.",
        "Manufacturing pillars benefit the economy by adding value to materials.",
        "Consumer's needs are an important part of the manufacturing pillars."
    ]

    # Create a radio button for the provided statements
    selected_option = st.radio("", statements)
    st.markdown("---")
    st.markdown(
        """
        <p style='font-size: 20px; margin-bottom: 0;'>Product characteristics are defined during:
    </p>
        """,
        unsafe_allow_html=True
    )
    options = [
        "Product Design",
        "Concept Generation",
        "Prototyping",
        "Product Launch"
    ]

    # Create a radio button for the provided options
    selected_option = st.radio("", options)
    st.markdown("---")
    # You can access the selected_option variable for each statement to get the user's choice
    st.markdown(
        """
        <p style='font-size: 20px; margin-bottom: 0;'>In the product development cycle, which of the following stages fall under Concept Development? Select all that apply.
    </p>
        """,
        unsafe_allow_html=True
    )
  

    # Define the list of text statements with unique keys
    statements = [
        ("Abide by product specifications", "statement1"),
        ("Select the materials to produce it", "statement2"),
        ("Select the method to produce it", "statement3"),
        ("Launch the product to the market", "statement4")
    ]

    # Define a CSS style to set the font size to 20 pixels
    css_style = f"font-size: 20px;"

    # Create a loop to generate radio buttons for each statement with "Apply" and "Do NOT apply" options and custom styling
    for statement, key in statements:
        st.markdown(f'<div style="{css_style}">{statement}:</div>', unsafe_allow_html=True)
        selected_option = st.radio("", ["Apply", "Do NOT apply"], key=key)


    # You can access the selected_option variable for each title to get the user's choice
    st.markdown("---")
    st.markdown(
        """
        <p style='font-size: 20px; margin-bottom: 0;'>Why is understanding the dynamic behavior of bikes important?
    </p>
        """,
        unsafe_allow_html=True
    )
    import streamlit as st

    # Create a list of options for the radio buttons
    options = [
        "To better understand the stability of a bike",
        "To design an effective controller in case of electric bikes",
        "To be able to improve the design of a bike prior to construction"
    ]

    # Use st.radio to create the radio buttons without a label
    selected_option = st.radio("", options)
    



