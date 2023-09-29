import streamlit as st
def render():
    # Define a CSS style to set the font size to 20 pixels and reduce the margin
    css_style = f"font-size: 20px; margin: 0;"

    # Define the radio button style to inherit font size
    radio_style = ".st-radio .stRadio label { font-size: inherit; }"

    # Main Streamlit app
    st.markdown(
        """
        <p style='font-size: 24px; margin-bottom: 0;'><b>Check-in: iBike Lesson Part 2</b></p>
        """,
        unsafe_allow_html=True
    )
    st.markdown("---")
    # Define statement sets
    statement_set_1 = [
        ("The material used to make a product is limited by (select all that apply):", None),
        ("Its availability", "availability"),
        ("Its transportability", "transportability"),
        ("Its affordability", "affordability"),
        ("Its processibility", "processibility"),
        ("Its processibility to meet specification", "processibility_specification")
    ]

    statement_set_2 = [
        ("Why do natural materials need to be processed? Select all that apply.", None),
        ("So that material's shape can change as needed by the product", "shape_change"),
        ("So that the material is more sanitary", "material_sanitary"),
        ("So that the material's properties can function the way desired by the product", "material_properties"),
        ("So that varied materials can be used and assembled into one product", "varied_materials_assembly")
    ]

    statement_set_3 = [
        ("What should be considered in selecting the method to process materials? Select all that apply.", None),
        ("The specifications of the product design", "product_design_specifications"),
        ("Whether the method has the capacity to process materials demanded by the market", "method_capacity"),
        ("Whether the method produces too much material waste", "material_waste"),
        ("Whether the processing method requires more investment in tools, space, etc.", "investment_required")
    ]

    # Loop through statement sets
    for index, statement_set in enumerate([statement_set_1, statement_set_2, statement_set_3]):
        if index > 0:
            st.markdown("---")  # Add a horizontal rule between statement sets

        if statement_set[0][0]:  # Check if a title is defined
            st.markdown(
                f"""
                <p style='{css_style}'>{statement_set[0][0]}</p>
                """,
                unsafe_allow_html=True
            )

        # Loop through individual statements in the set
        for statement, key in statement_set[1:]:
            if statement:  # Check if a statement is defined
                # Display the statement with custom style
                st.markdown(f'<p style="{css_style}">{statement}:</p>', unsafe_allow_html=True)

                # Apply the CSS style for radio buttons
                with st.markdown(f'<style>{radio_style}</style>'):
                    selected_option = st.radio(
                        "",
                        ["Applies", "Does NOT apply"],
                        key=key,
                        help=""
                    )
