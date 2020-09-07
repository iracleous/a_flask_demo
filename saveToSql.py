import pandas as pd
import pyodbc
import sqlalchemy as alc
from sqlalchemy import create_engine
import urllib

data = [['Alex',10,5],['Bob',12,5],['Clarke',13,6]]
df = pd.DataFrame(data,columns=['Name','Age','Value'],dtype=float)
print (df)

#connStr = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=codehub;Trusted_Connection=yes')
connStr = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=codehub;UID=sa;PWD=passw0rd')



##create table PersonData (id int primary key identity(1,1), name nvarchar(255), age int, value int)

 #save dataframe to csv
#df.to_csv('PersonData.csv')


#save dataframe to MS SQL 
connStr = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=codehub;UID=sa;PWD=passw0rd'
params = urllib.parse.quote_plus(connStr)
engine = alc.create_engine("mssql+pyodbc:///?odbc_connect={}".format(params))
 
df.to_sql(name='PersonData', con=engine, if_exists = 'append', index=False)
 