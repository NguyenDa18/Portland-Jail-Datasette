import pandas as pd
import sqlite3

# Read the csv file
details_csv_file = 'https://raw.githubusercontent.com/NguyenDa18/Portland-Jail-Data-Crawler/main/csvs/inmate_details.csv'
charges_csv_file = 'https://raw.githubusercontent.com/NguyenDa18/Portland-Jail-Data-Crawler/main/csvs/inmate_charges.csv'

# Load CSV into a dataframe
details_df = pd.read_csv(details_csv_file)

# Convert the Booking Date column to datetime
details_df['Booking Date'] = pd.to_datetime(details_df['Booking Date'])

# add column names
column_names = ['Charge', 'Bail Amount', 'Status', 'Name']
charges_df = pd.read_csv(charges_csv_file, names=column_names)


# Create a connection to the database file
conn = sqlite3.connect('pdx_inmates_data.db')

# Use the to_sql method to insert the dataframe into the database
details_df.to_sql('inmate_details', con=conn, if_exists='replace', index=False)
charges_df.to_sql('inmate_charges', con=conn, if_exists='replace', index=False)

conn.close()
