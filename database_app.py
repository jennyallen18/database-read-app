import pandas as pd
import psycopg2
import psycopg2.extras
import sqlalchemy
import streamlit as st

def get_connection():
    conn_string = "host='hh-pgsql-public.ebi.ac.uk' dbname='pfmegrnargs' user='reader' password='NWDMCE5xdipIjRrp'"

    engine = sqlalchemy.create_engine("postgresql+psycopg2://reader:NWDMCE5xdipIjRrp@hh-pgsql-public.ebi.ac.uk/pfmegrnargs")
    
    # retrieve a list of RNAcentral databases
    query = "SELECT * FROM rnc_database"

    df = pd.read_sql_query(query, engine)
    #df.to_html(header="true", table_id="table")
    #print(df)
    pd.display(df)
   


if __name__ == "__main__":
    get_connection()
