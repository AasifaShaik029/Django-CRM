import mysql.connector
dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Xy!@34567',
)

cursorObject =  dataBase.cursor()
cursorObject.execute("CREATE DATABASE crmdatabase")
print("crmdatabase created") 