import sqlite3

connection  = sqlite3.connect('flask_hw3.db',check_same_thread = False)
cursor = connection.cursor()

cursor.execute(
    """CREATE TABLE Task(
        Number INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        JobCode INTEGER NOT NULL,
        UserName VARCHAR(16) NOT NULL,
        Task VARCHAR(32) NOT NULL,
        Status VARCHAR(32) NOT NULL
    );"""
)

cursor.execute(
    """CREATE TABLE Users(
        UserName VARCHAR PRIMARY KEY,
        Password VARCHAR(32),
        LastName VARCHAR(16),
        FirstName VARCHAR(16)
    );"""
)


connection.commit()
cursor.close()
connection.close()
