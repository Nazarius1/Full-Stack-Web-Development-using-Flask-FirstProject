import sqlite3

connection  = sqlite3.connect('flask_hw3.db',check_same_thread = False)
cursor = connection.cursor()

cursor.execute(
    """INSERT INTO ToDoList(
        UserName,
        FirstName,
        LastName,
        Task)
        VALUES(
        'JoKo2020',
        'Nazarius',
        'Suseno',
        'Finishing project'
    );"""
)

cursor.execute(
    """INSERT INTO Users(
        UserName,
        Password,
        LastName,
        FirstName)
        VALUES(
        'JoKo2020',
        'Password123',
        'Suseno',
        'Nazarius'
    );"""
)

connection.commit()
cursor.close()
connection.close()
