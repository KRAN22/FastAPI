import mysql.connector
 
# Creating connection object
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Temp1234"
)
 
# Printing the connection object
cursor = mydb.cursor()

cursor.execute("SHOW DATABASES")
for x in cursor:
  print(x)