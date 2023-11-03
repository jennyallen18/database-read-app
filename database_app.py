import pandas as pd
import psycopg2
import psycopg2.extras
import sqlalchemy
import streamlit as st

def get_connection():
    # Connect to Database
    engine = sqlalchemy.create_engine("postgresql+psycopg2://reader:NWDMCE5xdipIjRrp@hh-pgsql-public.ebi.ac.uk/pfmegrnargs")
    
    # retrieve a table from the database databases
    query = "SELECT * FROM rnc_database"

    df = pd.read_sql_query(query, engine)

    # Display the table
    df
   

if __name__ == "__main__":
    get_connection()
