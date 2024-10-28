import pandas as pd
import sqlite3 as db
import functions
file_name = 'ecars.db'
connection = db.connect(file_name)
my_cursor = connection.cursor()
countries = my_cursor.execute ('select * from Countries')
rows= my_cursor.fetchall()
countries_df = pd.DataFrame(rows)
# create a dataframethat shows sales data from the sales table <<< TO DO
countries_df.columns = ['Coumtry', 'Comtinent']
functions.print_it('df from query result: ', countries_df)
sales_df = my_cursor.execute ('select * from sales')
sales_df = pd.DataFrame(rows)
functions.print_it('sales in Country: ',sales_df)