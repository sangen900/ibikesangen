import streamlit as st
def render():
    st.markdown(
        """
        <p style='font-size: 20px; margin-bottom: 0;'>In your own words, define manufacturing.</p>
        """,
        unsafe_allow_html=True
    )
    user_input1 = st.text_area("", key="text_area_1")
    st.markdown("---")
    st.markdown(
        """
        <p style='font-size: 20px; margin-bottom: 0;'>In your own words, define manufacturing pillars.</p>
        """,
        unsafe_allow_html=True
    )
    user_input2 = st.text_area("", key="text_area_2")
    st.markdown("---")
    st.markdown(
        """
        <p style='font-size: 20px; margin-bottom: 0;'>List and briefly describe the six pillars.</p>
        """,
        unsafe_allow_html=True
    )
    user_input3 = st.text_area("", key="text_area_3")
    st.markdown("---")
    st.markdown(
        """
        <p style='font-size: 20px; margin-bottom: 0;'>In your own words, define manufacturing systems.</p>
        """,
        unsafe_allow_html=True
    )
    user_input4 = st.text_area("", key="text_area_4")
    st.markdown("---")
    st.markdown(
        """
        <p style='font-size: 20px; margin-bottom: 0;'>In your own words, define manufacturing technologies?</p>
        """,
        unsafe_allow_html=True
    )
    user_input5 = st.text_area("", key="text_area_5")
    st.markdown("---")
    st.markdown(
        """
        <p style='font-size: 20px; margin-bottom: 0;'>In your own words, define product development lifecycle?</p>
        """,
        unsafe_allow_html=True
    )
    user_input6 = st.text_area("", key="text_area_6")
    st.markdown("---")