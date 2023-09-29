import streamlit as st
def render():
    import form_0
    import form_1
    import form_2
    import form_3
    import form_4
    import form_5
    import form_6
    import form_7
    import form_8
    import form_9
    import form_10
    import form_11
    import form_12
    import form_13

    if "page_index" not in st.session_state:
        st.session_state.page_index = 0
    pages = [
        form_0.render,
        form_1.render,
        form_2.render,
        form_3.render,
        form_4.render,
        form_5.render,
        form_6.render,
        form_7.render,
        form_8.render,
        form_9.render,
        form_10.render,
        form_11.render,
        form_12.render,
        form_13.render,
    ]
    pages[st.session_state.page_index]()
    col1, col2, col3 = st.columns([1, 4, 1])
    if col1.button("Previous", key="prev_button") and st.session_state.page_index > 0:
        st.session_state.page_index -= 1
    if col3.button("Next", key="next_button", disabled=st.session_state.page_index == len(pages) - 1):
        st.session_state.page_index += 1
        st.session_state.page_index = max(0, min(st.session_state.page_index, len(pages) - 1))
