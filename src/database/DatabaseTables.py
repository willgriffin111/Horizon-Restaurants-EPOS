import mysql.connector, dbfunc
from mysql.connector import errorcode

conn = dbfunc.getConnection()   #connection to DB
DB_NAME = 'Horizon_Restaurant'             #DB Name
TABLES = {}

# Data types 

# DOUBLE = decimal number 
# INT = whole number 
# VARCHAR = string value
TABLES['RESTAURANT'] = 'CREATE TABLE restaurant (\
  restaurant_id INT NOT NULL AUTO_INCREMENT,\
  PRIMARY KEY (restaurant_id),\
  restaurant_location VARCHAR(64) NOT NULL,\
  restaurant_name VARCHAR(64) NOT NULL,\
  restaurant_capacity INT NOT NULL\
 );' 

TABLES['INVENTORY'] = 'CREATE TABLE inventory (\
  inventory_id INT NOT NULL AUTO_INCREMENT,\
  PRIMARY KEY (inventory_id), \
  restaurant_id INT,\
  inventory_item_name VARCHAR(64) NOT NULL,\
  inventory_item_stock INT NOT NULL,\
  inventory_item_reorder_level INT NOT NULL,\
  inventory_item_type VARCHAR(64) NOT NULL,\
  FOREIGN KEY (restaurant_id) \
  REFERENCES restaurant (restaurant_id)\
);'

TABLES['INVENTORY_RESTAURANT'] = 'CREATE TABLE inventory_restaurant (\
  restaurant_id INT,\
  inventory_id INT,\
  FOREIGN KEY (restaurant_id) \
  REFERENCES restaurant (restaurant_id),\
  FOREIGN KEY (inventory_id) \
  REFERENCES inventory (inventory_id)\
);'


TABLES['MENU'] = 'CREATE TABLE menu(\
  menu_id INT NOT NULL AUTO_INCREMENT,\
  PRIMARY KEY (menu_id),\
  restaurant_id INT,\
  menu_item_name VARCHAR(64) NOT NULL,\
  menu_item_quantity INT NOT NULL,\
  menu_item_category VARCHAR(64) NOT NULL,\
  menu_item_notes VARCHAR(64),\
  FOREIGN KEY (restaurant_id) \
  REFERENCES restaurant (restaurant_id)\
);'

TABLES['MENU_INGREDIENTS'] = 'CREATE TABLE menu_ingredients(\
  menu_id INT NOT NULL,\
  restaurant_id INT,\
  inventory_id INT NOT NULL,\
  inventory_qty_needed INT NOT NULL,\
  PRIMARY KEY (menu_id,inventory_id),\
  FOREIGN KEY (menu_id) REFERENCES menu(menu_id),\
  FOREIGN KEY (inventory_id) REFERENCES inventory(inventory_id),\
  FOREIGN KEY (restaurant_id) \
  REFERENCES restaurant (restaurant_id)\
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
  restaurant_id INT,\
  employee_name VARCHAR(64) NOT NULL,\
  employee_account_type VARCHAR(64) NOT NULL,\
  employee_password VARCHAR(256) NOT NULL,\
  FOREIGN KEY (restaurant_id) \
  REFERENCES restaurant (restaurant_id)\
);'

TABLES['TABLES'] = 'CREATE TABLE tables (\
  table_id INT NOT NULL AUTO_INCREMENT,\
  PRIMARY KEY (table_id),\
  table_num INT NOT NULL,\
  table_capacity INT NOT NULL,\
  restaurant_id INT,\
  FOREIGN KEY (restaurant_id) \
  REFERENCES restaurant (restaurant_id)\
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
  reservation_time TIME NOT NULL,\
  table_id INT,\
  restaurant_id INT,\
  FOREIGN KEY (table_id) \
  REFERENCES tables (table_id),\
  FOREIGN KEY (restaurant_id) \
  REFERENCES restaurant (restaurant_id)\
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
  restaurant_id INT,\
  FOREIGN KEY (bill_id) \
  REFERENCES bill (bill_id),\
  FOREIGN KEY (restaurant_id) \
  REFERENCES restaurant (restaurant_id)\
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

# inventory table - Carries all of the ingredents and cutlery in the database 

#| inventory_id | inventory_item_name | inventory_item_stock     | inventory_item_reorder_level | inventory_item_type |
#|--------------|----------------------|-------------------------|------------------------------|---------------------|
#| 1            | Flour                | 100                     | 20                           | ingredient          |
#| 2            | Tomatoes             | 50                      | 10                           | ingredient          |
#| 3            | Cheese               | 30                      | 5                            | ingredient          |
#| 4            | Pasta                | 80                      | 15                           | ingredient          |

# menu table - Where the order is made 

#| menu_id | menu_item_name | menu_item_quantity | menu_item_category | menu_item_notes |
#|---------|----------------|--------------------|--------------------|-----------------|
#| 1       | Pizza          | 1                  | Main               | More Cheese     |
#| 2       | Pasta          | 1                  | Starter            | N/A             |


# Menu_ingredients table - This will show the ID of both menu items and ingredients used to make them in order to 
# remove it from the stocks.

#| menu_id | inventory_id | inventory_qty_needed |
#|---------|--------------|----------------------|
#| 1       | 1            | 2                    | (Pizza needs 2 units of Flour)
#| 1       | 2            | 3                    | (Pizza needs 3 units of Tomatoes)
#| 2       | 2            | 2                    | (Salad needs 2 units of Tomatoes)
#| 2       | 3            | 1                    | (Salad needs 1 unit of Cheese)
#| 2       | 4            | 4                    | (Salad needs 4 units of Pasta)