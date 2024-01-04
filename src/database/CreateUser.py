import mysql.connector, dbfunc
from mysql.connector import errorcode
from passlib.hash import sha256_crypt

  #connection to DB
# DB_NAME = 'horizon_resturant'    #DB Name
# DB_NAME = 'horizonResturant'    #DB Name  MISPELLED
DB_NAME = 'Horizon_Restaurant'
staffId = 2
restrantid = 2
staffName = 'admin'
staffType = 'ADMIN'
staffPassword = sha256_crypt.hash('password')  #password goes in brackets default password

restId = 2
restloc = "BRISTOL"
restname = 'Bristol 2'
restcap = 6


conn = dbfunc.getConnection() 
if conn != None:    #Checking if connection is None
    if conn.is_connected(): #Checking if connection is established
        print('MySQL Connection is established')                          
        dbcursor = conn.cursor()    #Creating cursor object
        dbcursor.execute('USE {};'.format(DB_NAME)) #use database
        dbcursor.execute("INSERT INTO restaurant (restaurant_id, restaurant_location, restaurant_name, \
                         restaurant_capacity) VALUES (%s, %s, %s, %s)", (restId, restloc, restname, restcap))     
        conn.commit() 
        print("resterant created sucsesfully")
        dbcursor.close()       
        conn.close() #Connection must be closed
    else:
        print('DB connection error')
else:
    print('DBFunc error')
    
conn = dbfunc.getConnection() 
if conn != None:    #Checking if connection is None
    if conn.is_connected(): #Checking if connection is established
        print('MySQL Connection is established')                          
        dbcursor = conn.cursor()    #Creating cursor object
        dbcursor.execute('USE {};'.format(DB_NAME)) #use database
        dbcursor.execute("INSERT INTO employee (employee_id, restaurant_id, employee_name, employee_account_type, \
                                 employee_password) VALUES (%s, %s, %s, %s, %s)", (staffId, restrantid, staffName, staffType, staffPassword))     
        conn.commit() 
        print("User created sucsesfully")
        dbcursor.close()       
        conn.close() #Connection must be closed
    else:
        print('DB connection error')
else:
    print('DBFunc error')
    
conn = dbfunc.getConnection() 
if conn != None:    #Checking if connection is None
    if conn.is_connected(): #Checking if connection is established
        print('MySQL Connection is established')                          
        dbcursor = conn.cursor()    #Creating cursor object
        dbcursor.execute('USE {};'.format(DB_NAME)) #use database
        dbcursor.execute("INSERT INTO tables (table_number, table_capacity, restaurant_id) VALUES (%s, %s, %s)", (1, 6, 2))    
        conn.commit() 
        print("table created sucsesfully")
        dbcursor.close()       
        conn.close() #Connection must be closed
    else:
        print('DB connection error')
else:
    print('DBFunc error')