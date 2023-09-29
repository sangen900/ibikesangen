def render():
    import streamlit as st

    #radio1
    st.markdown(
        """
        <p style='font-size: 20px; margin-bottom: 0;'>What is manufacturing?</p>
        """,
        unsafe_allow_html=True
    )
    options_q30 = [
        "A process that attempts to decompose an object into its basic units.", 
        "A process that transforms raw materials into finished products to add value.", 
        "A process that supports delivery or maintenance tangible commodities.", 
        "A process that measures operational reliability and assure conformance to specifications."
        "Manufacturing methods"
    ]

    selected_option_q30 = st.radio("", options_q30)
    st.markdown("---")
    #radio2
    st.markdown(
        """
        <p style='font-size: 20px; margin-bottom: 0;'>Which of the following is NOT a component of manufacturing?</p>
        """,
        unsafe_allow_html=True
    )
    options_q31 = [
        "Adds value", 
        "Transforms raw materials", 
        "Creates products", 
        "Extracts material"
    ]

    selected_option_q31 = st.radio("", options_q31)
    st.markdown("---")
    #radio3
    st.markdown(
        """
        <p style='font-size: 20px; margin-bottom: 0;'>What are the six pillars of manufacturing?</p>
        """,
        unsafe_allow_html=True
    )
    options_q32 = [
        "1.Requirements Ananlysis, 2. Product Design, 3. Processes Configuration, 4. Production Planning, 5. Product Assembly, 6. Product Delivery", 
        "1.Product Design, 2. Manufacturing Materials, 3. Manufacturing Processes, 4. Manufacturing systems, 5. Manufacturing Technologies, 6.Business Processes.", 
        "1.Conceptualization, 2. Resource planning, 3. Resources Scheduling, 4. Task assignment. 5. Execution. 6. Tremination", 
        "1.Analyzing, 2. Designing, 3. Manufacturing, 4. Testing, 5.Delivering, and 6. maintaining"
    ]

    selected_option_q32 = st.radio("", options_q32)
    st.markdown("---")
    #radio4
    st.markdown(
        """
        <p style='font-size: 20px; margin-bottom: 0;'>Which of the following is NOT a characteristic of a pillar of manufacturing?</p>
        """,
        unsafe_allow_html=True
    )
    options_q33 = [
        "Provides Knowledge in a defoned manufacturing area.", 
        "A building block of manufacturing that is characterized by a specific domain knowledge in manufacturing.", 
        "Includes product design, manufacturing materials, manufacturing processes, manufacturing systems, manufacturing technologies, and business processes.", 
        "Decomposition of an object into its basic units."
    ]

    selected_option_q33 = st.radio("", options_q33)
    st.markdown("---")
    #radio5
    st.markdown(
        """
        <p style='font-size: 20px; margin-bottom: 0;'>What is the definition of Product Design?</p>
        """,
        unsafe_allow_html=True
    )
    options_q34 = [
        "The process of making the product and delivering it to the end customer.", 
        "The process of importing the raw material from supplier.", 
        "The process of defining product characteristics (e.g., dimensions, appearance, materials, tolerance, etc.)"
        "The process of transforming the raw material into finished product."
    ]
    selected_option_q34 = st.radio("", options_q34)
    st.markdown("---")
    #radio6
    st.markdown(
        """
        <p style='font-size: 20px; margin-bottom: 0;'>What is the definition of Manufacturing Materials?</p>
        """,
        unsafe_allow_html=True
    )
    options_q35 = [
        "The input materials or substances used in the production of goods.", 
        "The input material which is dispose after production.", 
        "The input material which is assisted the production but not a part of final product."
        "The input material which is dissipated during production."
    ]
    selected_option_q35 = st.radio("", options_q35)
    st.markdown("---")
    #radio7
    st.markdown(
        """
        <p style='font-size: 20px; margin-bottom: 0;'>What is the definition of Manufacturing Processes?</p>
        """,
        unsafe_allow_html=True
    )
    options_q36 = [
        "A sequence of steps to decide the manufacturing process", 
        "A sequence of step to design the product.", 
        "A sequence of step to decide the cost of the product."
        "A specified combination or sequence of steps through which raw material is transformed into a final product."
    ]
    selected_option_q36 = st.radio("", options_q36)
    st.markdown("---")
    #radio8
    st.markdown(
        """
        <p style='font-size: 20px; margin-bottom: 0;'>What is the definition of Business Processes?</p>
        """,
        unsafe_allow_html=True
    )
    options_q37 = [
        "A sequence of related task designed for some type of financial gain.", 
        "A series of tasks associated with generating revenue or incurring costs.", 
        "A collection of tasks related to the oversight and management of people within the organization."
        "Is a collection of linked tasks which supports the reciept, execution, and/or delivery of aservice or product."
    ]
    selected_option_q37 = st.radio("", options_q37)
    st.markdown("---")
    #radio9
    st.markdown(
        """
        <p style='font-size: 20px; margin-bottom: 0;'>Which of the following statements BEST describes the product development life cycle?</p>
        """,
        unsafe_allow_html=True
    )
    options_q38 = [
        "Progression of phaases that follows a product over time from creation to maturity and finally to decline.", 
        "The sequence of stages necessary to take a product from an idea to the end customer.", 
        "the progression of product through a series of stages from design to manufacturing."
        "is the sequence of stages that a product goes through from its manufacturing to its deliver to the end customer."
    ]
    selected_option_q38 = st.radio("", options_q38)
    st.markdown("---")
    #radio10
    st.markdown(
        """
        <p style='font-size: 20px; margin-bottom: 0;'>What is the correct order of the stages of the product development lifecycle?</p>
        """,
        unsafe_allow_html=True
    )
    options_q39 = [
        "1.Concept, 2. Launch, 3. Development, 4. Manufacture, 5. Test, 6. sell", 
        "1.Product Design, 2. Manufacturing materials, 3. Manufacturing processes, 4. Manufacturing Systems, 5. manufacturing Technologies, 6. Business processes.", 
        "1.Concept, 2. Design, 3. Plan, 4. manufacture, 5. Test, 6. Store."
        "1.Concept, 2. Development, 3. Prototype, 4. Manufacture, 5. Launch, 6. Distribution"
    ]
    selected_option_q39 = st.radio("", options_q39)
