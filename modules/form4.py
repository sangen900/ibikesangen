import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
def form_4():
    javascript_code = """
    <script>
    document.addEventListener('DOMContentLoaded', function() {
    const textArea = document.querySelector('textarea');
    textArea.addEventListener('keydown', function(event) {
        if (event.key === 'Enter' && !event.shiftKey) {
        event.preventDefault();
        }
    });
    });
    </script>
    """
    with st.form("form4"):
        user_input1 = ""
        user_input2 = ""
        user_input3 = ""
        user_input4 = ""
        user_input5 = ""
        user_input6 = ""
        warnings = []
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
        #submit button
        submit_button = st.form_submit_button("Submit Form4")
        if submit_button:
           if not user_input1 or not user_input2 or not user_input3 or not user_input4 or not user_input5 or not user_input6:
             warnings.append("Please fill all the required forms:")
           if warnings:
                st.warning("\n".join(warnings))
           else:
                scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
                credentials = ServiceAccountCredentials.from_json_keyfile_name("my-credentials.json", scope)
                gc = gspread.authorize(credentials)
                #gsspreadsheet where data will be stored
                spreadsheet_id = "1UiBuyoFudQnvgzgIxlh__6ktEBKK7zJvqoWYwz_2WuE"  # Replace with your Spreadsheet ID
                sheet = gc.open_by_key(spreadsheet_id)
                worksheet_title = "Sheet3"
                worksheet = sheet.worksheet(worksheet_title)
                form_data2 = {
                            'In your own words, define manufacturing.': user_input1,
                            'In your own words, define manufacturing pillars.': user_input2,
                            'List and briefly describe the six pillars.': user_input3,
                            'In your own words, define manufacturing systems.': user_input4,
                            'In your own words, define manufacturing technologies?': user_input5,
                            'In your own words, define product development lifecycle?':user_input6
                        }
                num_rows = len(worksheet.get_all_values())
                worksheet.insert_rows([list(form_data2.values())], num_rows+1)
                st.success("Form 4 has been successfully submitted.")
                return True
                
