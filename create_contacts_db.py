import sqlite3


def main():
    # open the txt file
    file = open("contactsData.txt", "r")

    # define the data list
    dataList = []

    # read the lines from the txt file
    for line in file:
        line = line.rstrip("\n")
        dataList.append(line)

    # Create a connection.
    conn = sqlite3.connect('contacts.db')

    # Create a cursor
    c = conn.cursor()
    c.execute("DROP TABLE CONTACT")
    # Create a table
    c.execute("CREATE TABLE CONTACT (" +
              "   CONTACT_ID INTEGER PRIMARY KEY," +
              "   NAME TEXT, " +
              "   EMAIL TEXT)")

    for i in dataList:
        # split i into name and email
        name = i.split(",")[0]
        email = i.split(", ")[1]

        # insert the values into the database
        values = (name.strip("'"), email.strip("'"))
        sql = "INSERT INTO CONTACT (NAME,EMAIL) VALUES (?,?)"
        c.execute(sql, values)

    # Save (commit) the changes
    conn.commit()

    # Close the connection.
    conn.close()

    # close the text file
    file.close()


main()
