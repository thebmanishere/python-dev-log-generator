
import pandas as pd
import streamlit as st


st.title("Dev Log Generator")


if "data" not in st.session_state:
    data = pd.DataFrame(
        {"Date": [], "Start Time": [], "End Time": [], "Time Spent": [],  "Category":[],"Notes":[]}
    )
    st.session_state.data = data


st.dataframe(st.session_state.data, hide_index=True)



def add_dfForm():
    
    
   for r in range(form_rows):
    
    date_key = f'input_date_col'+str(r)
    start_time_key = f'input_start_time_col'+str(r)
    end_time_key = f'input_end_time_col'+str(r)
    time_spent_key = f'input_hours_spent_col'+str(r)
    category_key = f'input_category_col'+str(r)
    notes_key = f'input_notes_col'+str(r)
    
    
    row = pd.DataFrame(
        {
            "Date": [st.session_state[date_key]],
            "Start Time": [st.session_state[start_time_key]],
            "End Time": [st.session_state[end_time_key]],
            "Time Spent": [st.session_state[time_spent_key]],
            "Category":[st.session_state[category_key]],
            "Notes":[st.session_state[notes_key]]
        },
    )

    
    st.session_state.data = pd.concat([st.session_state.data, row])
    

dfForm = st.form(key="dfForm", clear_on_submit=True)


def add_row(row):
    
        with form_columns[0]:
            st.date_input("Date", value= None, key=f'input_date_col{row}', format="MM/DD/YYYY") 
        
        with form_columns[1]:
            st.time_input("Start Time", value=None, key=f'input_start_time_col{row}')
            
        with form_columns[2]:
            st.time_input("End Time", value=None, key=f'input_end_time_col{row}')
                
        with form_columns[3]:
            st.time_input("Hours Spent", value=None, key=f'input_hours_spent_col{row}')
                
        with form_columns[4]:
            st.selectbox("Category", options, key=f'input_category_col{row}', placeholder="Select category")
                
        with form_columns[5]:
            st.text_input("Notes", value=None, key=f'input_notes_col{row}',placeholder="Enter notes here.")
 
        
with dfForm:
    
    form_columns = st.columns(6)
    form_rows = st.slider("Number of rows", min_value=1, max_value=5)
    options = ["N/A", "Web Dev", "Marketing", "User Ticket","Misc."]
        
    
    submit_action = st.form_submit_button('Add rows to table')
    
    if submit_action:
        for r in range(form_rows):
            add_row(r) 
            
            
        
    add_to_form = st.form_submit_button('Add data to table', on_click=add_dfForm)


