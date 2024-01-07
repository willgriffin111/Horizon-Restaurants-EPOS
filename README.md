# Instructions

**Before we start, instructions will be signified by a 'dash(-)' symbol, and quotation marks(" ") will be used to give you information.**

## Pre-requisites:
- **pip install tkcalendar**
- **pip install fpdf2**
- **pip install mysql-connector-python**

## 1. Menu Management
- **Login with Usercode 2, Password=password**
  "This will log you in a chef account where you have access to the Menu Management page."
- **Click on the Menu Management button**
  "The table displays the current menu items stored in the DB."
- **Click on the Add button**
- **Enter the name, category, price, and description and click submit**
  "If you leave even one entry field empty it will return an error messagebox, you can try it."
- **Add as many menu items as you'd like**
- **Select an item then click delete. Delete until you're left with 3 menu items**
- **Try the category filter next to the Delete button to switch between categories**
- **Select an item then click edit to update its details**
  "At least one entry field has to be filled in or an error is returned."
- **Click on home**
- **Click on Account in the top bar**
- **Click on log off**

## 2. View Inventory
- **Login with Usercode 5, Password=password**
  "This will log you in a front of house account, where you have access to Create Reservation, Take Order, and View Inventory."
- **Click on View Inventory**
  "View Inventory is for staff that are not managers, to only view the inventory."
  "Here you will see colour coded rows. Green is for newly added menu items, Red is for menu items deleted from menu and Orange is if the item is low on stock. You cannot edit any menu items here, only managers can. Proceed with instructions for now.."
- **Click on home**
- **Click on Account in the top bar**
- **Click on log off**

## 3. Manage Inventory
- **Login with Usercode=6, Password=password**
  "This will log you in a manager account, where you have access to Creating Reservation Across Branches, Take Orders, View Orders, Manage Inventory, Reports, Discount Management."
- **Click on Manage Inventory**
  "Manage Inventory is for managers and admin, to modify inventory items."
  "Here you will again see colour coded rows. Green is for newly added menu items, Red is for menu items deleted from menu and Orange is if the item is low on stock."
- **Click on rows that are red and click delete**
  "Red means that these menu items are no longer in the menu so they can safely be deleted from the inventory."
- **Click on rows that are green and click delete**
  "Green means that these menu items are newly added and still in the menu so they cannot be deleted from inventory."
- **For rows that are green, double click cells in Qty or Re-order level column to update it**
  "Update the Qty or Re-order level by double clicking on cells."
- **Make Qty lower than Re-order level**
  "This makes the row orange, indicating they are low on stock."

# NOW FOLLOW INSTRUCTIONS CLOSELY
- **Make the Qty of a menu item equal to 2 and remember the item**
- **Make the Qty of a menu item equal to 10 and remember the item**
- **Click on home**

## 4. Take Orders
- **Click on Take Orders**
- **Find the menu item you set the quantity to 2 for, and add it to your order 3 times**
  "So you've ordered one more than there is available in the inventory."
- **Find the menu item you set the quantity to 10 for, and add it to your order 3 times**
- **Click on Pay**
- **Select a table located right above the order**
- **Click on Pay again**
  "It will let you know the amount refunded as there were not enough of it in the inventory. You can try it again, set Qty to 2 and order more than that and you will be refunded your money. If you wish to check the DB, look for the order, then inside that row look for the bill_id and look the bill_id up in the bills table to see that you only paid for the menu item in stock and not when it ran out."

- **Click on home**
- **Click on Account and log off**

## 5. View Orders
- **Login with Usercode=4, Password=password**
  "This will log you in a kitchen staff account, where you have access to View Orders and View Inventory."
- **Click on View Orders**
  "Here you will see the order you created. If you pay attention, only 2 of the 3 were ordered because only 2 were in stock, and the other menu item should say 3. Anyways."
- **Click on Done to complete order**
- **Click on Home**
- **Click on Accounts**
- **Click on Log off**

## 6. Create Reservation
- **Login with Usercode=5, Password=password**
  "This will log you in a front of house account again."
- **Click on Create Reservation: Table number = 3, Party size = 6, date = 2024-01-25, Time=12:00:00**
  "This will create a reservation, if you select a party size greater than 6 for table 3 it will return an error as it is greater than the table capacity."
- **Click on Create Reservation: Table number = 3, Party size = 6, date = 2024-01-25, Time=13:00:00**
  "This will give an error as the table has already been reserved an hour before. You can't reserve tables an hour after or before a reserved time."
- **Select a reservation then click Delete**
- **Double click on a cell to update it**
  "Everything except the reservation_id can be modified."
- **Click on home**
- **Click on Account**
- **Click on log off**

## 7. Create Branch Reservation
- **Login with Usercode=6, Password=password**
  "This will log you in a manager account again."
- **Click on create reservations**
  "It's the exact same thing, except this time you have a dropdown for different restaurants."
  "If you'd like, you can create a reservation and then check the DB."
- **Click on home**

## 8. Discount Management
- **Click on Discount Management**
- **Submit name, value, start, end date and click Add**
  "You will see it pop up on the table."
- **Create another discount where the end date is before the start date**
  "You will get an error for it."
- **Update the cells of the discount by double clicking it**
  "You cannot edit discount id, and cannot make start date go after end date."
- **Create discount for which end date is before today**
- **Create discount for which end date is set to today or after today**
- **Click on home**
- **Click on Take Order**
- **Add items to order**
- **Click on Discounts**
- **Add a discount**
  "You may notice that expired discounts are not shown."
- **Try removing discount**
- **Try staff discount and enter a valid staff id like 3**
  "This is a fixed staff discount that only works when a real staff id is provided."
- **Click on home**

## 9. Reports
- **Click on reports**
- **Click on Sales Reports**
- **For Start Date enter a date before today, for End Date enter a date after today and click update graph**
- **Click download report if you wish to download in PDF format**
- **Click Staff Reports**
  "You can also download staff reports."
- **Click home, Account then log off**

## 10. Reports Across Branches
- **Login with Usercode=1, Password=password**
  "This will log you in as an Admin, where you can access every page."
  "This is the exact same as Reports except now you can choose a restaurant or choose for all restaurants."
- **After you're done, click home and go to Admin Features**
  "Here you can perform CRUD on employee accounts. Use double click to update cells."

**THAT IS ALLLLLL!!**
