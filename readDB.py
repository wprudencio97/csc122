import sqlite3

def main():
    conn = sqlite3.connect('vehicle.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM vehicleTable")
    rows = cur.fetchall()
    
    for r in rows:
        print(r)

main()