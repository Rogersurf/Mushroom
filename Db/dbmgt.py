import sqlite3
import pandas as pd

# Set up a connection to the SQLite database
DATABASE = 'user_data.db'
conn = sqlite3.connect(DATABASE)
c = conn.cursor()

def setup_db():
    # Create table if not exists
    c.execute('''CREATE TABLE IF NOT EXISTS user_data
                 (user_id INTEGER PRIMARY KEY, email TEXT UNIQUE, mushroom_data TEXT, prediction TEXT)''')
    conn.commit()

def register_user(email, mushroom_details, prediction):
    try:
        c.execute("INSERT INTO user_data (email, mushroom_data, prediction) VALUES (?, ?, ?)", 
                  (email, mushroom_details, prediction))
        conn.commit()
    except sqlite3.IntegrityError:
        raise ValueError("User with this email already exists!")

def fetch_all_users():
    return pd.read_sql_query("SELECT * FROM user_data", conn)

def update_user(email_to_update, new_email, new_mushroom_details):
    c.execute("UPDATE user_data SET email = ?, mushroom_data = ? WHERE email = ?", 
              (new_email, new_mushroom_details, email_to_update))
    if c.rowcount == 0:
        raise ValueError("User with specified email not found!")
    conn.commit()

def delete_user(email_to_delete):
    c.execute("DELETE FROM user_data WHERE email = ?", (email_to_delete,))
    if c.rowcount == 0:
        raise ValueError("User with specified email not found!")
    conn.commit()

def fetch_user_by_email(email):
    c.execute("SELECT * FROM user_data WHERE email = ?", (email,))
    user_data = c.fetchone()
    if user_data:
        return user_data
    else:
        return None

# Add a function to close the database when done
def close_db():
    conn.close()