import pandas as pd
import streamlit as st


st.title("Dev Log Generator")

if "data" not in st.session_state:
    data = pd.DataFrame(
        {"Date": [], "Start Time": [], "End Time": [], "Time Spent": []}
    )
    st.session_state.data = data


st.dataframe(st.session_state.data)


def add_dfForm():
    row = pd.DataFrame(
        {
            "Date": [st.session_state.input_df_form_col1],
            "Start Time": [st.session_state.input_df_form_col2],
            "End Time": [st.session_state.input_df_form_col3],
            "Time Spent": [
                #cannot subract these two values because they are time_input
                st.session_state.input_df_form_col2 - st.session_state.input_df_form_col3
            ],
        }
    )
    st.session_state.data = pd.concat([st.session_state.data, row])


dfForm = st.form(key="dfForm", clear_on_submit=True)
with dfForm:
    dfFormColumns = st.columns(4)
    with dfFormColumns[0]:
        st.date_input("Date", value= None,key="input_df_form_col1", format="MM/DD/YYYY")
    with dfFormColumns[1]:
        st.time_input("Start Time", value=None, key="input_df_form_col2")
    with dfFormColumns[2]:
        st.time_input("End Time", value=None, key="input_df_form_col3")
    with dfFormColumns[3]:
        pass
    st.form_submit_button(on_click=add_dfForm)
