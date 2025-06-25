import pyodbc

server = '10.0.252.20\\admin' # e.g., 'localhost\SQLEXPRESS' or 'your_server_ip'
database = 'dbDBA'
username = 'usr_rotinas'
password = 'TAF1513#abc'

cnxn_str = (
        'DRIVER={ODBC Driver 17 for SQL Server};' # Use the appropriate driver version
        f'SERVER={server};'
        f'DATABASE={database};'
        f'UID={username};'
        f'PWD={password}'
 )

cnxn = pyodbc.connect(cnxn_str)

cursor = cnxn.cursor()
query = "SELECT * FROM tblServidores"
cursor.execute(query)
rows = cursor.fetchall()
# Process 'rows' as needed
for row in rows:
    print(row)