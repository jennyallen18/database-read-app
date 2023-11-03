import pandas as pd
import psycopg2
import psycopg2.extras
import sqlalchemy
import streamlit as st

def get_connection():
    conn_string = "host='hh-pgsql-public.ebi.ac.uk' dbname='pfmegrnargs' user='reader' password='NWDMCE5xdipIjRrp'"
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    # retrieve a list of RNAcentral databases
    query = "SELECT * FROM rnc_database"

    cursor.execute(query)
    for row in cursor:
        print(row)


if __name__ == "__main__":
    get_connection()
