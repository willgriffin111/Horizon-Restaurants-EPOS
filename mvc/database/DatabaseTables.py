import mysql.connector, dbfunc
from mysql.connector import errorcode

conn = dbfunc.getConnection()   #connection to DB
DB_NAME = 'Horizon_Restaurant'             #DB Name
TABLES = {}

# Data types 

# DOUBLE = decimal number 
# INT = whole number 
# VARCHAR = string value 

TABLES['CUTLERY'] = 'CREATE TABLE cutlery (\
  cutlery_id INT NOT NULL AUTO_INCREMENT,\
  PRIMARY KEY (cutlery_id), \
  cutlery_name VARCHAR(64) NOT NULL,\
  cutlery_quantity INT NOT NULL,\
  cutlery_reorder_level INT NOT NULL\
);'

TABLES['INGREDIENTS'] = 'CREATE TABLE ingredient (\
  ingredient_id INT NOT NULL AUTO_INCREMENT, \
  PRIMARY KEY (ingredient_id), \
  ingredient_name VARCHAR(64) NOT NULL,\
  ingredient_units VARCHAR(64) NOT NULL,\
  ingredient_quantity INT NOT NULL,\
  ingredient_reorder_level VARCHAR(64) NOT NULL,\
  ingredient_wastage VARCHAR(64) NOT NULL\
);'

TABLES['DISCOUNT'] = 'CREATE TABLE discount (\
  discount_id INT NOT NULL AUTO_INCREMENT, \
  PRIMARY KEY (discount_id),\
  discount_name VARCHAR(64) NOT NULL,\
  discount_validity_start DATE  NOT NULL,\
  discount_validity_end DATE NOT NULL,\
  discount_condition  VARCHAR(64) NOT NULL,\
  discount_is_active VARCHAR(64) NOT NULL,\
  discount_author VARCHAR(64) NOT NULL,\
  discount_date_created DATE NOT NULL\
);'
TABLES['EMPLOYEES'] = 'CREATE TABLE employee (\
  employee_id INT NOT NULL AUTO_INCREMENT,\
  PRIMARY KEY (employee_id),\
  employee_name VARCHAR(64) NOT NULL,\
  employee_account_type VARCHAR(64) NOT NULL,\
  employee_password VARCHAR(256) NOT NULL\
);'

TABLES['TABLES'] = 'CREATE TABLE tables (\
  table_id INT NOT NULL AUTO_INCREMENT,\
  PRIMARY KEY (table_id),\
  table_capacity INT NOT NULL,\
  table_is_reserved VARCHAR(64) NOT NULL\
);'

TABLES['RESERVATIONS'] = 'CREATE TABLE reservation (\
  reservation_id INT NOT NULL AUTO_INCREMENT, \
  PRIMARY KEY (reservation_id),\
  reservation_customer_name VARCHAR(64) NOT NULL,\
  reservation_customer_phone INT NOT NULL,\
  reservation_party_size INT NOT NULL,\
  reservation_author VARCHAR(64) NOT NULL,\
  reservation_creation_time DATETIME NOT NULL,\
  reservation_date DATE NOT NULL,\
  reservation_time DATETIME NOT NULL\
);'


TABLES['BILLS'] = 'CREATE TABLE bill (\
  bill_id INT NOT NULL AUTO_INCREMENT, \
  PRIMARY KEY (bill_id),\
  bill_sub_total DOUBLE NOT NULL,\
  bill_discount_applied DOUBLE NOT NULL,\
  bill_due_amount DOUBLE NOT NULL,\
  discount_id INT,\
  FOREIGN KEY (discount_id) \
  REFERENCES discount (discount_id)\
);'

TABLES['ORDERS'] = 'CREATE TABLE orders (\
  order_id INT NOT NULL AUTO_INCREMENT, \
  PRIMARY KEY (order_id),\
  order_table_num INT NOT NULL,\
  order_status VARCHAR(64) NOT NULL,\
  order_menu_items VARCHAR(64) NOT NULL,\
  order_payment_status VARCHAR(64) NOT NULL,\
  order_author VARCHAR(64) NOT NULL,\
  order_time_created DATETIME NOT NULL,\
  order_price VARCHAR(64) NOT NULL,\
  bill_id INT,\
  FOREIGN KEY (bill_id) \
  REFERENCES bill (bill_id)\
);'

TABLES['RESTAURANT'] = 'CREATE TABLE restaurant (\
  restaurant_id INT NOT NULL AUTO_INCREMENT,\
  PRIMARY KEY (restaurant_id),\
  restaurant_location VARCHAR(64) NOT NULL,\
  restaurant_name VARCHAR(64) NOT NULL,\
  restaurant_capacity INT NOT NULL,\
  restaurant_num_of_staff INT NOT NULL,\
  restaurant_manager VARCHAR(64) NOT NULL,\
  employee_id INT,\
  table_id INT,\
  reservation_id INT,\
  cutlery_id INT,\
  ingredient_id INT,\
  order_id INT,\
  FOREIGN KEY (employee_id)\
   REFERENCES employee (employee_id),\
  FOREIGN KEY (table_id) \
   REFERENCES tables (table_id),\
  FOREIGN KEY (reservation_id) \
   REFERENCES reservation (reservation_id),\
  FOREIGN KEY (cutlery_id) \
   REFERENCES cutlery (cutlery_id),\
  FOREIGN KEY (ingredient_id) \
   REFERENCES ingredient (ingredient_id),\
  FOREIGN KEY (order_id) \
   REFERENCES orders (order_id)\
 );'

if conn != None:    #Checking if connection is None
    if conn.is_connected(): #Checking if connection is established
        print('MySQL Connection is established')                          
        dbcursor = conn.cursor()    #Creating cursor object
        dbcursor.execute('USE {};'.format(DB_NAME)) #use database    

        for table_name in TABLES:   #loop through TABLES 
            table_description = TABLES[table_name]
            try:
                print('Creating table {}:'.format(table_name), end='')
                dbcursor.execute(table_description)
            except mysql.connector.Error as e:
                if e.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                    print('Table {} already exists.'.format(table_name))
                else:
                    print(e.msg)
            else:
                print('Table {} successfully created.'.format(table_name))       
        
        dbcursor.close()       
        conn.close() #Connection must be closed
    else:
        print('DB connection error')
else:
    print('DBFunc error')
