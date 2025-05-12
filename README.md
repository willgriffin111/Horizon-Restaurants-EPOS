# Horizon Restaurants EPOS

A multi-branch restaurant management system built with Python (Tkinter GUI) and MySQL (via Docker).  
The system allows restaurant staff to manage menu items, track inventory, create and manage reservations, take customer orders with automatic stock validation and refunds, apply discounts, and generate detailed sales and staff performance reports.  

[Usage Instructions](howToUse.md)


## Requirements

Install dependencies:

```bash
pip install tkcalendar fpdf2 mysql-connector-python passlib matplotlib python-dotenv
```

## How to run 
### Start the MySQL Databse

```bash
docker-compose up --build -d
```

### Run the App (Locally)

```bash
python3 src/main.py
```

### Demo Login Accounts

| Name        | User ID | Password | Role      | Branch |
|-------------|---------|----------|-----------|--------|
| Adam Min    | 1       | Password | ADMIN     | 1      |
| Che Fu      | 2       | Password | CHEF      | 1      |
| Deren Ter   | 3       | Password | DIRECTOR  | 1      |
| Kim Chin    | 4       | Password | KITCHEN   | 1      |
| Fred Staf   | 5       | Password | FRONT     | 1      |
| Man Ager    | 6       | Password | MANAGER   | 1      |

> All other branches (2–14) reuse the same names, passwords, and roles with different User IDs.
