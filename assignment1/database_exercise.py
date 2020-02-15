import sqlite3


def main():
    conn = sqlite3.connect('contacts.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM CONTACT")
    rows = cur.fetchall()
    conn.close()

    for r in rows:
        print('Contact ID:', r[0])
        print('Name:', r[1])
        print('Email:', r[2])
        print('-------------------')


main()
