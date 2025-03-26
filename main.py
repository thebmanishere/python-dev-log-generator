import pandas as pd
from datetime import date, timedelta

#generate excel file depending on user input 
#need to generate 7 columns, and 30 rows
#date, start time, end time, time spent, ticket, category, notes (columns)

#pandas is a good library to use
xlsx_file_path = 'eggs.xlsx'

df = pd.read_excel("eggs.xlsx", sheet_name="eggs")

#build dict and then pass it to data frame

dates = []
start_times=[]
end_times=[]
time_spent=[]
ticket=[]
category=[]
notes=[]



current_date = date.today()

for i in range(5):
    current_date -= timedelta(days=1)
    dates.append(current_date.strftime("%m/%d/%Y"))

dates.reverse()

d = {}

df = pd.DataFrame(data=d)

df.to_excel(xlsx_file_path, index = False, sheet_name="eggs")




    
