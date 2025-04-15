import pandas as pd
import streamlit as st


st.title("Dev Log Generator")

if "data" not in st.session_state:
    data = pd.DataFrame(
        {"Date": [], "Start Time": [], "End Time": [], "Time Spent": [],  "Category":[],"Notes":[]}
    )
    st.session_state.data = data


st.dataframe(st.session_state.data)



def add_dfForm():

    row = pd.DataFrame(
        {
            "Date": [st.session_state.input_df_form_col1],
            "Start Time": [st.session_state.input_df_form_col2],
            "End Time": [st.session_state.input_df_form_col3],
            "Time Spent": [st.session_state.input_df_form_col4],
            "Category":[st.session_state.input_df_form_col5],
            "Notes":[st.session_state.input_df_form_col6]
        }
    )
    st.session_state.data = pd.concat([st.session_state.data, row])
    

dfForm = st.form(key="dfForm", clear_on_submit=True)


def add_dfFormRow():
    new_row = dfForm.loc[len(dfForm)] = ["new", 35]
    


with dfForm:
    
    dfFormColumns = st.columns(6)
    with dfFormColumns[0]:
        st.date_input("Date", value= None,key="input_df_form_col1", format="MM/DD/YYYY")
    with dfFormColumns[1]:
        st.time_input("Start Time", value=None, key="input_df_form_col2")
    with dfFormColumns[2]:
        st.time_input("End Time", value=None, key="input_df_form_col3")
    with dfFormColumns[3]:
        st.time_input("Hours Spent", value=None, key="input_df_form_col4")
    with dfFormColumns[4]:
        st.text_input("Category", value=None, key="input_df_form_col5", placeholder="Enter category")
    with dfFormColumns[5]:
        st.text_input("Notes", value=None, key="input_df_form_col6",placeholder="Enter notes here.")
        
    add_rows = st.form_submit_button('Create new row', on_click=add_dfFormRow)
    submit_action = st.form_submit_button('Add data to table', on_click=add_dfForm)
   
        
        
    
    
    
    
   
    
