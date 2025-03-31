import pandas as pd
import streamlit as st
from datetime import date, timedelta


current_date = date.today()

# for i in range(5):
#     current_date -= timedelta(days=1)
#     dates.append(str(current_date.strftime("%m/%d/%Y")))

# dates.reverse()

# date_keys = ['1','2','3','4','5']
# date_values = dates

# d = {date_keys[i]:date_values[i] for i in range(len(date_keys))}


with open("test.txt", 'w') as f:
    f.write('This is a new text file!')

df = pd.DataFrame(
        {"Dates":["2/1/25"],
        "Start Time":["8:00am"],
        "End Time":["10:00pm"],
        "Time Spent":["2 Hours"],
        "Ticket":["NA"],
        "Category":["NA"],
        "Notes":["Notes go here"]
    }
)
 

st.dataframe(df, hide_index=True)
st.download_button(label="Download Log as .xlsx file",data="test.txt",file_name="downloaded_file.txt")

text = st.text_area("Text Field")




    
