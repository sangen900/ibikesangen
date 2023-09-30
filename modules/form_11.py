def render():
    import streamlit as st
    # Section 1: Check-in Part 3
    st.markdown(
    """
    <p style='font-size: 24px; margin-bottom: 0;'><b>Check-in: iBike Lesson Part 3</b></p>
    """,
    unsafe_allow_html=True
    )
    st.markdown("---")
    # Section 2: Manufacturing Paradigms
    st.markdown(
    """
    <p style='font-size: 20px; margin-bottom: 0;'>Manufacturing paradigms are:</p>
    """,
    unsafe_allow_html=True
    )
    options_q5 = [
    "Production Volume", 
    "Manufacturing equipment", 
    "Manufacturing technologies", 
    "Manufacturing models that characterize a specific period", 
    "Manufacturing methods"
    ]

    selected_option_q5 = st.radio("", options_q5)

    # Section 3: Evolution of Manufacturing Paradigms
    st.markdown("---")

    st.markdown(
    """
    <p style='font-size: 20px; margin-bottom: 0;'>The evolution of the manufacturing paradigms is illustrated in the figure below using a volume-variety relationship. Match the letters in the second column to the manufacturing paradigm first column of the table below</p>
    """,
    unsafe_allow_html=True
    )
    # Display an image
    import streamlit as st
    import os

    # Get the user's home directory
    user_home = os.path.expanduser("~")

    # Specify the path to the image on your desktop
    image_filename = "ibike.jpg"
    desktop_path = os.path.join(user_home, "Desktop", image_filename)

    # Display the image
    st.image(desktop_path, use_column_width=True)


    # Define the list of titles
    titles = ["Lean manufacturing", "Craft production", "Personalized production", "Mass customization", "Mass production"]

    # Create a dictionary to store selected options for each title
    selected_options_titles = {}

    # Loop through each title and add radio buttons with unique keys
    for title in titles:
    # Display the title
     st.markdown(
    f"<p style='font-size: 20px; margin-bottom: 0;'>{title}</p>",
    unsafe_allow_html=True
    )

    # Create a unique key for this title
    key = f"{title}_option"

    # Create a radio button for this title with the options
    selected_option = st.radio("", ["A", "B/C", "D", "F", "Not Applicable"], key=key)

    # Store the selected option in the dictionary
    selected_options_titles[title] = selected_option

    # Section 4: Additional Questions
    st.markdown("---")

    # Question 1
    st.markdown(
    """
    <p style='font-size: 20px; margin-bottom: 0;'>Which of the following did NOT drive manufacturing technology revolutions? </p>
    """,
    unsafe_allow_html=True
    )

    options_q1 = ["Steam", "Mechanical assembly", "Electricity", "Internet"]
    selected_option_q1 = st.radio("", options_q1)

    st.markdown("---")

    # Question 2
    st.markdown(
    """
    <p style='font-size: 20px; margin-bottom: 0;'>Which of the following supply chain activities may impact a product’s final cost?</p>
    """,
    unsafe_allow_html=True
    )

    options_q2 = [
    "Purchasing raw materials from suppliers",
    "Transporting raw materials to manufacturing plants",
    "Manufacturing products",
    "Transporting products to distribution centers",
    "All of the above"
    ]

    selected_option_q2 = st.radio("", options_q2)

    st.markdown("---")

    # Question 3
    st.markdown(
    """
    <p style='font-size: 20px; margin-bottom: 0;'>Which of the following statements about business processes is true?</p>
    """,
    unsafe_allow_html=True
    )

    options_q3 = [
    "They are executed across multiple functions.",
    "They are initiated by some type of trigger.",
    "They involve multiple activities.",
    "All of the above",
    "None of the above"
    ]

    selected_option_q3 = st.radio("", options_q3)

    st.markdown("---")

    # Question 4
    st.markdown(
    """
    <p style='font-size: 20px; margin-bottom: 0;'>The tendency of individuals to solely focus on the performance of their own activity with no concern or knowledge of the other tasks associated with proceeding or subsequent activities is called</p>
    """,
    unsafe_allow_html=True
    )

    options_q4 = [
    "The bottleneck effect",
    "The silo effect",
    "The blinders effect",
    "The manufacturing crossover"
    ]

    selected_option_q4 = st.radio("", options_q4)
    render()
