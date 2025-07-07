import mysql.connector


dataBase = mysql.connector.connect (
    host = 'localhost',
    user = 'root',
    passwd = 'axon9876'
)

curobj = dataBase.cursor()
curobj.execute("Create Database HPmainDB")
print('all done')