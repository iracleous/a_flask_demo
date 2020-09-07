import pandas as pd
import sqlalchemy as alc
import urllib

def getFromSql (tableName):
    connStr = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=codehub;UID=sa;PWD=passw0rd'
    params = urllib.parse.quote_plus(connStr)
    engine = alc.create_engine("mssql+pyodbc:///?odbc_connect={}".format(params))


    #load csv from  MS SQL 
    df = pd.read_sql(tableName, con=engine)
 
    return df

     

 