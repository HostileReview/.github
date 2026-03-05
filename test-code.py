import sqlite3
import os

def get_user(username):
    """Get user from database."""
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # SQL injection vulnerability - intentional for testing
    cursor.execute(f"SELECT * FROM users WHERE username = '{username}'")
    result = cursor.fetchone()
    conn.close()
    return result

def read_file(filename):
    """Read a file from disk."""
    # Path traversal vulnerability - intentional for testing
    path = "/var/data/" + filename
    with open(path, "r") as f:
        return f.read()

API_KEY = "sk-1234567890abcdef"  # Hardcoded secret

def process_data(data):
    password = data.get("password")
    eval(data.get("expression"))  # Code injection
    os.system(f"echo {data.get('name')}")  # Command injection
    return {"status": "ok", "password": password}  # Leaking password in response
