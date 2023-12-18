#Alex Rogers22018703

import mysql.connector
from mysql.connector import errorcode
 
# MYSQL CONFIG VARIABLES
name = "shahbaz"
if name == "alex":
    #idk why this isnt working man
    hostname    = "localhost"
    username    = "root"
    passwd  = "password"
    db = "Horizon_Restaurant"
    
elif name == "jev":
    hostname    = "localhost"
    username    = "root"
    passwd  = "minecraft"
    db = "Horizon_Restaurant"
    
elif name == "will":
    hostname    = "localhost"
    username    = "root"
    passwd  = "12345678"
    db = "Horizon_Restaurant"

elif name=="shahbaz":
    hostname    = "localhost"
    username    = "root"
    passwd  = "1234"
    db = "Horizon_Restaurant"
    
elif name == "shahbaz":
    hostname    = "localhost"
    username    = "root"
    passwd  = "1234"
    db = "Horizon_Restaurant"
    
else:
    hostname    = "localhost"
    username    = "root"
    passwd  = "minecraft"
    db = "Horizon_Restaurant"

def getConnection():    
    try:
        conn = mysql.connector.connect(host=hostname,                              
                              user=username,
                              password=passwd,
                              database=db)  
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('User name or Password is not working')
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print('Database does not exist')
        else:
            print(err)                    
    else:  #will execute if there is no exception raised in try block
        return conn   
                
