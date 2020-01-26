import sqlite3

def main():
    conn = sqlite3.connect('contacts.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM CONTACT")
    rows = cur.fetchall()
    
    for r in rows:
        print(r)

main()

