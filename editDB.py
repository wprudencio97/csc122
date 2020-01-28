import sqlite3

# define the main function


def main():
    print("Hello")

    # Create a connection.
    conn = sqlite3.connect('contacts.db')

    # Create a cursor
    c = conn.cursor()

    # get the user action and call the appropriate function
    userAction = input("Enter (C)reate, (U)pdate, or (D)elete: ")

    if(userAction.lower() == "c" or userAction.lower() == "create"):
        createRecord(c)
    elif(userAction.lower() == "u" or userAction.lower() == "update"):
        updateRecord(c)
    elif(userAction.lower() == "d" or userAction.lower() == "delete"):
        deleteRecord(c)

    # Save (commit) the changes
    conn.commit()

    # Close the connection.
    conn.close()

# define the create function


def createRecord(c):
    name = input("Enter the name to insert: ")
    email = input("Enter the email to insert: ")
    # insert the values into the database
    values = (name, email)
    sql = "INSERT INTO CONTACT (NAME,EMAIL) VALUES (?,?)"
    c.execute(sql, values)

# define the update record function


def updateRecord(c):
    c.execute("SELECT * FROM CONTACT")
    rows = c.fetchall()

    for r in rows:
        print(r)

    recordID = input("Enter the ID of the Record to update: ")
    name = input("Enter a new name for the record: ")
    email = input("Enter a new email for the record: ")

    sqlite_update_query = "UPDATE CONTACT SET NAME = ?, EMAIL = ? WHERE CONTACT_ID = ?"
    data = (name, email, recordID)
    c.execute(sqlite_update_query, data)

# define the delete record function


def deleteRecord(c):
    c.execute("SELECT * FROM CONTACT")
    rows = c.fetchall()

    for r in rows:
        print(r)

    recordID = input("Enter the ID of the Record to delete: ")

    sqlite_update_query = "DELETE FROM CONTACT WHERE CONTACT_ID = ?"
    c.execute(sqlite_update_query, (recordID,))


main()
