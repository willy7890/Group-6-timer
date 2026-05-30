#!/usr/bin/env python3
"""
Learning Databases in Python with SQL using SQLite3

This script demonstrates:
- Table creation with relationships
- CRUD operations (Create, Read, Update, Delete)
- JOIN queries
- Error handling
- Interactive user input
"""

import sqlite3
import sys

def create_tables(cursor):
    """Create users and orders tables with foreign key relationship"""
    # Users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE,
        age INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # Orders table with foreign key to users
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        product_name TEXT NOT NULL,
        price REAL,
        quantity INTEGER DEFAULT 1,
        order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
    """)

def insert_sample_data(cursor):
    """Insert sample users and orders"""
    # Insert users (using INSERT OR IGNORE to avoid duplicates)
    users_data = [
        ('Alice Johnson', 'alice@example.com', 25),
        ('Bob Smith', 'bob@example.com', 30),
        ('Charlie Brown', 'charlie@example.com', 35)
    ]

    cursor.executemany("INSERT OR IGNORE INTO users (name, email, age) VALUES (?, ?, ?)", users_data)

    # Insert orders
    orders_data = [
        (1, 'Laptop', 999.99, 1),
        (1, 'Mouse', 25.50, 2),
        (2, 'Keyboard', 75.00, 1),
        (2, 'Monitor', 299.99, 1),
        (3, 'Headphones', 149.99, 1)
    ]

    cursor.executemany("INSERT OR IGNORE INTO orders (user_id, product_name, price, quantity) VALUES (?, ?, ?, ?)", orders_data)

def display_users(cursor):
    """Display all users"""
    print("\n=== USERS ===")
    cursor.execute("SELECT id, name, email, age FROM users ORDER BY name")
    users = cursor.fetchall()

    if not users:
        print("No users found.")
        return

    for user in users:
        print(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}, Age: {user[3]}")

def display_orders(cursor):
    """Display all orders with user information using JOIN"""
    print("\n=== ORDERS WITH USER INFO ===")
    cursor.execute("""
    SELECT o.id, u.name, o.product_name, o.price, o.quantity,
           ROUND(o.price * o.quantity, 2) as total
    FROM orders o
    JOIN users u ON o.user_id = u.id
    ORDER BY o.order_date DESC
    """)

    orders = cursor.fetchall()

    if not orders:
        print("No orders found.")
        return

    for order in orders:
        print(f"Order ID: {order[0]}, Customer: {order[1]}, Product: {order[2]}, "
              f"Price: ${order[3]}, Qty: {order[4]}, Total: ${order[5]}")

def add_new_user(cursor, conn):
    """Add a new user interactively"""
    print("\n=== ADD NEW USER ===")
    try:
        name = input("Enter name: ").strip()
        if not name:
            print("Name cannot be empty.")
            return

        email = input("Enter email: ").strip()
        if not email:
            print("Email cannot be empty.")
            return

        age_input = input("Enter age: ").strip()
        if not age_input:
            print("Age cannot be empty.")
            return

        age = int(age_input)
        if age < 0 or age > 150:
            print("Please enter a valid age.")
            return

        cursor.execute("INSERT INTO users (name, email, age) VALUES (?, ?, ?)", (name, email, age))
        print(f"User '{name}' added successfully!")

    except ValueError:
        print("Invalid age. Please enter a number.")
    except sqlite3.IntegrityError as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nOperation cancelled.")

def show_user_orders(cursor):
    """Show orders for a specific user"""
    print("\n=== USER ORDERS ===")
    try:
        user_id = input("Enter user ID to see their orders: ").strip()
        if not user_id:
            return

        user_id = int(user_id)

        # Check if user exists
        cursor.execute("SELECT name FROM users WHERE id = ?", (user_id,))
        user = cursor.fetchone()

        if not user:
            print("User not found.")
            return

        print(f"\nOrders for {user[0]}:")

        cursor.execute("""
        SELECT product_name, price, quantity, ROUND(price * quantity, 2) as total, order_date
        FROM orders
        WHERE user_id = ?
        ORDER BY order_date DESC
        """, (user_id,))

        orders = cursor.fetchall()

        if not orders:
            print("No orders found for this user.")
            return

        total_spent = 0
        for order in orders:
            print(f"- {order[0]}: ${order[1]} x {order[2]} = ${order[3]} ({order[4]})")
            total_spent += order[3]

        print(f"\nTotal spent: ${total_spent:.2f}")

    except ValueError:
        print("Invalid user ID. Please enter a number.")
    except KeyboardInterrupt:
        print("\nOperation cancelled.")

def main():
    try:
        with sqlite3.connect('example.db') as conn:
            cursor = conn.cursor()

            # Create tables
            create_tables(cursor)

            # Insert sample data
            insert_sample_data(cursor)

            while True:
                print("\n" + "="*50)
                print("DATABASE LEARNING MENU")
                print("="*50)
                print("1. View all users")
                print("2. View all orders")
                print("3. Add new user")
                print("4. Show user orders")
                print("5. Exit")

                try:
                    choice = input("\nEnter your choice (1-5): ").strip()

                    if choice == '1':
                        display_users(cursor)
                    elif choice == '2':
                        display_orders(cursor)
                    elif choice == '3':
                        add_new_user(cursor, conn)
                    elif choice == '4':
                        show_user_orders(cursor)
                    elif choice == '5':
                        print("Goodbye!")
                        break
                    else:
                        print("Invalid choice. Please enter 1-5.")

                except KeyboardInterrupt:
                    print("\n\nGoodbye!")
                    break
                except Exception as e:
                    print(f"An error occurred: {e}")

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n\nProgram terminated by user.")
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()