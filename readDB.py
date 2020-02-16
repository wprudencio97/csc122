import sqlite3

def vehicleTable():
    conn = sqlite3.connect('vehicle.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM vehicleTable")
    rows = cur.fetchall()
    
    for r in rows:
        print(r)

def maintenenceTable():
    conn = sqlite3.connect('vehicle.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM maintenenceTable")
    rows = cur.fetchall()
    
    for r in rows:
        print(r)


vehicleTable()