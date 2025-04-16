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
            #grab the other keys from session state and add to data frame
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
  

with dfForm:
    
    dfFormColumns = st.columns(6)
    options = ["N/A", "Web Dev", "Marketing", "User Ticket","Misc."]
    
    #placeholder keys for the different inputs
    with dfFormColumns[0]:
        st.date_input("Date", value= None, key="input_df_form_col1", format="MM/DD/YYYY")
        st.date_input("Date", value= None, key="date_col2", format="MM/DD/YYYY")
        st.date_input("Date", value= None, key ="date_col3",format="MM/DD/YYYY")
        st.date_input("Date", value= None, key="date_col4", format="MM/DD/YYYY")
        st.date_input("Date", value= None, key ="date_col5",format="MM/DD/YYYY")
         
    with dfFormColumns[1]:
        st.time_input("Start Time", value=None, key="input_df_form_col2")
        st.time_input("Start Time", value=None, key="start_time_col3")
        st.time_input("Start Time", value=None, key="start_time_col4")
        st.time_input("Start Time", value=None, key="start_time_col5")
        st.time_input("Start Time", value=None, key="start_time_col6")
        
    with dfFormColumns[2]:
        st.time_input("End Time", value=None, key="input_df_form_col3")
        st.time_input("End Time", value=None, key="end_time_col4")
        st.time_input("End Time", value=None, key="end_time_col5")
        st.time_input("End Time", value=None, key="end_time_col6")
        st.time_input("End Time", value=None, key="end_time_col7")
        
    with dfFormColumns[3]:
        st.time_input("Hours Spent", value=None, key="input_df_form_col4")
        st.time_input("Hours Spent", value=None, key="hours_col4")
        st.time_input("Hours Spent", value=None, key="hours_col5")
        st.time_input("Hours Spent", value=None, key="hours_col6")
        st.time_input("Hours Spent", value=None, key="hours_col7")
        
    with dfFormColumns[4]:
        st.selectbox("Category", options, key="input_df_form_col5", placeholder="Select category")
        st.selectbox("Category", options, key="category_col5", placeholder="Select category")
        st.selectbox("Category", options, key="category_col6", placeholder="Select category")
        st.selectbox("Category", options, key="category_col7", placeholder="Select category")
        st.selectbox("Category", options, key="category_col8", placeholder="Select category")
        
        
    with dfFormColumns[5]:
        st.text_input("Notes", value=None, key="input_df_form_col6",placeholder="Enter notes here.")
        st.text_input("Notes", value=None, key="notes_col6",placeholder="Enter notes here.")
        st.text_input("Notes", value=None, key="notes_col7",placeholder="Enter notes here.")
        st.text_input("Notes", value=None, key="notes_col8",placeholder="Enter notes here.")
        st.text_input("Notes", value=None, key="notes_col9",placeholder="Enter notes here.")

    submit_action = st.form_submit_button('Add data to table', on_click=add_dfForm)

        
    
    
    
    
   
    
