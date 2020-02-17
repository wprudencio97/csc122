import sqlite3

def vehicleTable():
    conn = sqlite3.connect('vehicle.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM vehicleTable")
    rows = cur.fetchall()
    
    for r in rows:
        print(r)

def maintenanceTable():
    conn = sqlite3.connect('vehicle.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM maintenanceTable")
    rows = cur.fetchall()
    
    for r in rows:
        print(r)


vehicleTable()
maintenanceTable()