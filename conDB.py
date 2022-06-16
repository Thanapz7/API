
import mysql.connector

def conDB():
    mydb = mysql.connector.connect(
            host="localhost",
            user="test",
            password="12345",
            database="test",
        )
    return mydb

class Con:
    def getHW():
        mydb = conDB()
        mycursor = mydb.cursor(dictionary=True)
        sql = "SELECT value FROM hardware"
        mycursor.execute(sql)
        data = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return data 
#getdata = Con.getHW()
#for i in getdata:
#    print(i)

   
    def getHWname():
        mydb = conDB()
        mycursor = mydb.cursor(dictionary=True)
        sql = "SELECT name FROM hardware"
        mycursor.execute(sql)
        data = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return data 
# getdata = Con.getHWname()
# for i in getdata:
#     print(i)
    
    def insertHW(name, hw_name):
        mydb = conDB()
        mycursor = mydb.cursor(dictionary=True)
        sql = "INSERT INTO hardware (name, hw_name, status, value) VALUES ('{}', '{}', 'OFF', 0.00)".format(name, hw_name)
        mycursor.execute(sql)
        mydb.commit()
        ID = mycursor.lastrowid
        mycursor.close()
        mydb.close()
        return ID
# data = Con.insertHW()
# print(data)
    
    def updateHW(ID, status):
        mydb = conDB()
        mycursor = mydb.cursor(dictionary=True)
        sql = "UPDATE hardware SET status = '{}' WHERE id = {}".format(status, ID)
        mycursor.execute(sql)
        mydb.commit()
        mycursor.close()
        mydb.close()
        return True
    
    def updateHWvalue(ID, value):
        mydb = conDB()
        mycursor = mydb.cursor(dictionary=True)
        sql = "UPDATE hardware SET value = '{}' WHERE id = {}".format(value, ID)
        mycursor.execute(sql)
        mydb.commit()
        mycursor.close()
        mydb.close()
        return True
#data = Con.updateHW()
#print(data)

    def deleteHW(ID):
        mydb = conDB()
        mycursor = mydb.cursor(dictionary=True)
        sql = "DELETE FROM hardware WHERE id ={}".format(ID)
        mycursor.execute(sql)
        mydb.commit()
        mycursor.close()
        mydb.close()
        return True
# data = Con.deleteHW()
# print(data)

    def selectHW():
        mydb = conDB()
        mycursor = mydb.cursor(dictionary=True)
        sql = "SELECT * FROM hardware WHERE id = (SELECT MIN(id) FROM hardware)"
        mycursor.execute(sql)
        data = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return data 

    def selectHW_byid(ID):
        mydb = conDB()
        mycursor = mydb.cursor(dictionary=True)
        sql = "SELECT * FROM hardware WHERE id = {}".format(ID)
        mycursor.execute(sql)
        data = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return data 
    
   