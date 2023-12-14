import mysql.connector,dbfunc

conn = dbfunc.getConnection()   #connection to DB
DB_NAME = 'horizon_Resturant'             #DB Name
DBStatement = 'CREATE DATABASE ' + DB_NAME + ';'    #SQL
if conn != None:    #Checking if connection is None
    if conn.is_connected(): #Checking if connection is established
        print('MySQL Connection is established')                          
        dbcursor = conn.cursor()    #Creating cursor object
        #CREATE database - only if you want to create new DB and 
        #your useraccount has privileges to create new Database        
        dbcursor.execute(DBStatement)
        #dbcursor.execute('CREATE DATABASE {}'.format(DB_NAME))
        print("Database {} created successfully.".format(DB_NAME))     
        dbcursor.close()                               
        conn.close() #Connection must be closed
    else:
        print('DB connection error')
else:
    print('DBFunc error')